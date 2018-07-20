#coding=utf-8
"""
    author=gaokun_cug@163.com
"""


import os.path

class GetDataFromDexTxt:
    def __init__(self,dexTxtFilePath):
        if os.path.exists(dexTxtFilePath):
            self.path = dexTxtFilePath
        else :
            self.path = None
            print dexTxtFilePath , " is not exists !!!"
            return None


    def getDataFromDexFile(self):
        dexTxtFile = self.path
        hash_list = []
        filesize_list = []
        stringIdSize_list = []
        methodIdsSize_list = []
        classDefsSize_list = []
        avg_size_list = []
        max_size_list = []
        min_size_list = []
        opcode_count_list = [ ]
        permissionlist_array = []
        receiver_num_list = []
        service_num_list = []
        activity_num_list = []
        provider_num_list = []
        metadata_num_list = []

        if os.path.exists(dexTxtFile):
            filehandler = open(dexTxtFile,"r")
            while True :
                lines = filehandler.readlines(1000)
                if not lines:
                    break
                for line in  lines :
                    tmp = line.strip().split(";")
                    if len(tmp[0]) == 32  and len(tmp) == 15:
                        hash = tmp[0]
                        hash_list.append(hash)
                        filesize =tmp[1]
                        filesize_list.append(int(filesize))
                        stringIdSize = tmp[2]
                        stringIdSize_list.append(int(stringIdSize))
                        methodIdsSize = tmp[3]
                        methodIdsSize_list.append(int(methodIdsSize))
                        classDefsSize = tmp[4]
                        classDefsSize_list.append(int(classDefsSize))
                        avg_size = tmp[5]
                        avg_size_list.append(int(avg_size))
                        max_size = tmp[6]
                        max_size_list.append(int(max_size))
                        min_size = tmp[7]
                        min_size_list.append(int(min_size))
                        opcode_count = tmp[8]
                        print type(opcode_count) , opcode_count
                        opcode_count_list.append(int(opcode_count))
                        permission_list = tmp[9]
                        permissionlist_array.append(permission_list)
                        #print permission_list.split(",")
                        receiver_num = tmp[10]
                        receiver_num_list.append(int (receiver_num))
                        service_num = tmp[11]
                        service_num_list.append(int(service_num))
                        activity_num = tmp[12]
                        activity_num_list.append(int(activity_num))
                        provider_num = tmp[13]
                        provider_num_list.append(int(provider_num))
                        metadata_num = tmp[14]
                        metadata_num_list.append(int(metadata_num))
                    else :
                        print "parse dex txt error ! \n"
            filehandler.close()



        else :
            print  " dextxt is not exists !"
        return hash_list, filesize_list ,stringIdSize_list ,methodIdsSize_list , \
        classDefsSize_list ,avg_size_list ,max_size_list ,min_size_list , \
        opcode_count_list  , permissionlist_array , receiver_num_list  ,\
        service_num_list , activity_num_list ,provider_num_list , metadata_num_list



"""

if __name__ == '__main__':
    path = "/home/skyriver/DataBase/dex.txt"
    getData = GetDataFromDexTxt(path)
    getData.getDataFromDexFile()

"""
