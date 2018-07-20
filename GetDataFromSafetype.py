#coding=utf-8

import os.path

class GetDataFromSafetype:
    def __init__(self, safepath):
        if os.path.exists(safepath):
            self.safefilepath = safepath
        else :
            self.safefilepath = None
            print "safttype.txt is not exists ! \r\n "
            return None
    def getDataFromFile(self):
        filehandler = open(self.safefilepath,"r")
        ismalware_list = []
        family_list = []
        while True :
            error = 0
            lines = filehandler.readlines(1000)
            if not lines :
                break
            for line in lines :
                tmp = line.strip().split(";")
                if len(tmp[0]) == 32 and len(tmp) == 3 :
                    hash = tmp[0]
                    ismalware = tmp[1]
                    family = tmp[2]
                    ismalware_list.append(int(ismalware))
                    family_list.append(int(family))
                    #print "xxx  ", behaviorlist
                else :
                    error = error + 1
                    if error > 1 :
                        print tmp
                        print "parse safetyoe  file failed !"
        filehandler.close()
        return ismalware_list , family_list
"""
if __name__ == '__main__':
    path = "/home/skyriver/DataBase/safetype.txt"
    tmp = GetDataFromSafetype(path)
    tmp.getDataFromFile()
"""
