from django.http import HttpResponse
import pymysql
import pandas as pd
import math
def hello(request):
    conn = pymysql.connect(host='192.168.10.243', port=3306, user='root', passwd='', db='wanfu', charset='utf8')
    RList=pd.read_sql('CALL CityCount',conn)
    #print(RList.iloc[1, 0])
    #date_ = []
    text = ''
    for i in range(len(RList)):
        print(RList.iloc[i, 0])
        #date_.append(RList.iloc[i, 0])
        if i == 0:
            text = RList.iloc[i, 0]
        else:
            text = text +';'+ RList.iloc[i, 0]
    for i in range(len(RList)):
        print(RList.iloc[i, 1])
        #date_.append(RList.iloc[i, 0])
        if i == 0:
            text =text+'|'+str(math.floor(RList.iloc[i, 1]))
        else:
            text = text +';'+ str(math.floor(RList.iloc[i, 1]))
    return HttpResponse(text)


