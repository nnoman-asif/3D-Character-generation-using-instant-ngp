import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QApplication,QGroupBox,QSizePolicy
from PyQt5.QtCore import Qt,QSize

class ViewerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.folder_path = ""
        self.image_index = 0
        self.images = None

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.prev_button = QPushButton("Prev")
        self.next_button = QPushButton("Next")
        self.image_number = QPushButton()
        
        self.groupbox=QGroupBox()
        self.groupbox1=QGroupBox()

        self.init_ui()

    def init_ui(self):
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(5, 5, 5, 5)
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)
        button_layout.addWidget(self.image_number)

        layoutofImage=QHBoxLayout()
        layoutofImage.addWidget(self.image_label)

        self.groupbox.setLayout(layoutofImage)
        self.groupbox1.setLayout(button_layout)
        self.groupbox1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QVBoxLayout()
        #self.image_label.setScaledContents(True)
        layout.addWidget(self.groupbox)
        layout.addWidget(self.groupbox1)
        self.setLayout(layout)
        self.update_image()
        self.prev_button.clicked.connect(self.prev_image)
        self.next_button.clicked.connect(self.next_image)

    def get_images(self):
        return [os.path.join(self.folder_path, filename) for filename in os.listdir(self.folder_path) if filename.endswith(".jpg")]

    def update_image(self):
        if self.images:
            pixmap = QPixmap(self.images[self.image_index])
            scaled_pixmap = pixmap.scaled(self.image_label.size(), aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
            self.image_number.setText('{}/{}'.format(self.image_index + 1, len(self.images)))

    def prev_image(self):
        if self.folder_path != "":
            self.image_index -= 1
            if self.image_index < 0:
                self.image_index = len(self.images) - 1
            self.update_image()

    def next_image(self):
        if self.folder_path != "":
            self.image_index += 1
            if self.image_index >= len(self.images):
                self.image_index = 0
            self.update_image()

    def run(self,new_folder_path):
        self.folder_path = new_folder_path
        self.images = self.get_images()
        self.image_index = 0
        self.update_image()
        
    def wheelEvent(self, event):
        if self.folder_path != "":
            self.prev_image() if event.angleDelta().y() > 0 else self.next_image()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     viewer = ViewerWidget()
#     viewer.show()
#     sys.exit(app.exec_())