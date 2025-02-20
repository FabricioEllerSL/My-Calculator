from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)

    v_layout = QVBoxLayout()
    cw = QWidget()
    cw.setLayout(v_layout)

    label = QLabel("Um texto aleatorio")
    v_layout.addWidget(label)

    window = QMainWindow()
    window.setCentralWidget(cw)
    window.show()
    
    app.exec()