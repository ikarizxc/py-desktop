from PySide6.QtWidgets import QFileDialog
import json


class FileHandler:
    @staticmethod
    def OpenFileDialog(fileType):
        fileDialog = QFileDialog()
        fileDialog.setWindowTitle("Выберите файл")
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        
        if fileType == 'txt':
            fileDialog.setNameFilter("Text files (*.txt)")
        elif fileType == 'json':
            fileDialog.setNameFilter("JSON files (*.json)")
        
        if fileDialog.exec():
            selectedFiles = fileDialog.selectedFiles()
            if selectedFiles:
                return selectedFiles[0]
        return None

    @staticmethod
    def SaveFileDialog(fileType):
        fileDialog = QFileDialog()
        fileDialog.setWindowTitle("Сохранение файла")
        fileDialog.setFileMode(QFileDialog.AnyFile)
        fileDialog.setAcceptMode(QFileDialog.AcceptSave)

        if fileType == 'txt':
            fileDialog.setNameFilter("Text files (*.txt)")
        elif fileType == 'json':
            fileDialog.setNameFilter("JSON files (*.json)")
        
        if fileDialog.exec():
            selectedFiles = fileDialog.selectedFiles()
            if selectedFiles:
                return selectedFiles[0]
        return None


    @staticmethod
    def ReadTxt():
        filePath = FileHandler.OpenFileDialog('txt')
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                return file.read()
        return None

    @staticmethod
    def ReadJson():
        filePath = FileHandler.OpenFileDialog('json')
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                return json.load(file)
        return None

    @staticmethod
    def WriteJson(data):
        filePath = FileHandler.SaveFileDialog('json')
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                jsonData = json.dumps(data, ensure_ascii=False, indent=4)
                file.write(jsonData)
                return True
        return False