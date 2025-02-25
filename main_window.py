from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon
import sys

class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent,  *args, **kwargs)

        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle("My Calculator")

        # Setting window icon
        icon =  QIcon("./assets/icon.png")
        self.setWindowIcon(icon)

    def add_widget_to_vlayout(self, widget):
        self.v_layout.addWidget(widget)

    def adjust_fixed_size(self):

        self.adjustSize()

        # Defines the fixed size for the window, based on its adjusted size
        self.setFixedSize(self.width(), self.height())


