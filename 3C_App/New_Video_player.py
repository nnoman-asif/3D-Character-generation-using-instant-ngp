from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QSlider, QPushButton,QApplication,
                             QWidget, QGraphicsScene,QGraphicsView,QGroupBox)

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        #graphics
        self._scene =QGraphicsScene(self)
        self._gv = QGraphicsView(self._scene)
        self._videoitem = QGraphicsVideoItem()
        self._scene.addItem(self._videoitem)
        self.num=90
        self._videoitem.setRotation(self.num)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.stateChanged.connect(self.on_stateChanged)
        self.mediaPlayer.setVideoOutput(self._videoitem)
        self.file=""
        #buttons
        self.playButton = QPushButton("Play")
        self.rotateButtonl = QPushButton("Rotate left")
        self.rotateButtonr = QPushButton("Rotate right")
        self.fowardButton = QPushButton()
        self.backButton = QPushButton()
        #layout and groupboxes
        self.controlLayout = QHBoxLayout()
        self.gui_layout=QVBoxLayout()
        self.groupbox=QGroupBox()
        
        #slider
        self.positionSlider = QSlider(Qt.Horizontal)#video slider
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.all_layout()
        self.buttons()
        self.sliders()

    def all_layout(self):     
        #control box
        self.controlLayout.setContentsMargins(5, 5, 5, 5)
        #self.controlLayout.addWidget(self.label2)
        self.controlLayout.addWidget(self.playButton)
        self.controlLayout.addWidget(self.backButton)
        self.controlLayout.addWidget(self.positionSlider)
        self.controlLayout.addWidget(self.fowardButton)
        self.controlLayout.addWidget(self.volumeSlider)
        self.controlLayout.addWidget(self.rotateButtonl)
        self.controlLayout.addWidget(self.rotateButtonr)

        #layout and groupbox
        self.gui_layout.addWidget(self._gv)
        #self.groupbox.setStyleSheet("QGroupBox{background-color:#1f1f1f;}")
        self.groupbox.setLayout(self.controlLayout)
        self.gui_layout.addWidget(self.groupbox)
        self.setLayout(self.gui_layout)

    def sliders(self):
        # Update position slider range and position when media player changes state
        self.mediaPlayer.durationChanged.connect(self.setDuration)
        self.mediaPlayer.positionChanged.connect(self.setPositionSlider)

        # Create slider for seeking to a specific time in the video and connect to slot
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        # Create slider for volume control and connect to slot
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(50)
        self.volumeSlider.setTickPosition(QSlider.TicksBelow)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.valueChanged.connect(self.setVolume)

    def buttons(self):
        #buttons
        self.playButton.clicked.connect(self.play)
        self.rotateButtonr.clicked.connect(self.R_button)
        self.rotateButtonl.clicked.connect(self.L_button)
        self.fowardButton.clicked.connect(self.forward)
        self.backButton.clicked.connect(self.backward)

    def play(self):
        # Handle play/pause button clicks
        self.pause_video() if self.mediaPlayer.state() == QMediaPlayer.PlayingState else self.play_video()

    def play_video(self):
        self.mediaPlayer.play()
        #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.playButton.setText('pause')

    def pause_video(self):
        self.mediaPlayer .pause()
        #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.setText('play')

    def rotateVideo(self):
        self._videoitem.setRotation(self.num)
        if self.mediaPlayer .state() == QMediaPlayer.PlayingState:
            self.pause_video()
            self._gv.fitInView(self._videoitem, Qt.KeepAspectRatio)
            self.play_video()
        else:
            self.play_video()
            self._gv.fitInView(self._videoitem, Qt.KeepAspectRatio)
            self.pause_video()
        
    def L_button(self):
        self.num-=90
        self.rotateVideo()

    def R_button(self):
        self.num+=90
        self.rotateVideo()

    @pyqtSlot(QMediaPlayer.State)
    def on_stateChanged(self, state):
        if state == QMediaPlayer.PlayingState:
            self._gv.fitInView(self._videoitem, Qt.KeepAspectRatio)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._gv.fitInView(self._videoitem, Qt.KeepAspectRatio)

    def setDuration(self, duration):# Update position slider range when duration of media player changes
        self.positionSlider.setRange(0, duration)
    
    def setPosition(self, position):# Set position of media player to slider position
        self.mediaPlayer.setPosition(position)
        
    def setPositionSlider(self, position):# Update position slider position when position of media player changes
        self.positionSlider.setValue(position)
        
    def setVolume(self, volume):# Set volume of media player to slider position
        self.mediaPlayer.setVolume(volume)

    def backward(self):
        position = self.mediaPlayer.position()
        position -= 10000
        self.mediaPlayer.setPosition(position) if position > 0 else self.mediaPlayer.setPosition(0)

    def forward(self):
        position = self.mediaPlayer.position()
        position += 10000
        self.mediaPlayer.setPosition(position) if position < self.mediaPlayer.duration() else self.mediaPlayer.setPosition(self.mediaPlayer.duration())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = VideoPlayer()
#     w.show()
#     sys.exit(app.exec_())

