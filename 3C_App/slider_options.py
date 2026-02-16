from PyQt5.QtWidgets import QSlider, QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt

class MySliderWidget(QWidget):
    def __init__(self):
        super().__init__()

        # create a slider widget
        self.my_slider = QSlider()
        self.my_label = QLabel(str(self.my_slider.value()))# create a label widget to display the value of the slider
        
        self.choice=2
        
        # apply custom CSS styles to the slider and label widgets
        self.setStyleSheet("""
            QSlider {
                background-color: white;

                border: 1px solid #a0a0a0;
                height: 30px;
                margin: 0px 10px;
            }

            QSlider::groove:horizontal {
                background-color: #0CCFFF;
                color:pink;
                height: 10px;
                margin: 10px 0;
            }

            QSlider::handle:horizontal:hover {
            background: #0CCFFF;
                }
            

            QSlider::handle:horizontal {
                background-color: #06426E;
                border: 2px solid black;
                width: 20px;
                height: 20px;
                margin: -5px -10px;
                border-radius: 10px;
            }

            QLabel {
                background-color: #f0f0f0;
                border: 1px solid #a0a0a0;
                border-radius: 5px;
                font-size: 28px;
                font-weight: bold;
                color:#06426E;
                margin: 10px;
                padding: 10px;
                min-width: 50px;
            }
        """)
        self.display()
        # connect the slider's valueChanged signal to a function to update the label text
        self.my_slider.valueChanged.connect(self.on_slider_change)

        # create a layout and add the slider and label widgets to it
        my_layout = QVBoxLayout()
        my_layout.addWidget(self.my_slider)
        my_layout.addWidget(self.my_label)

        # set the layout for the widget
        self.setLayout(my_layout)

    def display(self):
        self.my_label.setAlignment(Qt.AlignCenter)  # center the label text

        #slider settings
        self.my_slider.setOrientation(Qt.Horizontal)
        self.my_slider.setRange(1, 4)  # set the range of values to 1-4
        self.my_slider.setTickInterval(1)  # set the tick interval to 1
        self.my_slider.setTickPosition(QSlider.TicksBelow)  # show the tick marks below the slider
        self.my_slider.setSingleStep(1)  # set the step size to 1
        self.my_slider.setValue(2)
        # set the tick positions and labels
        self.my_slider.setTickPosition(QSlider.TicksBelow)
        self.my_slider.setTickInterval(1)

        
    def on_slider_change(self, value):
        # update the label text with the current slider value
        self.my_label.setText(str(value))
        self.choice=value
        self.my_label.repaint()  # force the label to repaint to show the new text


