from rembg import remove
import os
import json 
import shutil
from isNetModel.DIS_model import isnet_remover
from Cartoonizer.cartoonized import cartoonize
from PyQt5.QtCore import QThread 
import pymeshlab

def copy_video(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print("Video copied successfully!")
    except FileNotFoundError:
        print("Source file not found!")
    except IsADirectoryError:
        print("Source is a directory, not a file!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# human segmentation
def remove_Background(folder_path="",output_folder_path=""):
    if folder_path!="" and output_folder_path!="":
        os.makedirs(output_folder_path,exist_ok=True)
        for k in [filename for filename in os.listdir(folder_path) if filename.endswith(".jpg")]:
            with open(folder_path+'/'+k, 'rb') as i:
                input = i.read()
                output = remove(input)
            with open(output_folder_path+'/'+k, 'wb') as o:
                o.write(output)

# Update json file path
def update_json_path(src, img_src):
    data=None
    with open(src) as f:
        data = json.load(f)
        for i, frame in enumerate(data['frames']):
            data['frames'][i]['file_path'] = os.path.join(img_src, os.path.basename(frame['file_path']))

    with open(src, 'w') as out_file:
        json.dump(data, out_file, indent=4)


class run_object_extractor(QThread):
    def __init__(self):
        super().__init__()
        self.src=""
        self.dst=""
        
    def run(self):
        isnet_remover(self.src,self.dst)
        remove_Background(self.dst,self.dst)


class run_human_extractor(QThread):
    def __init__(self):
        super().__init__()
        self.src=""
        self.dst=""
        
    def run(self):
       remove_Background(self.src,self.dst)

class run_Cartoonizer(QThread):
    def __init__(self):
        super().__init__()
        self.src=""
        self.dst=""
    def run(self):
        cartoonize(self.src,self.dst)
        remove_Background(self.dst,self.dst)

class run_copy_video(QThread):
    def __init__(self):
        super().__init__()
        self.src=""
        self.dst=""
       
    def run(self):
        copy_video(self.src,self.dst)
       
class run_update_json_file(QThread):
    def __init__(self):
        super().__init__()
        self.src=""
        self.dst=""
    
    def run(self):
        update_json_path(self.src,self.dst)
     
class get_Texture(QThread):
    def __init__(self): 
        super().__init__()
        self.ms = pymeshlab.MeshSet()
        self.path=""

        self.quality=1
        self.dst=""
        

    def runned(self):
        x=0
        if self.quality==1:
            x=1024
        elif self.quality==2:
            x=2048
        elif self.quality==3:
            x=4096
        elif self.quality==4:
            x=8192

        self.ms.load_new_mesh(self.path)
        self.ms.apply_filter('remove_isolated_pieces_wrt_diameter', mincomponentdiag=pymeshlab.Percentage(10),removeunref = True)
        self.ms.apply_filter('compute_normal_for_point_clouds')
        self.ms.apply_filter('generate_surface_reconstruction_screened_poisson')
        self.ms.apply_filter('parametrization_trivial_per_triangle',textdim=x,border=0,method=0)
        self.ms.apply_filter('transfer_vertex_attributes_to_texture_1_or_2_meshes',sourcemesh=0,targetmesh=1,attributeenum=0,textname="transforms_base.png",textw=x,texth=x)
        self.ms.save_current_mesh(self.dst)
        print('model generated')

    def run(self):
        self.runned()

