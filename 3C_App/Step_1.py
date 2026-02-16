from PyQt5.QtWidgets import (QVBoxLayout, QWidget,QGroupBox,QPushButton)
from RadioButtons import radio_Buttons

class Step_1(QWidget):
    def __init__(self):
        super().__init__()#radio buttons
        #group boxes
        self.groupbox = QGroupBox()
        self.aabb=radio_Buttons(['1', '2', '4', '8'],['16', '32', '64', '128'],"Aabb Scale",False)
        self.fps=radio_Buttons(['0.1', '0.5', '1', '2'],['3', '4', '5', '8'],"Video fps",True)
        #self.pth=""
        #Vlayouts
        self.main_lay = QVBoxLayout()
        self.start_button=QPushButton("Start")
        self.cancel_button=QPushButton("Cancel")
        self.all_Layouts()
     
    def all_Layouts(self):
        self.main_lay.addWidget(self.aabb.groupbox)
        self.main_lay.addWidget(self.fps.groupbox)
        self.main_lay.addWidget(self.start_button)
        self.main_lay.addWidget(self.cancel_button)
        self.groupbox.setLayout(self.main_lay)

    