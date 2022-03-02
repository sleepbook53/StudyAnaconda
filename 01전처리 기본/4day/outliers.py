#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np

def outliers_iqr3(dframe,data) :
    
    #q1, q3값 확인
    #np.percentil(): 25 %와 75% 시점의 데이터값 알려줌(return)
    q1, q3 =np.percentile(data,[25,75])
    print(q1)
    print(q3)
    
    #iqr 값 계산하기
    iqr = q3-q1
    print(iqr)
    
    #최솟값/최댓값
    upper_bound = q3 + (iqr *1.5)
    lower_bound = q1 - (iqr*1.5)
    
    #나이 데이터에서 이상치 값 조회
    df_temp =dframe[(data< lower_bound)
                             | (data > upper_bound)]
    
    print(len(df_temp))
    print(df_temp)

