from PySide6.QtWidgets import QPushButton


class ButtonWidget(QPushButton):
    def __init__(self, text, function):
        super().__init__(text)
        self.pressed.connect(function)

        self.setStyleSheet(
            "QPushButton {"
            "background-color: #79B3AC;"
            "border: none;"
            "color: #000000;"
            "padding: 10px 24px;"
            "text-align: center;"
            "text-decoration: none;"
            "font-size: 12px;"
            "font-weight: 600;"
            "margin: 4px 2px;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {background-color: #458980;}"
            "QPushButton:pressed {background-color: #205E56;}"
        )

