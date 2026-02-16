import os
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QPushButton

class NewProjectDialog(QDialog):#
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Project")
        self.project_name_label = QLabel("Project Name:")
        self.project_name_input = QLineEdit()
        self.project_exists_label = QLabel()
        self.save_button = QPushButton("Save")

        self.Path_Dictionary=dict()
        self.make_dictionary()

        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_project)
        self.folder_text=""
        layout = QGridLayout()
        layout.addWidget(self.project_name_label, 0, 0)
        layout.addWidget(self.project_name_input, 0, 1)
        layout.addWidget(self.project_exists_label, 2,0,1,2)
        layout.addWidget(self.save_button, 1, 0, 1, 2)
        self.setLayout(layout)
        self.project_name_input.textChanged.connect(self.check_project_name)
        #self.toolbarshow_Signal = pyqtSignal(bool)
        

    def check_project_name(self, text):
        projects_directory = "Projects"
        main_directory = os.path.join(projects_directory, text)
        self.folder_text=text
        if os.path.exists(main_directory):
            self.project_exists_label.setText(f"The project directory '{text}' already exists.")
            self.save_button.setEnabled(False)
        else:
            self.project_exists_label.setText("")
            self.save_button.setEnabled(True)

    def save_project(self):# Save the project here
        self.create_new_project(self.folder_text)
        print("Project saved!")
        self.accept()
    
    def reject(self):
        pass

    def make_dictionary(self):#dictionary for paths
        self.Path_Dictionary["json_file"]=""
        self.Path_Dictionary["original_images_folder"]=""
        self.Path_Dictionary["cartoonized_folder"]=""
        self.Path_Dictionary["background_removed"]=""
        self.Path_Dictionary["video_folder"]=""
        self.Path_Dictionary["models_folder"]=""
        self.Path_Dictionary["video_path"]=""
        self.Path_Dictionary["images_folder"]=""
        self.Path_Dictionary["point_cloud"]=""
        self.Path_Dictionary["textured_mesh"]=""
        self.Path_Dictionary["fbx_textured_mesh"]=""


    def create_new_project(self,project_name):#file tree is created
        if project_name!="":

            projects_directory = "Projects"
            main_directory = os.path.join(projects_directory, project_name)
            os.makedirs(main_directory)
            file_path = os.path.abspath(__file__)
            dir_path = os.path.dirname(file_path)

            self.Path_Dictionary["json_file"]=dir_path+'/'+os.path.join(main_directory, "json_file")
            #self.Path_Dictionary["original_images_folder"]=os.path.join(main_directory, "images_folder", "original_images_folder")
            self.Path_Dictionary["cartoonized_folder"]=dir_path+'/'+os.path.join(main_directory, "images_folder", "cartoonized_folder")
            self.Path_Dictionary["background_removed"]=dir_path+'/'+os.path.join(main_directory, "images_folder", "background_removed")
            self.Path_Dictionary["video_folder"]=dir_path+'/'+os.path.join(main_directory, "video_folder")
            self.Path_Dictionary["models_folder"]=dir_path+'/'+os.path.join(main_directory, "models_folder")
            self.Path_Dictionary["original_images_folder"]=dir_path+'/'+os.path.join(main_directory, "video_folder","images")
           
            self.Path_Dictionary["textured_mesh_png"]=self.Path_Dictionary["models_folder"]+"/textured_mesh.png"           
            self.Path_Dictionary["textured_mesh"]=self.Path_Dictionary["models_folder"]+"/textured_mesh.obj"
            self.Path_Dictionary["fbx_textured_mesh"]=self.Path_Dictionary["models_folder"]+"/textured_mesh.fbx"
           
           
            # Create the subdirectories inside the main directory
            #os.makedirs(self.Path_Dictionary["original_images_folder"])

            print(self.Path_Dictionary["json_file"])
            print(self.Path_Dictionary["original_images_folder"])
            print(self.Path_Dictionary["models_folder"])
            print(self.Path_Dictionary["background_removed"])
            print(self.Path_Dictionary["cartoonized_folder"])
            print(self.Path_Dictionary["video_folder"])
            
            os.makedirs(self.Path_Dictionary["cartoonized_folder"])
            os.makedirs(self.Path_Dictionary["background_removed"])
            os.makedirs(self.Path_Dictionary["video_folder"])
            os.makedirs(self.Path_Dictionary["models_folder"])
            os.makedirs(self.Path_Dictionary["json_file"])
            self.Path_Dictionary["json_file"]+="/transforms.json"
            
            # self.Path_Dictionary["video_path"]=""
            # self.Path_Dictionary["images_folder"]=""