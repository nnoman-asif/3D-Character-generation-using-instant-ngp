from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox
class Step_2(QWidget):
    def __init__(self):
        super().__init__()
        #box  for checking 
        self.yesButton = QPushButton('Yes')
        self.noButton = QPushButton('No')
        self.start_button = QPushButton('Start')
        self.cancel_button = QPushButton('Cancel')
        self.show_button = QPushButton('Show Images')

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.group_box=QGroupBox()
 
        self.choice=None
    
        self.layout_grid()

    def layout_grid(self):
        self.hbox.addWidget(self.yesButton)
        self.hbox.addWidget(self.noButton)
        # Create a vertical layout for the widget
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.start_button)
        #self.vbox.addWidget(self.cancel_button)
        self.group_box.setLayout(self.vbox)

    
       
        
    
