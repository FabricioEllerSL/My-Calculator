from PySide6.QtWidgets import QLineEdit
from utils.variables import BIG_FONT_SIZE, TEXT_MAGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()
        
    def config_style(self):
        self.setStyleSheet(F"font-size: {BIG_FONT_SIZE}px")
        self.setMinimumHeight(BIG_FONT_SIZE * 1.5)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(TEXT_MAGIN, TEXT_MAGIN, TEXT_MAGIN, TEXT_MAGIN)