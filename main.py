import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon

from display import Display
from main_window import MainWindow



if __name__ == "__main__":


    app = QApplication(sys.argv)

    window = MainWindow()

    display = Display()
    window.add_widget_to_vlayout(display)

    # Adjusting the final window size
    window.adjust_fixed_size()
    
    window.show()
    
    app.exec()