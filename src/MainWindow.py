from PySide6.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from src.TableWidget import TableWidget
from src.ButtonWidget import ButtonWidget
from src.CompetitorsController import CompetitorsController
from src.MessageBox import MessageBox


class MainWindow(QMainWindow):
    competitorsController = CompetitorsController()

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(800, 500))
        self.setWindowTitle("Спортсмены")
        self.setWindowIcon(QIcon("./resources/running.png"))
        self.setLayout()

        self.setStyleSheet(
            "QMainWindow {"
            "background-color: white"
            "color: #000000;"
            "border-bottom: 1px solid #d0d0d0;"
            "border-right: 1px solid #d0d0d0;"
            "border-radius: 10px;"
            "}"
        )

    def setLayout(self):
        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.tableWidget = TableWidget()

        pageLayout.addLayout(buttonLayout)
        pageLayout.addWidget(self.tableWidget)

        # button_layout
        btn = ButtonWidget("Загрузить спортсменов", self.LoadCompetitors)
        buttonLayout.addWidget(btn)

        btn = ButtonWidget("Загрузить результаты", self.LoadResults)
        buttonLayout.addWidget(btn)

        btn = ButtonWidget("Запустить вычисления", self.Calculate)
        buttonLayout.addWidget(btn)

        btn = ButtonWidget("Сохранение результатов", self.Save)
        buttonLayout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

    def LoadCompetitors(self):
        self.competitorsController.LoadCompetitors()

    def LoadResults(self):
        self.competitorsController.LoadResults()

    def Calculate(self):
        if self.competitorsController.IsCompetitorsAreLoaded() == False:
            messageBox = MessageBox("Ошибка!", "Данные о спростменах не загружены!")
            messageBox.exec()
        elif self.competitorsController.IsResultsAreLoaded() == False:
            messageBox = MessageBox("Ошибка!", "Данные о результатах спортсменов не загружены!")
            messageBox.exec()
        else:
            self.competitorsController.SortCompetitors()
            self.tableWidget.SetCompetitors(self.competitorsController.competitorsList)

    def Save(self):
        if self.competitorsController.IsDataIsSorted() == False:
            messageBox = MessageBox("Ошибка!", "Результаты спортсменов не посчитаны!")
            messageBox.exec()
        else:
            self.competitorsController.SaveResults()