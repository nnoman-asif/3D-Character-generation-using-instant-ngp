from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,QPushButton,QWidget,QLabel,
                            QAction,QToolBar, QToolBar, QStackedWidget,QDesktopWidget,
                            QScrollArea,QGroupBox,QFileDialog)
from New_Video_player import VideoPlayer
from Step_1 import Step_1
from Step_2 import Step_2
from Step_4 import Step_4
from My_images_viewer import ViewerWidget
from model_view import Model_Viewer
from loadingbar import LoadingProgressBar
from terminal_widget import OutputWidget
from directory_maker import NewProjectDialog
 
def QmainWindowConstruct(self):        
    self.dropMenu=QLabel("Drop everything here")
    self.VideoPlayer_widget = VideoPlayer()
    self.Image_viewer_widget=ViewerWidget()
    self.loading_bar=LoadingProgressBar()

    #video and folder path
    self.video_File_Path=""
    self.directory_Path=""
    
    self.directory_Maker=NewProjectDialog()
    #multiple Steps
    self.Step_1=Step_1()
    self.Step_2=Step_2()
    self.Step_2.yesButton.setText("Human")
    self.Step_2.noButton.setText("Object")
    self.Step_3=Step_2()
    self.Step_4=Step_4()
    self.model_viewer_1=Model_Viewer()
    self.model_viewer_2=Model_Viewer()
    self.model_viewer_3=Model_Viewer()
    self.widget = QWidget() 
    

    #toolbar and scrollbar
    self.toolbar = QToolBar('Toolbar')
    self.Htoolbar = QToolBar('HToolbar')
    self.Htoolbarlayout=QHBoxLayout()
    self.toolbar_Vlayout=QVBoxLayout()
    self.scrollbar_toolbar = QScrollArea()

    #stacked widgets
    self.stackedWidget = QStackedWidget()
    
    #colmap
    self.worker = None

    #htoolbar buttons
    self.newAction = QPushButton('Browse Video')
    self.clearAction = QPushButton('Clear')
    self.saveAction = QPushButton('Browse Folder')
    self.cancelAction = QPushButton('Cancel')
    
    self.showAction = QPushButton('Show Images')
    self.proceedAction = QPushButton('Proceed')
    
    self.showbriAction = QPushButton('Show Background Removed Images')
    self.showCAction = QPushButton('Show Cartoonized Images')
    self.showmAction = QPushButton('Show Model')
    self.showvideoAction = QPushButton('Show video')
    self.showtmAction = QPushButton('Show textured model')
    
    self.showfAction = QPushButton('Show fbx model')
    
    self.closeToolbarAction=QPushButton('Hide Toolbar')
    self.openToolbarAction=QPushButton('Show Toolbar')

    self.exitAction = QPushButton('Exit')

    # set the size of the main window
    screen = QDesktopWidget().screenGeometry()
    width, height = screen.width(), screen.height()
    self.setGeometry(width*0.03, height*0.05, width-(width*0.05), height-(height*0.1))
    self.toolbar.setFixedWidth(int(width/4.3))
        
    #OUTPUT widget
    self.output_widget = OutputWidget()
    self.output_widget.groupbox.setFixedHeight(height/7)

    self.worker = None
    #self.cancelAction.clicked.connect(self.close)

    hToolBar_widget_display(self)
    VToolBar(self)
    Scroll_toolbar(self)
    stacked_Windows(self)
    DropMenu(self)
    meshFuction(self)
 
    hide_inital_widgets(self)

   


def Scroll_toolbar(self):
    self.scrollbar_toolbar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.scrollbar_toolbar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.scrollbar_toolbar.setStyleSheet("""QScrollBar::handle
                                            {background-color: #06426E;
                                            border: 0.5px solid white;
                                            }""")
    self.scrollbar_toolbar.setWidgetResizable(True)

def hToolBar_widget_display(self):#htoolbar working
    self.Htoolbar.setMovable(True)
    #self.Htoolbar.setAllowedAreas(Qt.TopToolBarArea | Qt.BottomToolBarArea)
    self.Htoolbarlayout.setContentsMargins(5, 0, 5, 0)
    
    self.Htoolbarlayout.addWidget(self.newAction)
    self.Htoolbarlayout.addWidget(self.saveAction)
    self.Htoolbarlayout.addWidget(self.clearAction)
    self.Htoolbarlayout.addWidget(self.exitAction)
    self.Htoolbarlayout.addWidget(self.proceedAction)
   

    self.Htoolbarlayout.addWidget(self.openToolbarAction)
    self.Htoolbarlayout.addWidget(self.closeToolbarAction)

    #self.Htoolbarlayout.addWidget(self.showvideoAction)

    htoolbargroupbox=QGroupBox()
    htoolbargroupbox.setLayout(self.Htoolbarlayout)
    self.Htoolbar.addWidget(htoolbargroupbox)

    
    #l1.__animation
    self.Htoolbar.addWidget(self.loading_bar)

def hide_inital_widgets(self):
    self.proceedAction.hide()
    # self.closeToolbarAction.hide()
    # self.openToolbarAction.hide()

def VToolBar(self):# vertical toolbar widgets
    self.toolbar.setMovable(True)
    self.toolbar.setAllowedAreas(Qt.RightToolBarArea | Qt.LeftToolBarArea)
    self.addToolBar(Qt.TopToolBarArea,self.Htoolbar)
    self.addToolBar(Qt.RightToolBarArea,self.toolbar)

    self.toolbar_Vlayout.addWidget(self.Step_1.groupbox)
    self.toolbar_Vlayout.addWidget(self.Step_2.group_box)
    self.toolbar_Vlayout.addWidget(self.Step_3.group_box)
    self.toolbar_Vlayout.addWidget(self.Step_4.group_box)
    
    
    self.toolbar_Vlayout.addWidget(self.model_viewer_2)
    #self.toolbar_Vlayout.addWidget(self.model_viewer_3)

    self.widget.setLayout(self.toolbar_Vlayout)
    self.scrollbar_toolbar.setWidget(self.widget)
    self.toolbar.addWidget(self.scrollbar_toolbar)



    self.Step_2.group_box.hide()
    self.Step_3.group_box.hide()
    self.Step_4.group_box.hide()
    self.model_viewer_2.groupbox.hide()
    

def stacked_Windows(self):
    groupBOX=QGroupBox()
    dropMenulayout=QVBoxLayout()
    dropMenulayout.addWidget(self.dropMenu)
    groupBOX.setLayout(dropMenulayout)

    self.stackedWidget.addWidget(groupBOX)
    self.stackedWidget.addWidget(self.VideoPlayer_widget)
    self.stackedWidget.addWidget(self.Image_viewer_widget)

    action1 = QAction('Page 1', self)
    action1.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
    self.toolbar.addAction(action1)

    action2 = QAction('Page 2', self)
    action2.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    self.toolbar.addAction(action2)

    action3 = QAction('Page 3', self)
    action3.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))
    self.toolbar.addAction(action3)

    self.toolbar.addWidget(self.output_widget.groupbox)


def DropMenu(self):
    self.dropMenu.setAlignment(Qt.AlignCenter)
    self.dropMenu.setStyleSheet("background-color: #06426E")

def meshFuction(self):
    pass

def select_file_dialog(folder_path):
        # Open the file dialog for selecting a file
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("JSON files (*.json)")
        file_dialog.setDirectory(folder_path)
        file_dialog.setWindowTitle('Select File')
        
        if file_dialog.exec_():
            pass