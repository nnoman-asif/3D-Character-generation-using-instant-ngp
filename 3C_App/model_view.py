import open3d as o3d
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget,QLabel,QGroupBox,QFileDialog
from PyQt5.QtGui import QIcon
from slider_options import MySliderWidget
from multiprocessing import Process

def show_mesh(mesh_path,width=880,height=880):
    mesh = o3d.io.read_triangle_mesh(mesh_path)                         
            # Create a visualization object and set the window size
    vis = o3d.visualization.Visualizer()
    vis.create_window(width=width, height=height)
            # Add the mesh to the visualizer
    vis.add_geometry(mesh)
    vis.run()
    vis.destroy_window()

class Model_Viewer(QWidget):
    def __init__(self):
        super().__init__()
        # Create a button to trigger the mesh visualization
        self.button_change=True
        self.button = QPushButton("Visualize Mesh")
          
        self.Quality_label=QLabel("Mesh Quality")
        self.Next_button= QPushButton("Next")
        
        self.p=None
        self.isObj=True
        self.path=""
        self.window_width=880
        self.window_height=880
        self.Vlayout = QVBoxLayout()
        self.main_layout=QVBoxLayout()
        self.groupbox = QGroupBox('Step meshing')
        self.slider_options=MySliderWidget()
        self.create_layout()
        
       



    def create_layout(self):
        self.button.clicked.connect(self.visualize_mesh)
        self.Next_button.clicked.connect(self.closeWindow)
        # Create a layout to add the button
        self.Vlayout.addWidget(self.slider_options)
        self.Vlayout.addWidget(self.button)
        self.Vlayout.addWidget(self.Next_button)
        
        # Create a central widget and set the layout
        self.groupbox.setLayout(self.Vlayout)
        self.main_layout.addWidget(self.groupbox)
        self.setLayout(self.main_layout)

    def visualize_mesh(self):
        if self.button_change==True:
            if self.path!="":
                self.p = Process(target=show_mesh,args=(self.path,))
                self.p.start()   
            else:
                if self.isObj==True:
                    file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Wavefront OBJ Files (*.obj)")
                    self.path=file_name
                else:
                    file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "FBX Files (*.fbx)")
                    self.path=file_name
                if self.path!="":
                    self.visualize_mesh()
        else:
            self.button_change=True
            self.button.setText("Visualize Mesh")
            self.button.setIcon(QIcon('icons3/Untitled-8.png'))
            self.p.terminate()
            
    def closeProcess(self):
        if self.p and self.p.is_alive():
            self.p.terminate()

    def closeWindow(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "json Files (*.json)")
        #self.vis.close()
        
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())