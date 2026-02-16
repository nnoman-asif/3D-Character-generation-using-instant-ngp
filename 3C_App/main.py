import sys
from PyQt5.QtWidgets import QApplication
from StyleSheets import StyleSheet
from QMainWindow_widget import MainWindow as Qmw
from size_scaler import scaler

if __name__ == '__main__':
    app = QApplication(sys.argv)#212121;
    Ss=StyleSheet()
    app.setStyleSheet(Ss.QWidget+Ss.QSlider+Ss.QPushButton+
                      Ss.QVideoWidget+Ss.GroupBox+Ss.QMenuBar #loading stylesheets
                      +Ss.QRadioButton)
    mainWidowObj=Qmw()
    mainWindow = scaler(mainWidowObj)
    mainWindow.show()
    sys.exit(app.exec_())

