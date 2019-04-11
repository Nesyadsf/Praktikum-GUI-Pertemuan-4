![Screenshot (66)](https://user-images.githubusercontent.com/44077159/55980900-b6fc2e80-5cbf-11e9-9414-d8ebfd79b7b7.png)
from PyQt5.QtWidgets import QWidget, QLabel

class FormSederhana(QWidget):
        def __init__(self):
            super().__init__()
            self.setupUi()

        def setupUi(self):
            self.resize(500,200)
            self.move(400,400)
            self.setWindowTitle('FormSederhana')

            self.label = QLabel('Menampilkan Tulisan berupa label')
            self.label.move(100,40)
            self.label.setParent(self)
