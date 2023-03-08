from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
from qrcode import QRCode
from PIL import Image

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("MainWin.ui", self) #load window/ui file
        self.show()

        self.generateButton.clicked.connect(self.generate)

    def generate(self):
        self.url = self.link.text()
        qr = QRCode(version=3)
        qr.add_data(self.url)
        qr.make()
        qr.make_image().save(f"saved/{self.filename.text()}.png")

        img = Image.open(f"saved/{self.filename.text()}.png")
        img.show()

def main():
    app = QApplication([])

    window = Window()
    window.setWindowTitle("QR Code Generator")

    app.exec_()

if __name__ == "__main__":
    main()