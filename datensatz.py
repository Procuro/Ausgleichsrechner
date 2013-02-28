# Datensatz (Rechnung)

import datetime

class Rechnung:
    __Date = datetime.date(2000,1,1)
    __Amount = int()              #in cents
    __Description = str()
    __Comment = str()
    __City = str()

    def SetDate(self, NewDate):
        self.__Date = NewDate

    def GetDate(self):
        return self.__Date

    def SetAmount(self, NewAmount):
        self.__Amount = NewAmount

    def GetAmount(self):
        return self.__Amount

    def SetDescription(self, NewDescription):
        self.__Description = NewDescription

    def GetDescription(self):
        return self.__Description

    def SetComment(self, NewComment):
        self.__Comment = NewComment

    def GetComment(self):
        return self.__Comment

    def SetCity(self, NewCity):
        self.__City = NewCity

    def GetCity(self):
        return self.__City
