import os
class StyleSheet():
    def __init__(self):

        self.file_path = os.path.abspath(__file__)
        self.dir_path = os.path.dirname(self.file_path)
        print( self.file_path)
        self.path= self.dir_path+"/icons3"
        self.path=self.path.replace('\\','/')
        print(self.path)
        self.QWidget="""
        
            QWidget {
                background-color: black;
                color: #f1f1f1;
            }

        """
        self.QSlider="""

            QSlider::groove:horizontal {
                height: 6px;
                background: #565656;
                background-color:#1f1f1f;
            }
            
            QSlider::handle:horizontal {
                width: 12px;
                height: 12px;
                background: #f1f1f1;
                border: none;
                margin: -3px 0;
            }
        
            QSlider::handle:horizontal:hover {
                background: #0CCFFF;
                }
        

            QSlider::sub-page:horizontal {
                    height: 6px;
                    background: #2196F3;
                }
        
        """

        self.QPushButton="""
                        QPushButton {
                                background: #06426E;
                                border: 0.5px solid white;
                                outline: none;
                                color: #f1f1f1;
                                padding: 6px;
                                margin: 0;
                                font-size: 16px;
                         }
                          QPushButton:hover {
                                background-color: #00cfff;
                            }
                            
                            QPushButton:pressed {
                                background-color: #00cfff;
                                padding: 8px;
                            }
                            
                            QPushButton:disabled {
                                background-color: #212121;
                                padding: 8px;
                            }
                            
        """

        self.QVideoWidget="""
            
            QVideoWidget {
            background-color: black;
            }
        
        #VideoPlayer {
            border: 2px solid #06426E;
            border-radius: 6px;
        }"""


        self.GroupBox="""
                QGroupBox{
                    background-color:#1f1f1f;
                    }"""

        self.QMenuBar= """
                QMenuBar {
                    background-color: blue;
                    color: white;
                }

                QMenuBar::item {
                    background-color: #333333;
                    padding: 5px 10px;
                    border-radius: 3px;
                }

                QMenuBar::item:selected {
                    background-color: #666666;
                }

                QMenu {
                    background-color: pink;
                    color: white;
                    border: 1px solid #555555;
                }

                QMenu::item {
                    background-color: #333333;
                    color: white;
                    padding: 5px 20px;
                }

                QMenu::item:selected {
                    background-color: #666666;
                }
                """
        

        self.QRadioButton = f"""
            QRadioButton {{
                background:None;
                color: white;
                font-size: 16px;
                font-weight: bold;
                font-family: Arial, sans-serif;
            }}
            QRadioButton::indicator {{
                width: 40px;
                height: 40px;
            }}
            QRadioButton::indicator:checked {{
                image: url('{self.path}/Untitled-14.png');
            }}
            QRadioButton::indicator:unchecked {{
                image: url('{self.path}/Untitled-13.png');
            }}
            QRadioButton::indicator:checked:disabled {{
                image: url('{self.path}/Untitled-12.png');
            }}
            QRadioButton::indicator:unchecked:disabled {{
                image: url('{self.path}/Untitled-10.png');
            }}
            QRadioButton::indicator:unchecked:pressed {{
                image: url('{self.path}/Untitled-17.png');
            }}
            QRadioButton::indicator:checked:pressed {{
                image: url('{self.path}/Untitled-18.png');
            }}
            QRadioButton::indicator:checked:focus {{
                border: none;
                outline: none;
            }}
            QRadioButton::indicator:unchecked:focus {{
                border: none;
                outline: none;
            }}
            QRadioButton::indicator:unchecked:hover {{
                image: url('{self.path}/Untitled-17.png');
            }}
            QRadioButton::indicator:checked:hover {{
                border: none;
                outline: none;
            }}
            QRadioButton::indicator:checked:disabled:hover {{
                border: none;
                outline: none;
            }}
            QRadioButton::indicator:unchecked:disabled:hover {{
                border: none;
                outline: none;
            }}
    """

#print(QRadioButton)
# QRadioButton = """
#             QRadioButton {
#                 background:None;
#                 color: white;
#                 font-size: 16px;
#                 font-weight: bold;
#                 font-family: Arial, sans-serif;
#             }
#             QRadioButton::indicator {
#                 width: 40px;
#                 height: 40px;
#             }
#             QRadioButton::indicator:checked {
#                 image: url('icons/Untitled-14.png');
#             }
#             QRadioButton::indicator:unchecked {
#                 image: url('icons/Untitled-13.png');
#             }
#             QRadioButton::indicator:checked:disabled {
#                 image: url('icons/Untitled-12.png');
#             }
#             QRadioButton::indicator:unchecked:disabled {
#                 image: url('icons/Untitled-10.png');
#             }
#             QRadioButton::indicator:unchecked:pressed {
#                 image: url('icons/Untitled-17.png');
#             }
#             QRadioButton::indicator:checked:pressed {
#                 image: url('icons/Untitled-18.png');
#             }
#             QRadioButton::indicator:checked:focus {
#                 border: none;
#                 outline: none;
#             }
#             QRadioButton::indicator:unchecked:focus {
#                 border: none;
#                 outline: none;
#             }
#             QRadioButton::indicator:unchecked:hover {
#                 image: url('icons/Untitled-17.png');
#             }
#             QRadioButton::indicator:checked:hover {
#                 border: none;
#                 outline: none;
#             }
#             QRadioButton::indicator:checked:disabled:hover {
#                 border: none;
#                 outline: none;
#             }
#             QRadioButton::indicator:unchecked:disabled:hover {
#                 border: none;
#                 outline: none;
#             }
#         """
