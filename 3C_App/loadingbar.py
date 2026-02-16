from PyQt5.QtWidgets import QProgressBar, QApplication
from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation, QEasingCurve

class LoadingProgressBar(QProgressBar):#loading bar
    def __init__(self):
        super().__init__()
        
        self.setValue(0)
        self.setTextVisible(False)
        self.__animation = QPropertyAnimation(self, b'loading')
        self.__animation.setStartValue(self.minimum())
        self.__animation.setEndValue(self.maximum())
        self.__animation.valueChanged.connect(self.__loading)
        self.__animation.setDuration(1000)
        self.__animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.setStyleSheet('QProgressBar {background-color: #2196F3;} QProgressBar::chunk {background-color:#2196F3 ;}')
        self.__animation.start()

    def __loading(self, v):
        self.setValue(v)
        if self.__animation.currentValue() == self.__animation.endValue():
            self.__animation.setDirection(QAbstractAnimation.Backward)
            self.setInvertedAppearance(True)
            #self.__animation.start()
        elif self.__animation.currentValue() == self.__animation.startValue():
            self.__animation.setDirection(QAbstractAnimation.Forward)
            self.setInvertedAppearance(False)
            #self.__animation.start()

if __name__ == '__main__':
    app = QApplication([])
    widget = LoadingProgressBar()
    widget.show()
    app.exec_()