from PyQt5.QtWidgets import  QPlainTextEdit, QVBoxLayout, QWidget,QGroupBox

class OutputWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.groupbox = QGroupBox()
        self.output_text = QPlainTextEdit()
        self.output_text.setReadOnly(True)
        layout = QVBoxLayout()
        layout.addWidget(self.output_text)
        self.groupbox.setLayout(layout)

    def write(self, text):
        cursor = self.output_text.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        self.output_text.setTextCursor(cursor)
        self.output_text.ensureCursorVisible()

