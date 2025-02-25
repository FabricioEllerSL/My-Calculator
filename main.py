from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon

import sys
from main_window import MainWindow


if __name__ == "__main__":


    app = QApplication(sys.argv)
    icon = QIcon("./assets/icon.png")
    app.setWindowIcon(icon)

    window = MainWindow()

    label_teste = QLabel("asdasdasdsd")

    window.add_widget_to_vlayout(label_teste)

    # Adjusting the final window size
    window.adjust_fixed_size()
    
    window.show()
    
    app.exec()