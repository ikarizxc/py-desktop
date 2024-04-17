from src.Competitor import Competitor
from src.FileHandler import FileHandler
from datetime import datetime

class CompetitorsController:
    competitorsList = list()
    results = dict()

    isSorted = False

    def __init__(self):
        pass

    def LoadCompetitors(self):
        jsonData = FileHandler.ReadJson()

        if jsonData != None:
            self.competitorsList = []
            for number, info in jsonData.items():
                if number.startswith('\ufeff'):
                    number = number[1:]
                competitor = Competitor(number, info["Surname"], info["Name"])
                self.competitorsList.append(competitor)

            self.isSorted = False

    
    def LoadResults(self):
        txtData = FileHandler.ReadTxt()

        if txtData != None:
            self.results = {}

            if txtData.startswith('\ufeff'):
                txtData = txtData[1:]

            start_times = {}

            txtData = txtData.split("\n")
            for line in txtData:
                parts = line.split(" ")

                if len(parts) >= 3:

                    number = parts[0]
                    action = parts[1]
                    time_str = parts[2]

                    if action == 'start':
                        start_times[number] = datetime.strptime(time_str, '%H:%M:%S,%f')
                    elif action == 'finish':
                        finish_time = datetime.strptime(time_str, '%H:%M:%S,%f')

                        start_time = start_times.get(number)
                        if start_time:
                            time_difference = finish_time - start_time
                            self.results[number] = datetime.strptime(str(time_difference), '%H:%M:%S.%f')

            self.isSorted = False

    
    def MatchCompetitorsAndResults(self):
        for i in range(len(self.competitorsList)):
            number = self.competitorsList[i].number
            if number not in self.results.keys():
                self.competitorsList[i].result = datetime.max
            else:
                self.competitorsList[i].result = self.results[number]

    def SortCompetitors(self):
        self.MatchCompetitorsAndResults()
        self.competitorsList.sort(key=lambda x: x.result)

        for i in range(len(self.competitorsList)):
            if self.competitorsList[i].result == datetime.max:
                self.competitorsList[i].position = " - "
            else:
                self.competitorsList[i].position = i + 1

        self.isSorted = True

    def SaveResults(self):
        competitorsData = {}

        for competitor in self.competitorsList:
            competitorsData[competitor.position] = {
                "Нагрудный номер": competitor.number,
                "Имя": competitor.name,
                "Фамилия": competitor.surname,
                "Результат": f"{competitor.result.minute:02}:{competitor.result.second:02},{competitor.result.microsecond:06}"
            }

        FileHandler.WriteJson(competitorsData)

    def IsCompetitorsAreLoaded(self):
        if len(self.competitorsList) > 0:
            return True
        else:
            return False

    def IsResultsAreLoaded(self):
        if len(self.results) > 0:
            return True
        else:
            return False
    
    def IsDataIsSorted(self) -> bool:
        return self.isSorted