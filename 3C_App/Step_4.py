from PyQt5.QtWidgets import  QWidget, QPushButton, QVBoxLayout, QGroupBox

class Step_4(QWidget):
    def __init__(self):
        super().__init__()
        self.run_ngp = QPushButton('Run Instant Ngp')
        self.next = QPushButton('Next')
        self.Viewmesh = QPushButton('View mesh')
        self.group_box=QGroupBox("step 4")
        self.fbox=QVBoxLayout()
        self.layout_grid()
       
    def layout_grid(self):
        
        self.fbox.addWidget(self.run_ngp)
        
        self.fbox.addWidget(self.Viewmesh)
        self.fbox.addWidget(self.next)
        self.group_box.setLayout(self.fbox)

   
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Step_4()
#     sys.exit(app.exec_())
