#coding=utf-8

import os.path

class GetDataFromSandBox:
    def __init__(self, sanboxlogpath):
        if os.path.exists(sanboxlogpath):
            self.sandPath = sanboxlogpath
        else :
            self.sandPath = None
            print "sandBoxpath is not exists !"
            return None
    def getDataFromFile(self):
        filehandler = open(self.sandPath,"r")
        behaviorlist_array = []
        while True :
            error = 0
            lines = filehandler.readlines(1000)
            if not lines :
                break
            for line in lines :
                tmp = line.strip().split(";")
                if len(tmp[0]) == 32 and len(tmp) == 2 :
                    hash = tmp[0]
                    behaviorlist = tmp[1].split(",")
                    behaviorlist_array.append(behaviorlist)
                
                else :
                    error = error + 1
                    if error > 1 :
                        print tmp
                        print "parse sanbox log file failed !"
        filehandler.close()
        return behaviorlist_array


"""
if __name__ == '__main__':
    path = '/home/skyriver/DataBase/sandbox_behaviorlist.txt'
    tmp = GetDataFromSandBox(path)
    tmp.getDataFromFile()
"""
