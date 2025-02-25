from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys
from main_window import MainWindow


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    label_teste = QLabel("ola")

    window.v_layout.addWidget(label_teste)
    
    window.show()
    
    app.exec()