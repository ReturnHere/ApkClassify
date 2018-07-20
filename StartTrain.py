#coding=utf-8

from GenStartData import GenStartData
class StartTrain :
    def __init__ (self, trainDir ) :
        self.dirPath  = trainDir
    def StartByAi(self):
        temp = GenStartData(self.dirPath)
        temp.getStartData()



if __name__ == '__main__':
    path = '/home/skyriver/DataBase'
    xxx = StartTrain(path)
    xxx.StartByAi()
