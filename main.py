# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QFrame, QSizePolicy, QPushButton,
                               QFileDialog,QMessageBox)
from PySide2.QtGui import QPixmap,QImage
class test2(QWidget):
    def __init__(self):
        super(test2, self).__init__()
        self.load_ui()
        self.setWindowTitle('Singal-Analyzer_SAILB')

        self.imageLabel = QLabel()
        self.imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setPixmap(QPixmap())

        image = QImage('/Users/leekatme/Desktop/SAILB_Signal_Analyzer/26.png')

        self.imageLabel.setPixmap(QPixmap.fromImage(image))


    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = test2()
    widget.show()
    sys.exit(app.exec_())


# from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
#                                QLabel, QFrame, QSizePolicy, QPushButton,
#                                QFileDialog,QMessageBox)
# from PySide2.QtGui import QPixmap,QImage
# import sys
#
# class MainWindow(QWidget):
#     def __init__(self,parent=None):
#         QWidget.__init__(self,parent)
#         self.setWindowTitle('Image viewer')
#
#         self.imageLabel=QLabel()
#         self.imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
#         self.imageLabel.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
#         self.imageLabel.setScaledContents(True)
#         self.imageLabel.setPixmap(QPixmap())
#
#         openButton = QPushButton("Load image")
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.imageLabel)
#         layout.addWidget(openButton)
#         self.setLayout(layout)
#
#         openButton.clicked.connect(self.open)
#         self.resize(QApplication.primaryScreen().availableSize()*2/5)
#
#     def open(self):
#         fileName, _ = QFileDialog.getOpenFileName(self,
#                             "Open Image File",".","Images (*.png *.xpm *.jpg)")
#         if fileName != "":
#             self.load(fileName)
#
#     def load(self,fileName):
#         image = QImage(fileName)
#         if image.isNull():
#             QMessageBox.information(self,QApplication.applicationName(),
#                                     "Cannot load "+fileName)
#             self.setWindowTitle("Image viewer")
#             self.setPixmap(QPixmap())
#
#         self.imageLabel.setPixmap(QPixmap.fromImage(image))
#         self.setWindowTitle(fileName)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     app.exec_()