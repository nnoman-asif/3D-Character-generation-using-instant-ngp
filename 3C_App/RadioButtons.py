from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QWidget,QGroupBox,QRadioButton)
class radio_Buttons(QWidget):
    def __init__(self,labels_row1,labels_row2,name,k):
        super().__init__()
        
        self.hbox = QHBoxLayout()
        for label in labels_row1:
            radio = QRadioButton(label)
            if k==True:
                radio.clicked.connect(self.onRadioButtonClicked)
            else:
                radio.clicked.connect(self.onRadioButtonClicked1)
            self.hbox.addWidget(radio)

        self.h1box = QHBoxLayout()
        for label in labels_row2:
            radio = QRadioButton(label)
            if k==True:
                radio.clicked.connect(self.onRadioButtonClicked)
            else:
                radio.clicked.connect(self.onRadioButtonClicked1)
            self.h1box.addWidget(radio)

        # Add the layouts to the main layout
        self.value=2
        self.groupbox = QGroupBox(name)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.h1box)
        self.groupbox.setLayout(self.vbox)

    def onRadioButtonClicked(self):
        radiobutton = self.sender()  # get the radio button that was clicked
        print(radiobutton.text())
        self.value=float(radiobutton.text())

    def onRadioButtonClicked1(self):
        radiobutton = self.sender()  # get the radio button that was clicked
        print(radiobutton.text())
        self.value=int(radiobutton.text())