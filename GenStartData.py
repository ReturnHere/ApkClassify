#coding=utf-8

import os.path
from GetDataFromDex import GetDataFromDexTxt
from GetDataFromSafetype import GetDataFromSafetype
from GetDataFromSandBox import GetDataFromSandBox
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report


class GenStartData:

    def __init__(self,trainDir):
        self.dirPath = trainDir

    def getStartData(self):
        dexPath = os.path.join(self.dirPath , "dex.txt")
        safetypepath = os.path.join(self.dirPath,"safetype.txt")
        sandpath = os.path.join(self.dirPath , "sandbox_behaviorlist.txt")

        column_names = ["sha1",	"fileSize" ,  "stringIdSize",   "methodIdsSize", "classDefsSize" ,  "avg_size", "max_size"  , "min_size" ,"opcode_count" ,  "permission_list", "receiver_num" ,"service_num", "activity_num", "provider_num" ,"meta-data_num"]
        data = pd.read_csv(dexPath ,sep=";", names= column_names,  header = 0 )


        columns_safe =["sha1","saft_type","family_id"]
        data_safe = pd.read_table(safetypepath, sep=";", names= columns_safe , header= 0)

        columns_behavior = ["sha1","behavior_list"]
        data_behavior = pd.read_table(sandpath, sep=";", names= columns_behavior, header= 0)
        tmpdata = pd.merge(data, data_behavior , on ="sha1",how='left')

        #realdata = pd.concat([data , data_behavior[column_names[1:-1]],data_safe[column_names[1:-1]] ],axis=1 , join_axes=[data.index])
        realdata = pd.merge(tmpdata,data_safe, on = "sha1",how='left')
        #print realdata.columns.values
        #print realdata.columns.size  #, realdata.iloc[:,0].size
        """
        realdata.drop("opcode_count",axis=1,inplace=True)
        realdata.drop("permission_list",axis=1,inplace=True)
        realdata.drop("behavior_list",axis=1,inplace=True)

        xclouns =  realdata.columns.values

        realdata = realdata.reindex(columns = xclouns)
        """
        del realdata["opcode_count"]
        del realdata["permission_list"]
        del realdata["behavior_list"]
        xclouns =  realdata.columns.values

        #realdata = realdata.reindex(columns = xclouns)

        #print  realdata[column_names[16]]
        X_train, X_test, y_train, y_test = train_test_split(realdata[xclouns[1:12]],realdata["family_id"],test_size=0.25,random_state = 33 )
        #print y_test.value_counts()
        print y_train.value_counts()
        print y_test.value_counts()
        ss = StandardScaler() #standadize data : variance = 1, mean value = 0
        X_train = ss.fit_transform(X_train)
        X_text = ss.transform(X_test)

        lr = LogisticRegression() #initialize Logistic Regression
        sgdc = SGDClassifier(max_iter=5) #initialize SGDClassifier
        lr.fit(X_train,y_train) #train
        lr_y_predict = lr.predict(X_test) #predict
        print classification_report(y_test ,lr_y_predict, target_names = ["0","1","2","3","4","5"])
        #print type(lr_y_predict)
        sgdc.fit(X_train,y_train)
        #print type(X_text)
        sgdc_y_predict = sgdc.predict(X_test)
        #print lr_y_predict
        #print sgdc_y_predict


        print "accuraacy of LR Classifier :" , lr.score(X_text, y_test)

        print "accuraacy of sgdc Classifier :" ,sgdc.score(X_text, y_test)

        """
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
        """
