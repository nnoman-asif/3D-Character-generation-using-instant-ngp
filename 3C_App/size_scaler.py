from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import os

def scaler(Mw):# icons are scaled and tool tip of buttons
    file_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(file_path)

    path= dir_path+"/icons3/"

    Mw.Step_2.yesButton.setIcon(QIcon(path+'Untitled-19.png'))
    Mw.Step_2.yesButton.setIconSize(QSize(32, 32))

    Mw.Step_2.noButton.setIcon(QIcon(path+'Untitled-20.png'))
    Mw.Step_2.noButton.setIconSize(QSize(32, 32))

    Mw.Step_3.yesButton.setIcon(QIcon(path+'Untitled-19.png'))
    Mw.Step_3.yesButton.setIconSize(QSize(32, 32))

    Mw.Step_3.noButton.setIcon(QIcon(path+'Untitled-20.png'))
    Mw.Step_3.noButton.setIconSize(QSize(32, 32))

    Mw.newAction.setIcon(QIcon(path+'Untitled-9.png'))
    Mw.newAction.setIconSize(QSize(32, 32))

    Mw.saveAction.setIcon(QIcon(path+'Untitled-4.png'))
    Mw.saveAction.setIconSize(QSize(32, 32))

    Mw.clearAction.setIcon(QIcon(path+'Untitled-23.png'))
    Mw.clearAction.setIconSize(QSize(32, 32))

    Mw.exitAction.setIcon(QIcon(path+'Untitled-5.png'))
    Mw.exitAction.setIconSize(QSize(32, 32))

    Mw.Step_4.run_ngp.setIcon(QIcon(path+'Untitled-22.png'))
    Mw.Step_4.run_ngp.setIconSize(QSize(32, 32))

    Mw.Image_viewer_widget.prev_button.setIcon(QIcon(path+'Untitled-11.png'))
    Mw.Image_viewer_widget.prev_button.setIconSize(QSize(32, 32))
    Mw.Image_viewer_widget.next_button.setIcon(QIcon(path+'Untitled-6.png'))
    Mw.Image_viewer_widget.next_button.setIconSize(QSize(32, 32))
    Mw.Image_viewer_widget.image_number.setIcon(QIcon(path+'Untitled-24.png'))
    Mw.Image_viewer_widget.image_number.setIconSize(QSize(32, 32))

    Mw.VideoPlayer_widget.rotateButtonl.setIcon(QIcon(path+'Untitled-2.png'))
    Mw.VideoPlayer_widget.rotateButtonl.setIconSize(QSize(32, 32))
    Mw.VideoPlayer_widget.rotateButtonr.setIcon(QIcon(path+'Untitled-1.png'))
    Mw.VideoPlayer_widget.rotateButtonr.setIconSize(QSize(32, 32))

    Mw.model_viewer_1.Next_button.setIcon(QIcon(path+'Untitled-21.png'))
    Mw.model_viewer_1.Next_button.setIconSize(QSize(32, 32))
    Mw.model_viewer_1.button.setIcon(QIcon(path+'Untitled-8.png'))
    Mw.model_viewer_1.button.setIconSize(QSize(32, 32))
    Mw.model_viewer_1.button.setToolTip("It is used for mesh visualization")

    Mw.model_viewer_2.Next_button.setIcon(QIcon(path+'Untitled-21.png'))
    Mw.model_viewer_2.Next_button.setIconSize(QSize(32, 32))
    Mw.model_viewer_2.button.setIcon(QIcon(path+'Untitled-8.png'))
    Mw.model_viewer_2.button.setIconSize(QSize(32, 32))
    Mw.model_viewer_2.button.setToolTip("It is used for mesh visualization")
    
    Mw.model_viewer_3.Next_button.setIcon(QIcon(path+'Untitled-21.png'))
    Mw.model_viewer_3.Next_button.setIconSize(QSize(32, 32))
    Mw.model_viewer_3.button.setIcon(QIcon(path+'Untitled-8.png'))
    Mw.model_viewer_3.button.setIconSize(QSize(32, 32))
    Mw.model_viewer_3.button.setToolTip("It is used for mesh visualization")
    return Mw
