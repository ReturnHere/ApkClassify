#coding=utf-8

import tensorflow as tf
import pandas as  pd

class ClassifyApk:
    def __init__(self,vectorData , classNum):
        self.vectordata = vectorData
        self.classnum = classNum
    def classifyByKmeans(self):
        assert self.classnum <  len(self.vectordata)
        
