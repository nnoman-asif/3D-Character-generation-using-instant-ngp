import os
import sys
from PyQt5.QtCore import Qt, QUrl,QEvent,QSize, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import (QFileDialog, QHBoxLayout, QVBoxLayout, QSlider, QMessageBox
        ,QMainWindow,QLabel, QAction,QToolBar, QToolBar, QStackedWidget, QLineEdit,QDesktopWidget,QScrollArea,QGroupBox)
from PyQt5.QtGui import QIcon
from New_Video_player import VideoPlayer
from My_images_viewer import ViewerWidget

import argparse
from QmainWindowConstructor import QmainWindowConstruct
import subprocess
from models_Json import run_object_extractor,run_human_extractor,get_Texture,run_Cartoonizer,run_copy_video,run_update_json_file

from threading import Thread
from video_to_images import videoToImages
from multiprocessing import Process

def select_file_dialog(folder_path):
    # Open the file dialog for selecting a file
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    file_dialog.setNameFilter("JSON files (*.json)")
    file_dialog.setDirectory(folder_path)
    file_dialog.setWindowTitle('Select File')
    
    if file_dialog.exec_():
        pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Display windows
        QmainWindowConstruct(self)

        self.runOe=run_object_extractor()
        self.runHe=run_human_extractor()
        self.runC=run_Cartoonizer()
        self.runCv=run_copy_video()
        self.runUj=run_update_json_file()
        self.runTm=get_Texture()
        
        #
        # sys.stdout = self.output_widget
        # sys.stderr = self.output_widget
        
        self.setAcceptDrops(True)
        self.installEventFilter(self)
        self.hToolBar_widget()
        self.vToolBar_widget()
        self.setCentralWidget(self.stackedWidget)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to exit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.cancel_worker()
            self.model_viewer_1.closeProcess()
            self.model_viewer_2.closeProcess()
            self.model_viewer_3.closeProcess()
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        else:
            event.ignore()
            
    def start_worker(self):
        args = argparse.Namespace()
        args.video_in = self.runCv.dst
        args.video_fps = self.Step_1.fps.value
        args.run_colmap = True
        args.out = self.directory_Maker.Path_Dictionary["json_file"]
        args.overwrite = True
        args.aabb_scale = self.Step_1.aabb.value
        #self.worker.args=args
        self.worker = videoToImages("C:/Users/hp/Downloads/fyp_demo/Instant-NGP-for-GTX-1000/scripts/colmap2nerf.py",args)
        self.worker.finished.connect(self.display_Step2)
        self.worker.start()
        #print("working1s")
        
    def cancel_worker(self):
        self.Step_1.start_button.setEnabled(True)
        if self.worker is not None and self.worker.isRunning():
            self.worker.stopped()

    def copying_video(self):
        self.Step_1.start_button.setEnabled(False)
        self.runCv.src=self.video_File_Path
        self.runCv.dst=self.directory_Maker.Path_Dictionary["video_folder"]+"/video.mp4"
        self.runCv.finished.connect(self.start_worker)
        self.runCv.start()
           #self.gg()
        #print("working")
        

    def vToolBar_widget(self):#vtoolbar working
        self.toolbar.hide()
        #step1

        self.Step_1.start_button.clicked.connect(self.copying_video)
        self.Step_1.cancel_button.clicked.connect(self.cancel_worker)

        #step2
        self.Step_2.yesButton.clicked.connect(self.on_HumanButton_clicked)
        self.Step_2.noButton.clicked.connect(self.on_ObjectButton_clicked)
        self.Step_2.start_button.clicked.connect(self.background_removal_Process)
        #step3
        self.Step_3.yesButton.clicked.connect(self.on_YesButton_clicked)
        self.Step_3.noButton.clicked.connect(self.on_NoButton_clicked)
        self.Step_3.start_button.clicked.connect(self.cartoonizer_Process)
       
        #step4
        self.Step_4.run_ngp.clicked.connect(self.run_exe)
        self.Step_4.Viewmesh.clicked.connect(self.model_viewer_2.visualize_mesh)
        self.Step_4.next.clicked.connect(self.run_conversion)

    def run_conversion(self):

        self.directory_Maker.Path_Dictionary['point_cloud']=self.model_viewer_2.path
        
        self.runTm.path=self.directory_Maker.Path_Dictionary['point_cloud']
        self.runTm.dst=self.directory_Maker.Path_Dictionary['textured_mesh']
        self.runTm.start()
        #self.runOe.finished.connect(self.display_Step3)
        
        #self.runC.finished.connect(self.display_Step4)


    def display_Step2(self):
        self.Step_2.group_box.show()
        self.Step_1.groupbox.hide()
        self.stackedWidget.setCurrentIndex(2)
        #print(self.Path_Dictionary["original_images_folder"])
        self.Image_viewer_widget.run(self.directory_Maker.Path_Dictionary["original_images_folder"])
        

    def display_Step3(self):
        self.Step_3.group_box.show()
        self.Step_2.group_box.hide()
        self.stackedWidget.setCurrentIndex(2)
        self.Image_viewer_widget.run(self.directory_Maker.Path_Dictionary["background_removed"])

    def display_Step4(self):
        self.runUj.src=self.directory_Maker.Path_Dictionary["json_file"]
        self.runUj.dst=self.directory_Maker.Path_Dictionary["cartoonized_folder"]+'/'
        self.runUj.start()
        self.Step_4.group_box.show()
        self.Step_3.group_box.hide()
        self.stackedWidget.setCurrentIndex(2)
        self.Image_viewer_widget.run(self.directory_Maker.Path_Dictionary["cartoonized_folder"])
        
    def display_Step4b(self):
        self.runUj.src=self.directory_Maker.Path_Dictionary["json_file"]
        self.runUj.dst=self.directory_Maker.Path_Dictionary["background_removed"]+'/'
        self.runUj.start()
        self.Step_4.group_box.show()
        self.Step_3.group_box.hide()
        self.stackedWidget.setCurrentIndex(2)
        self.Image_viewer_widget.run(self.directory_Maker.Path_Dictionary["background_removed"])


    def display_mesh_step(self):
        self.Step_4.group_box.hide()
        self.model_viewer_1.show()
        pass
    
    def display_textured_mesh_step(self):
        self.model_viewer_1.hide()
        self.model_viewer_2.show()
        pass

    def display_fbx_textured_mesh_step(self):
        self.model_viewer_2.hide()
        self.model_viewer_3.show()
        pass
        

    def hToolBar_widget(self):#htoolbar working
        # create File menu and its actions
        self.newAction.clicked.connect(self.openFile)
        self.saveAction.clicked.connect(self.browse_folder)
        self.clearAction.clicked.connect(self.clearedAction)
        self.exitAction.clicked.connect(self.close)
        self.proceedAction.clicked.connect(self.proceed_func)
        self.closeToolbarAction.clicked.connect(self.toolbar.hide)
        self.openToolbarAction.clicked.connect(self.toolbar.show)
        #exit menu

    def background_removal_Process(self):
        self.Step_2.start_button.setEnabled(False)


        if self.Step_2.choice:
            self.runHe.src=self.directory_Maker.Path_Dictionary["original_images_folder"]
            self.runHe.dst=self.directory_Maker.Path_Dictionary["background_removed"]
            
            self.runHe.start()
            self.runHe.finished.connect(self.display_Step3)
       
        else:
            self.runOe.src=self.directory_Maker.Path_Dictionary["original_images_folder"]
            self.runOe.dst=self.directory_Maker.Path_Dictionary["background_removed"]
            self.runOe.finished.connect(self.display_Step3)
            self.runOe.start()
           #self.gg()
            #self.runOe.finished.connect(self.display_Step3)
           # self.run_object_remover()
            pass

    def cartoonizer_Process(self):
        self.Step_3.start_button.setEnabled(False)
        if self.Step_3.choice:
            self.runC.src=self.directory_Maker.Path_Dictionary["background_removed"]
            self.runC.dst=self.directory_Maker.Path_Dictionary["cartoonized_folder"]
            self.runC.start()
           #self.gg()
            self.runC.finished.connect(self.display_Step4)
            
        else:
            self.display_Step4b()
           # self.run_object_remover()
            
        
    def get_texture(self):
        self.model_viewer_1.path

    def proceed_func(self):
        self.directory_Maker.show()
        self.setAcceptDrops(False)
        self.directory_Maker.finished.connect(self.dialog_finished)

    def dialog_finished(self):
        self.toolbar.show()
        self.proceedAction.hide()
        self.newAction.hide() 
        self.clearAction.hide()
        self.saveAction.hide()
        self.closeToolbarAction.show()
        self.openToolbarAction.show()

    def on_HumanButton_clicked(self):
        self.Step_2.yesButton.setStyleSheet("""QPushButton
                     {color:black;
                            background-color: #39FF14;}""")
        self.Step_2.noButton.setStyleSheet("")
        self.Step_2.choice=True

    def on_ObjectButton_clicked(self):
        self.Step_2.noButton.setStyleSheet("""QPushButton
                     {color:black;
                     background-color: #FF3131;}""")
        self.Step_2.yesButton.setStyleSheet("")
        self.Step_2.choice=False

    def on_YesButton_clicked(self):
        self.Step_3.yesButton.setStyleSheet("""QPushButton
                     {color:black;
                            background-color: #39FF14;}""")
        self.Step_3.noButton.setStyleSheet("")
        self.Step_3.choice=True

    def on_NoButton_clicked(self):
        self.Step_3.noButton.setStyleSheet("""QPushButton
                     {color:black;
                     background-color: #FF3131;}""")
        self.Step_3.yesButton.setStyleSheet("")
        self.Step_3.choice=False
        
    def run_exe(self): # run instant ngp exe 
        subprocess.Popen('C:/Users/hp/Downloads/fyp_nerf/Instant-NGP-for-GTX-1000/instant-ngp.exe')

    def clearedAction(self):
        self.stackedWidget.setCurrentIndex(0)
        self.VideoPlayer_widget.deleteLater()
        self.Image_viewer_widget.deleteLater()
        self.VideoPlayer_widget=VideoPlayer()
        self.Image_viewer_widget=ViewerWidget()
        self.Step_1.groupbox.show()
        self.stackedWidget.addWidget(self.VideoPlayer_widget)
        self.stackedWidget.addWidget(self.Image_viewer_widget)
        path='icons1/'
        self.Image_viewer_widget.prev_button.setIcon(QIcon(path+'Untitled-11.png'))
        self.Image_viewer_widget.prev_button.setIconSize(QSize(32, 32))
        self.Image_viewer_widget.next_button.setIcon(QIcon(path+'Untitled-6.png'))
        self.Image_viewer_widget.next_button.setIconSize(QSize(32, 32))
        self.Image_viewer_widget.image_number.setIcon(QIcon(path+'Untitled-24.png'))
        self.Image_viewer_widget.image_number.setIconSize(QSize(32, 32))
        self.VideoPlayer_widget.rotateButtonl.setIcon(QIcon(path+'Untitled-2.png'))
        self.VideoPlayer_widget.rotateButtonl.setIconSize(QSize(32, 32))
        self.VideoPlayer_widget.rotateButtonr.setIcon(QIcon(path+'Untitled-1.png'))
        self.VideoPlayer_widget.rotateButtonr.setIconSize(QSize(32, 32))
        self.proceedAction.hide()

    def browse_folder(self):#folder
        ###3d model viewer
        self.directory_Path=QFileDialog.getExistingDirectory(self, "Select Folder")
        print(self.directory_Path)
        if self.directory_Path!="":
            self.stackedWidget.setCurrentIndex(2)
            self.Image_viewer_widget.run(self.directory_Path)
            self.Step_1.groupbox.hide()
            self.proceedAction.show()
            self.VideoPlayer_widget.mediaPlayer.pause()

    def openFile(self):#Browse video
        self.video_File_Path, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "Video Files (*.mp4 *.avi *.mkv)")
        if self.video_File_Path != "":
            print(self.video_File_Path)
            self.Step_1.pth=self.video_File_Path
            self.stackedWidget.setCurrentIndex(1)
            self.VideoPlayer_widget.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_File_Path)))
            #self.VideoPlayer_widget.mediaPlayer.play()
            self.proceedAction.show()

    def eventFilter(self, obj, event):
        # Handle drag and drop events for the video widget
        if event.type() == QEvent.DragEnter:
            event.acceptProposedAction()
        elif event.type() == QEvent.Drop:
            urls = event.mimeData().urls()
            if urls and urls[0].scheme() == 'file':
                self.video_File_Path = str(urls[0].toLocalFile())
                if self.video_File_Path.endswith(('.mp4', '.avi', '.mkv')):
                    self.VideoPlayer_widget.close()
                    self.stackedWidget.setCurrentIndex(1)
                    self.Step_1.pth=self.video_File_Path
                    self.VideoPlayer_widget.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_File_Path)))
                    self.VideoPlayer_widget.mediaPlayer.play()
                    self.proceedAction.show()
                    return True
            for url in urls:
                if url.isLocalFile() and os.path.isdir(url.toLocalFile()):
                    #self.label.setText(urls.toLocalFile())
                    print(url.toLocalFile())
                    self.directory_Path=url.toLocalFile()
                    self.stackedWidget.setCurrentIndex(2)
                    self.Image_viewer_widget.run( self.directory_Path)
                    self.Step_1.groupbox.hide()
                    self.VideoPlayer_widget.mediaPlayer.pause()
                    self.proceedAction.show()
                    break
        return super().eventFilter(obj, event)