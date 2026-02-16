import numpy as np
import cv2
import os
from isNetModel.models.data_loader_cache import normalize, im_reader, im_preprocess 
import torch
from torch.autograd import Variable
from torchvision import transforms
import torch.nn.functional as F
from isNetModel.models.isnet import ISNetDIS

class GOSNormalize(object):
    '''Normalize the Image using torch.transforms'''
    def __init__(self, mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225]):
        self.mean = mean
        self.std = std

    def __call__(self,image):
        image = normalize(image,self.mean,self.std)
        return image

def load_image(im_path, hypar):
    im = im_reader(im_path)
    im, im_shp = im_preprocess(im, hypar["cache_size"])
    im = torch.divide(im,255.0)
    shape = torch.from_numpy(np.array(im_shp))
    transform =  transforms.Compose([GOSNormalize([0.5,0.5,0.5],[1.0,1.0,1.0])])
    return transform(im).unsqueeze(0), shape.unsqueeze(0) # make a batch of image, shape

def build_model(hypar,device):
    net = hypar["model"]#GOSNETINC(3,1)
    # convert to half precision
    if(hypar["model_digit"]=="half"):
        net.half()
        for layer in net.modules():
            if isinstance(layer, torch.BatchNorm2d):
                layer.float()
    net.to(device)
    if(hypar["restore_model"]!=""):
        net.load_state_dict(torch.load(hypar["model_path"]+"/"+hypar["restore_model"],map_location=device))
        net.to(device)
    net.eval()  
    return net

def predict(net,  inputs_val, shapes_val, hypar, device):
    '''
    Given an Image, predict the mask
    '''
    net.eval()

    if(hypar["model_digit"]=="full"):
        inputs_val = inputs_val.type(torch.FloatTensor)
    else:
        inputs_val = inputs_val.type(torch.HalfTensor)
  
    inputs_val_v = Variable(inputs_val, requires_grad=False).to(device) # wrap inputs in Variable
    ds_val = net(inputs_val_v)[0] # list of 6 results
    pred_val = ds_val[0][0,:,:,:] # B x 1 x H x W    # we want the first one which is the most accurate prediction
    ## recover the prediction spatial size to the orignal image size
    pred_val = torch.squeeze(F.upsample(torch.unsqueeze(pred_val,0),(shapes_val[0][0],shapes_val[0][1]),mode='bilinear'))
    ma = torch.max(pred_val)
    mi = torch.min(pred_val)
    pred_val = (pred_val-mi)/(ma-mi) # max = 1
    if device == 'cuda': torch.cuda.empty_cache()
    return (pred_val.detach().cpu().numpy()*255).astype(np.uint8) # it is the mask we need

def run_model():
    hypar = {} # parameters for inferencing
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    hypar["model_path"] =current_script_path+"/saved_models" ## load trained weights from this path
    hypar["restore_model"] = "isnet.pth" ## name of the to-be-loaded weights
    hypar["interm_sup"] = False ## indicate if activate intermediate feature supervision
    ##  choose floating point accuracy --
    hypar["model_digit"] = "full" ## indicates "half" or "full" accuracy of float number
    hypar["seed"] = 0
    hypar["cache_size"] = [1024, 1024] ## cached input spatial resolution, can be configured into different size
    ## data augmentation parameters ---
    hypar["input_size"] = [1024, 1024] ## mdoel input spatial size, usually use the same value hypar["cache_size"], which means we don't further resize the images
    hypar["crop_size"] = [1024, 1024] ## random crop size from the input, it is usually set as smaller than hypar["cache_size"], e.g., [920,920] for data augmentation
    hypar["model"] = ISNetDIS()

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(device)
    net=build_model(hypar, device)
    return net,hypar,device 

def isnet_remover(src="", dst=""):
    if src!="" and dst!="":
        net,hypar,device=run_model()
        os.makedirs(dst, exist_ok=True)
        for i in [filename for filename in os.listdir(src) if filename.endswith(".jpg")]:
            input_path = os.path.join(src, i)
            output_path = os.path.join(dst, i)
            image_tensor, orig_size = load_image(input_path, hypar)
            mask = predict(net, image_tensor, orig_size, hypar, device)
            input_image = cv2.imread(input_path, 1)
            cv2.imwrite(output_path, cv2.bitwise_and(input_image, input_image, mask=mask))





