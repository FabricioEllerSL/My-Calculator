import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon

from mod_widgets import Display, Info
from main_window import MainWindow



if __name__ == "__main__":


    app = QApplication(sys.argv)

    window = MainWindow()

    info = Info("Texto generico...")
    window.add_widget_to_vlayout(info)

    # Main Display
    display = Display()
    window.add_widget_to_vlayout(display)

    # Adjusting the final window size
    window.adjust_fixed_size()
    
    window.show()
    
    app.exec()