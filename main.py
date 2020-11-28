from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

        self.pushButton.clicked.connect(self.ellipse)

        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def ellipse(self):
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [100, 100]
        p = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(100)
        pen.setColor(QColor(255, 255, 0))
        p.setPen(pen)
        p.drawEllipse(x, y, w, h)
        p.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
