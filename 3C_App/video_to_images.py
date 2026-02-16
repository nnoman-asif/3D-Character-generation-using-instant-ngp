
import os
import subprocess
import sys

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import  QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox

class videoToImages(QThread):#separate process for video to images
    finished = pyqtSignal()
    def __init__(self, script_path, args):
        super().__init__()
        self.script_path = script_path
        self.args = args

    def run(self):
        self.process = subprocess.Popen([sys.executable, self.script_path, "--video_in", self.args.video_in,
                                         "--video_fps", str(self.args.video_fps), "--run_colmap",
                                         "--aabb_scale", str(self.args.aabb_scale),
                                         "--out", self.args.out, "--overwrite" if self.args.overwrite else ""])
        self.process.wait()
        self.finished.emit()
    
    def stopped(self):
        self.process.kill()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_worker)
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.cancel_worker)

        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
 
        main_layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.cancel_button, alignment=Qt.AlignCenter)

        self.setCentralWidget(central_widget)

        self.setGeometry(200, 300, 700, 700)

        self.worker = None

