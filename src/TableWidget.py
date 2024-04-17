from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt


class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(5)
        
        headers = ["Занятое место", "Нагрудный номер", "Имя", "Фамилия", "Результат"]
        self.setHorizontalHeaderLabels(headers)
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStretchLastSection(True)

        self.verticalHeader().hide()

        self.setEditTriggers(QTableWidget.NoEditTriggers)

        self.setStyleSheet(
            "QTableWidget {"
            "background-color: #D7DFDE;"
            "color: #000000;"
            "border-bottom: 1px solid #d0d0d0;"
            "border-right: 1px solid #d0d0d0;"
            "border-radius: 10px;"
            "font-size: 12px;"
            "font-weight: 600;"
            "}"
            "QTableWidget::item {"
            "border-bottom: 1px solid #d0d0d0;"
            "border-right: 1px solid #d0d0d0;"
            "}"
            "QTableWidget::item:selected {"
            "background-color: #79B3AC;"
            "}"
            "QHeaderView::section {"
            "background-color: #458980;"
            "color: #000000;"
            "border-top-left-radius: 10px;"
            "border-top-right-radius: 10px;"
            "padding: 4px;"            
            "font-size: 14px;"
            "font-weight: 600;"
            "}"
        )


    def SetCompetitors(self, data):
        self.setRowCount(len(data))
        for row, competitor in enumerate(data):
            self.setItem(row, 0, QTableWidgetItem(str(competitor.position)))
            self.setItem(row, 1, QTableWidgetItem(competitor.number))
            self.setItem(row, 2, QTableWidgetItem(competitor.name))
            self.setItem(row, 3, QTableWidgetItem(competitor.surname))
            self.setItem(row, 4, QTableWidgetItem(f"{competitor.result.minute:02}:{competitor.result.second:02},{competitor.result.microsecond:06}"))

            for col in range(5):
                self.item(row, col).setTextAlignment(Qt.AlignCenter)