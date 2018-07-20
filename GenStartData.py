#coding=utf-8

import os.path
from GetDataFromDex import GetDataFromDexTxt
from GetDataFromSafetype import GetDataFromSafetype
from GetDataFromSandBox import GetDataFromSandBox
#import numpy as np

class GenStartData:

    def __init__(self,trainDir):
        self.dirPath = trainDir

    def getStartData(self):
        dexPath = os.path.join(self.dirPath , "dex.txt")
        safetypepath = os.path.join(self.dirPath,"safetype.txt")
        sandpath = os.path.join(self.dirPath , "sandbox_behaviorlist.txt")
        dexTmp = GetDataFromDexTxt(dexPath)
        hash_list, filesize_list ,stringIdSize_list ,methodIdsSize_list , \
        classDefsSize_list ,avg_size_list ,max_size_list ,min_size_list , \
        opcode_count_list  , permissionlist_array , receiver_num_list  ,\
        service_num_list , activity_num_list ,provider_num_list , metadata_num_list \
        = dexTmp.getDataFromDexFile()
        safetypeTmp = GetDataFromSafetype(safetypepath)
        ismalware_list , family_list  = safetypeTmp.getDataFromFile()
        sandbox = GetDataFromSandBox(sandpath)
        behaviorlist_array = sandbox.getDataFromFile()
        print "getData Secuss !"
