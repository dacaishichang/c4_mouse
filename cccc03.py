import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#head=["id","move","target","label"]
#train=pd.read_table(r"F:\桌面的东西\赛事数据\腾讯cccc\dsjtzs_txfz_training.txt",sep=" ",names=head)
#
#train.move=train.move.str.replace(';',',')
#train.move=train.move.str.split(',')
#train.target=train.target.str.split(',')
#
#
#print("count")
#for i,j in enumerate(train.move):
#    j.pop()
#count=[]
#for i in train.move:
#    j=len(i)/3
#    count.append(j)
#train["counts"]=count #次数
#
#
#countsss=train.counts.copy()
#countsss[countsss<200]=1
#countsss[countsss>=200]=0
#train['counts_ss']=countsss
#
#
#time_one=[]
#for i in train.move:
#    time_two=[]
#    for j,k in enumerate(i):
#        if (j+1)%3==0:
#            time_two.append(k)
#    time_one.append(time_two)
#    
#time_int1=[]#时间值（int）
#for i in time_one:
#    time_int2=[int(item) for item in i]
#    time_int1.append(time_int2)
#
#    
#time_range=[]
#for i in time_int1:
#    a=i[-1]-i[0]
#    time_range.append(a)
#
#time_range_00=pd.Series(time_range)
#time_range_00=time_range_00/3
#time_range_00=time_range_00*2
#time_range_00[time_range_00==0]=1
#time_range=time_range_00.tolist()
#train['time_range']=time_range
#    
#
#
#
#time_cha1=[]#时间差值
#for i in time_int1:
#    time_cha2=[]
#    for k,j in enumerate(i):
#        if k==0:
#            if len(i)==1:
#                a=0
#        else:
#            a=i[k-1]
#            time_cha2.append(j-a)
#    time_cha1.append(time_cha2)
#
#for i in time_cha1:#优化
#    if len(i)==0:
#        i.append(3)
#        
#
#time_cha_01=[]
#for i in time_cha1:
#    a=pd.Series(i)
#    a=a/3
#    a=a*2
#    a=a.values.tolist()
#    time_cha_01.append(a)
#    
#time_cha_02=[]
#for i in time_cha_01:
#    time_cha_00000=[]
#    for j,k in enumerate(i):
#        if k==0:
#            i[j]=1
#    time_cha_02.append(i)
#time_cha_01=time_cha_02
#        
#print("time_int")
#
#time_max=[]#时间间隔max
#time_min=[]
#time_qu25=[]
#time_qu75=[]
#time_median=[]
#timemax_min=[]
#time_sum=[]
#time_mean=[]
#for i in time_int1:
#    a=pd.Series(i)
#    b=a.quantile(0.25)
#    c=a.quantile(0.75)
#    d=a.median()
#    e=a.max()
#    f=a.min()
#    g=e-f
#    h=a.sum()
#    j=a.mean()
#    time_qu25.append(b)
#    time_qu75.append(c)
#    time_median.append(d)
#    time_max.append(e)
#    time_min.append(f)
#    timemax_min.append(g)
#    time_sum.append(h)
#    time_mean.append(j)
#    
#train['time_qu25']=time_qu25
#train['time_qu75']=time_qu75
#train['time_median']=time_median
#train["ti_max"]=time_max    
#train["ti_min"]=time_min  
#train["timemax_min"] =timemax_min
#train["time_sum"] =time_sum
#train["time_mean"] =time_mean
#
#
#
#print("time_cha") 
#
#time_ra_max=[]
#time_ra_max_ind=[]
#time_ra_median=[]
#time_ra_skew=[]
#time_ra_kurt=[]
#time_ra_min=[]
#time_ra_min_ind=[]
#time_ra_max_min=[]
#time_ra_25=[]
#time_ra_75=[]
#time_ra_mean=[]
#time_std=[]
#for i in time_cha_01:
#    a=pd.Series(i).astype(float)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    e=a.skew()
#    f=a.kurt()
#    g=a.min()
#    h=a.idxmin()
#    j=b-g
#    k=a.quantile(0.25)
#    l=a.quantile(0.75)
#    m=a.mean()
#    n=a.std()
#    time_ra_max.append(b)
#    time_ra_max_ind.append(c)
#    time_ra_median.append(d)
#    time_ra_skew.append(e)
#    time_ra_kurt.append(f)
#    time_ra_min.append(g)
#    time_ra_min_ind.append(h)
#    time_ra_max_min.append(j)
#    time_ra_25.append(k)
#    time_ra_75.append(l)
#    time_ra_mean.append(m)
#    time_std.append(n)
#    
#
#train["time_ra_max"]=time_ra_max
#train["time_ra_max_ind"]=time_ra_max_ind
#train["time_ra_median"]=time_ra_median
#
#train["time_ra_skew"]=time_ra_skew
#train["time_ra_skew"]=train["time_ra_skew"].fillna(0)
#
#train["time_ra_kurt"]=time_ra_kurt
#train["time_ra_kurt"]=train["time_ra_kurt"].fillna(0)
#
#train["time_ra_min"]=time_ra_min
#train["time_ra_min_ind"]=time_ra_min_ind
#train["time_ra_max_min"]=time_ra_max_min
#train["time_ra_25"]=time_ra_25
#train["time_ra_75"]=time_ra_75
#
#train["time_ra_mean"] =time_ra_mean
#train["time_ra_mean"]=train["time_ra_mean"].replace(0,1)
#
#train["time_std"] =time_std
#train["time_std"] =train["time_std"].fillna(0)
#
###############################3333333333333333time
#print("距离开始---------------------------")
#
#dist_one=[]#距离12
#for i in train.move:
#    dist_two=[]
#    for j,k in enumerate(i):
#        if (j+1)%3==0:
#            pass
#        else:
#            dist_two.append(k)
#    dist_one.append(dist_two)
#
#dist_float1=[]
#for i in dist_one:
#    dist_float2=[float(item) for item in i]
#    dist_float1.append(dist_float2)
#
#
#dist_x=[]############x
#for i in dist_float1:
#    dist_x0=[]
#    for k,j in enumerate(i):
#        if k%2==0:
#            dist_x0.append(j)
#    dist_x.append(dist_x0)
#dist_y=[]
#for i in dist_float1:
#    dist_y0=[]
#    for k,j in enumerate(i):
#        if k%2!=0:
#            dist_y0.append(j)
#    dist_y.append(dist_y0)  
#
#dist_xx=[]#x差
#for i in dist_x:
#    dist_xx0=[]
#    for k,j in enumerate(i):
#        if k==0:
#            pass
#        else:
#            a=i[k-1]
#            dist_xx0.append(j-a)
#    dist_xx.append(dist_xx0)
#
#for i in dist_xx:    
#    if len(i)==0:
#        i.append(0)
#   
#       
#dist_xx_01=[]#############(asdadasasdsadasda)
#for i in dist_xx:
#    a=pd.Series(i)
#    a=a/7
#    a=a.values.tolist()
#    dist_xx_01.append(a)
#        
#
#dist_yx=[]#y差
#for i in dist_y:
#    dist_yx0=[]
#    for k,j in enumerate(i):
#        if k==0:
#            pass
#        else:
#            a=i[k-1]
#            dist_yx0.append(j-a)
#    dist_yx.append(dist_yx0)
#for i in dist_yx:    
#    if len(i)==0:
#        i.append(0)  
##        
#dist_yx_01=[]#############(asdadasasdsadasda)
#for i in dist_yx:
#    a=pd.Series(i)
#    a=a/13
#    a=a.values.tolist()
#    dist_yx_01.append(a)
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#print("dist_x")
#dist_xmax=[]
#dist_xmax_ind=[]
#dist_xmax_med=[]
#dist_xmax_skew=[]
#x_mean=[]
#dist_xmax_kurt=[]
#dist_x25=[]
#dist_x75=[]
#dist_x_std=[]
#
#for i in dist_x:
#    a=pd.Series(i)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    e=a.skew()
#    f=a.mean()
#    g=a.kurt()
#    h=a.quantile(0.25)
#    j=a.quantile(0.75)
#    k=a.std()
#    dist_xmax.append(b)
#    dist_xmax_ind.append(c)
#    dist_xmax_med.append(d)
#    dist_xmax_skew.append(e)
#    x_mean.append(f)
#    dist_xmax_kurt.append(g)
#    dist_x25.append(h)
#    dist_x75.append(j)
#    dist_x_std.append(k)
#train["dist_xmax"]=dist_xmax
#train["dist_xmax_ind"]=dist_xmax_ind
#train["dist_xmax_med"]=dist_xmax_med
#
#train["dist_xmax_skew"]=dist_xmax_skew
#train["dist_xmax_skew"]=train["dist_xmax_skew"].fillna(0)
#
#train["x_mean"]=x_mean
#
#train["dist_xmax_kurt"]=dist_xmax_kurt
#train["dist_xmax_kurt"]=train["dist_xmax_kurt"].fillna(0)
#
#train["dist_x25"]=dist_x25
#train["dist_x75"]=dist_x75
#
#train["dist_x_std"]=dist_x_std
#train["dist_x_std"]=train["dist_x_std"].fillna(0)
#
#
#
#print("dist_y")
#dist_ymax=[]
#dist_ymax_ind=[]
#dist_ymax_med=[]
#y_mean=[]
#dist_ymax_skew=[]
#dist_ymax_kurt=[]
#dist_y25=[]
#dist_y75=[]
#dist_y_std=[]
#
#for i in dist_y:
#    a=pd.Series(i)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()  
#    e=a.skew()
#    f=a.mean()
#    g=a.kurt()
#    h=a.quantile(0.25)
#    j=a.quantile(0.75)
#    k=a.std()
#    dist_ymax.append(b)
#    dist_ymax_ind.append(c)
#    dist_ymax_med.append(d)
#    y_mean.append(f)
#    dist_ymax_skew.append(e)
#    dist_ymax_kurt.append(g)
#    dist_y25.append(h)
#    dist_y75.append(j)
#    dist_y_std.append(k)
#    
#train["dist_ymax"]=dist_ymax
#train["dist_ymax_ind"]=dist_ymax_ind
#train["dist_ymax_med"]=dist_ymax_med
#train["y_mean"]=y_mean
#
#train["dist_ymax_skew"]=dist_ymax_skew
#train["dist_ymax_skew"]=train["dist_ymax_skew"].fillna(0)
#
#train["dist_ymax_kurt"]=dist_ymax_kurt
#train["dist_ymax_kurt"]=train["dist_ymax_kurt"].fillna(0)
#
#train["dist_y25"]=dist_y25
#train["dist_y75"]=dist_y75
#
#train["dist_y_std"]=dist_y_std
#train["dist_y_std"]=train["dist_y_std"].fillna(0)
#
#
#print("dist_xx_01")####
#x_cha_max=[]
#x_cha_max_ind=[]
#x_cha_max_med=[]
#x_cha_skew=[]
#x_cha_min=[]
#x_cha_min_ind=[]
#x_cha_kurt=[]
#x_cha_mean=[]
#x_range=[]
#x_cha_25=[]
#x_cha_75=[]
#x_cha_std=[]
#
#total_x=[]
#for i in dist_xx_01:
#    a=pd.Series(i)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    e=a.skew()
#    f=a.min()
#    g=a.idxmin()
#    h=a.kurt()
#    j=a.mean()
#    k=a.max()-a.min()
#    l=a.abs().sum()
#    m=a.quantile(0.25)
#    n=a.quantile(0.75)
#    o=a.std()
#    x_cha_max.append(b)
#    x_cha_max_ind.append(c)
#    x_cha_max_med.append(d)
#    x_cha_skew.append(e)
#    x_cha_min_ind.append(f)
#    x_cha_min.append(g)
#    x_cha_kurt.append(h)
#    x_cha_mean.append(j)
#    x_range.append(k)
#    total_x.append(l)
#    x_cha_25.append(m)
#    x_cha_75.append(n)
#    x_cha_std.append(o)
#train["x_cha_max"]=x_cha_max
#train["x_cha_max_ind"]=x_cha_max_ind
#train["x_cha_max_med"]=x_cha_max_med
#
#train["x_cha_skew"]=x_cha_skew
#train["x_cha_skew"]=train["x_cha_skew"].fillna(0)
#
#train["x_cha_min"]=x_cha_min
#train["x_cha_min_ind"]=x_cha_min_ind
#
#train["x_cha_kurt"]=x_cha_kurt
#train["x_cha_kurt"]=train["x_cha_kurt"].fillna(0)
#
#train["x_cha_mean"]=x_cha_mean
#train["x_range"]=x_range
#train["total_x"]=total_x
#train["x_cha_25"]=x_cha_25
#train["x_cha_75"]=x_cha_75
#
#train["x_cha_std"]=x_cha_std
#train["x_cha_std"]=train["x_cha_std"].fillna(0)
#
#
#
#
#print("dist_yx_01")####
#y_cha_max=[]
#y_cha_max_ind=[]
#y_cha_max_med=[]
#y_cha_skew=[]
#y_cha_kurt=[]
#y_cha_min=[]
#y_cha_min_ind=[]
#y_cha_mean=[]
#y_range=[]
#total_y=[]
#y_cha_25=[]
#y_cha_75=[]
#y_cha_std=[]
#for i in dist_yx_01:
#    a=pd.Series(i)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    e=a.skew()
#    f=a.kurt()
#    g=a.min()
#    h=a.idxmin()
#    j=a.mean()
#    k=a.max()-a.min()
#    l=a.abs().sum()
#    m=a.quantile(0.25)
#    n=a.quantile(0.75)
#    o=a.std()
#    y_cha_max.append(b)
#    y_cha_max_ind.append(c)
#    y_cha_max_med.append(d)
#    y_cha_skew.append(e)
#    y_cha_kurt.append(f)
#    y_cha_min.append(g)
#    y_cha_min_ind.append(h)
#    y_cha_mean.append(j)
#    y_range.append(k)
#    total_y.append(l)
#    y_cha_25.append(m)
#    y_cha_75.append(n)
#    y_cha_std.append(o)
#train["y_cha_max"]=y_cha_max
#train["y_cha_max_ind"]=y_cha_max_ind
#train["y_cha_max_med"]=y_cha_max_med
#train["y_cha_skew"]=y_cha_skew
#train["y_cha_skew"]=train["y_cha_skew"].fillna(0)
#
#train["y_cha_kurt"]=y_cha_kurt
#train["y_cha_kurt"]=train["y_cha_kurt"].fillna(0)
#
#train["y_cha_min"]=y_cha_min
#train["y_cha_min_ind"]=y_cha_min_ind
#train["y_cha_mean"]=y_cha_mean
#train["y_range"]=y_range
#train["total_y"]=total_y
#train["y_cha_25"]=y_cha_25
#train["y_cha_75"]=y_cha_75
#
#train["y_cha_std"]=y_cha_std
#train["y_cha_std"]=train["y_cha_std"].fillna(0)
#
#
#
#
#print("mianji")
#train["mianji"]=train.x_range*train.y_range
#print('jvli')
#train["jvli"]=train.x_range**2+train.y_range**2
#train["jvli"]=train["jvli"]**0.5
#
#print("total_juli")
#total_juli=[]
#juli_max=[]
#juli_max_ind=[]
#juli_med=[]
#juli_skew=[]
#juli_kurt=[]
#juli_std=[]
#
#for i,j in zip(dist_xx_01,dist_yx_01):
#    a=pd.Series(i)
#    b=pd.Series(j)
#    c=a**2+b**2
#    c=c**0.5
#    d=c.sum()
#    e=c.max()
#    f=c.idxmax()
#    g=c.median()
#    h=c.skew()
#    j=c.kurt()
#    k=c.std()
#    total_juli.append(d)
#    juli_max.append(e)
#    juli_max_ind.append(f)
#    juli_med.append(g)
#    juli_skew.append(h)
#    juli_kurt.append(j)
#    juli_std.append(k)
#train["juli_max"]=juli_max
#train["total_juli"]=total_juli
#train["juli_max_ind"]=juli_max_ind
#train["juli_med"]=juli_med
#train["juli_skew"]=juli_skew
#train["juli_skew"]=train["juli_skew"].fillna(0)
#
#train["juli_kurt"]=juli_kurt
#train["juli_kurt"]=train["juli_kurt"].fillna(0)
#
#train["juli_std"]=juli_std
#train["juli_std"]=train["juli_std"].fillna(0)
#
#
#
############################################################速度
#
#print("x_v")
#x_v=[]
#for i,j in zip(dist_xx_01,time_cha_01):
#    a=pd.Series(i)
#    b=pd.Series(j)
#    c=a/b
#    c=c.values.tolist()
#    x_v.append(c)
#    
#    
#    
#print("y_v")
#y_v=[]
#for i,j in zip(dist_yx_01,time_cha_01):
#    a=pd.Series(i)
#    b=pd.Series(j)
#    c=a/b
#    c=c.values.tolist()
#    y_v.append(c)
#    
#print("x_v")
#x_v_mean=[]
#x_v_std=[]
#x_v_max=[]
#x_v_min=[]
#x_v_idmax=[]
#x_v_idmin=[]
#
#for i in x_v:
#    a=pd.Series(i)
#    b=a.mean()
#    c=a.std()
#    d=a.abs().max()
#    e=a.abs().min()
#    f=a.idxmax()
#    g=a.idxmin()
#    x_v_mean.append(b)
#    x_v_std.append(c)
#    x_v_max.append(d)
#    x_v_min.append(e)
#    x_v_idmax.append(f)
#    x_v_idmin.append(g)
#train['x_v_mean']=x_v_mean
#train['x_v_std']=x_v_std
#train['x_v_std']=train['x_v_std'].fillna(0)
#train['x_v_max']=x_v_max
#train['x_v_min']=x_v_min
#train['x_v_idmax']=x_v_idmax
#train['x_v_idmin']=x_v_idmin
#
#    
#y_v_mean=[]
#y_v_std=[]
#y_v_max=[]
#y_v_min=[]
#y_v_idmax=[]
#y_v_idmin=[]
#for i in y_v:
#    a=pd.Series(i)
#    b=a.mean()
#    c=a.std()
#    d=a.abs().max()
#    e=a.abs().min()
#    f=a.idxmax()
#    g=a.idxmin()
#    y_v_mean.append(b)
#    y_v_std.append(c)
#    y_v_max.append(d)
#    y_v_min.append(e)
#    y_v_idmax.append(f)
#    y_v_idmin.append(g)
#
#train['y_v_mean']=y_v_mean
#train['y_v_std']=y_v_std
#train['y_v_std']=train['y_v_std'].fillna(0)
#train['y_v_max']=y_v_max
#train['y_v_min']=y_v_min
#train['y_v_idmax']=y_v_idmax
#train['y_v_idmin']=y_v_idmin
#
#print("total_v")
#total_v=[]
#for i,j in zip(x_v,y_v):
#    a=pd.Series(i)
#    b=pd.Series(j)
#    c=a**2+b**2
#    c=a**0.5
#    d=c.sum()
#    total_v.append(d)
#train['total_v']=total_v
#
#
##############################################################频率
#print("hz")
#hz_up=[]
#hz_down=[]
#hz_left=[]
#hz_right=[]
#hz_stop_y=[]
#hz_stop_x=[]
#for i in dist_xx:
#    hz1=0
#    hz2=0
#    hzt=0
#    for j in i:
#        if j>0:
#            hz1=hz1+1
#        elif j<0:
#            hz2=hz2+1
#        else:
#            hzt=hzt+1
#    hz_right.append(hz1)
#    hz_left.append(hz2)
#    hz_stop_x.append(hzt)
# 
#train["hz_right"]=hz_right
#train["hz_right"]=train["hz_right"]/train["hz_right"].max()
#
#train["hz_left"]=hz_left  
#train["hz_left"]=train["hz_left"]/train["hz_left"].max()
#
#train["hz_stop_x"]=hz_stop_x
#train["hz_stop_x"]=train["hz_stop_x"]/train["hz_stop_x"].max()  
#      
#for i in dist_yx:
#    hz1=0
#    hz2=0
#    hzt=0
#    for j in i:
#        if j>0:
#            hz1=hz1+1
#        elif j<0:
#            hz2=hz2+1
#        else :
#            hzt=hzt+1
#    hz_up.append(hz1)
#    hz_down.append(hz2)
#    hz_stop_y.append(hzt)
#train["hz_up"]=hz_up
#train["hz_up"]=train["hz_up"]/train["hz_up"].max()  
#
#train["hz_down"]=hz_down
#train["hz_down"]=train["hz_down"]/train["hz_down"].max() 
#
#train["hz_stop_y"]=hz_stop_y
#train["hz_stop_y"]=train["hz_stop_y"]/train["hz_stop_y"].max() 
#
#
#train["dianpin"]=train.counts/train.time_range
#
#
#
###
##########################################################target
#print("target-end-start")
#targ_one=[]#mobiao
#for i in train.target:
#    targ_two=[]
#    for k in i:
#        targ_two.append(k)
#    targ_one.append(targ_two)
#
#targ_float1=[]
#for i in targ_one:
#    targ_float2=[float(item) for item in i]
#    targ_float1.append(targ_float2)
#    
#targ_x=[]
#targ_y=[]
#for i in targ_float1:#######targ
#    targ_x.append(i[0])
#    targ_y.append(i[1])
##    
#train['targ_x']=targ_x
#train['targ_y']=targ_y
#
#
#
#x_start=[]
#y_start=[]
#for i in dist_x:#######xstart
#    x_start.append(i[0])
#    
#for i in dist_y:#######ystart
#    y_start.append(i[0])
##    
#train['x_start']=x_start
#train['y_start']=y_start
#
#x_end=[]
#y_end=[]
#for i in dist_x:#######xend
#    x_end.append(i[-1])
#
#for i in dist_y:#######yend
#    y_end.append(i[-1])
#
#dist_en_tar_x=[]
#a=pd.Series(x_end)
#b=pd.Series(targ_x)
#c=a-b
#c=c.abs()
#dist_en_tar_x=c.values.tolist()
#train['dist_en_tar_x']=dist_en_tar_x
#
#
####################################################################337
###0-5,,,90-200,,,20-50,,,,
###
###
#
##
#isback=[]
#
#for i in dist_xx:
#    a=pd.Series(i)
#    b=a[a<=0]
#    if b.size<=5:
#        isback.append(0)
#    elif b.size>90 and b.size<180:
#        isback.append(0)
#    elif b.size>20 and b.size<50:
#        isback.append(0)
#    else:
#        isback.append(1)
#train['isback']=isback
#
#
#back_x=[]
#for i in dist_xx:
#    a=pd.Series(i)
#    b=a[a<=0]
#    c=len(b.values)
#    back_x.append(c)
#    
#train['back_x']=back_x
#label=train.label
#del train['id']
#del train['move']
#del train['target']
#
#
#
#train.to_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\train.csv")
#
#print("--------------------------------------------------------------------------------")
#print("for test data")
###
##
#
#
#
#
#
#
#
#
#












#
#




test=pd.read_table(r"F:\桌面的东西\赛事数据\腾讯cccc\dsjtzs_txfz_test1.txt",sep=" ",names=["id","move","target"])
test.move=test.move.str.replace(';',',')
test.move=test.move.str.split(',')
test.target=test.target.str.split(',')
#
#
#
#
print("count")
for i,j in enumerate(test.move):
    j.pop()
count=[]
for i in test.move:
    j=len(i)/3
    count.append(j)
test["counts"]=count #次数

countsss=test.counts.copy()
countsss[countsss<200]=1
countsss[countsss>=200]=0
test['counts_ss']=countsss


time_one=[]

for i in test.move:
    time_two=[]
    for j,k in enumerate(i):
        if (j+1)%3==0:
            time_two.append(k)
    time_one.append(time_two)
    
time_int1=[]#时间值（int）
for i in time_one:
    time_int2=[int(item) for item in i]
    time_int1.append(time_int2)

time_cha1=[]#时间差值
for i in time_int1:
    time_cha2=[]
    for k,j in enumerate(i):
        if k==0:
            if len(i)==1:
                a=0
        else:
            a=i[k-1]
            time_cha2.append(j-a)
    time_cha1.append(time_cha2)

for i in time_cha1:#优化
    if len(i)==0:
        i.append(3)
        

time_range=[]#+++++++++++++++++++++++++++++++=======================909
for i in time_int1:
    a=i[-1]-i[0]
    time_range.append(a)

time_range_00=pd.Series(time_range)
time_range_00=time_range_00/3
time_range_00=time_range_00*2
time_range_00[time_range_00==0]=1
time_range=time_range_00.tolist()
test['time_range']=time_range


time_cha_01=[]####(asdadasdadadadasd)
for i in time_cha1:
    a=pd.Series(i)
    a=a/3
    a=a*2
    a=a.values.tolist()
    time_cha_01.append(a)

time_cha_02=[]
for i in time_cha_01:
    time_cha_00000=[]
    for j,k in enumerate(i):
        if k==0:
            i[j]=1
    time_cha_02.append(i)
time_cha_01=time_cha_02

        
print("time_int")


time_max=[]#时间间隔max
time_min=[]
time_qu25=[]
time_qu75=[]
time_median=[]
timemax_min=[]
time_sum=[]
time_mean=[]
for i in time_int1:
    a=pd.Series(i)
    b=a.quantile(0.25)
    c=a.quantile(0.75)
    d=a.median()
    e=a.max()
    f=a.min()
    g=e-f
    h=a.sum()
    j=a.mean()
    time_qu25.append(b)
    time_qu75.append(c)
    time_median.append(d)
    time_max.append(e)
    time_min.append(f)
    timemax_min.append(g)
    time_sum.append(h)
    time_mean.append(j)
    
test['time_qu25']=time_qu25
test['time_qu75']=time_qu75
test['time_median']=time_median
test["ti_max"]=time_max    
test["ti_min"]=time_min  
test["timemax_min"] =timemax_min
test["time_sum"] =time_sum
test["time_mean"] =time_mean



print("time_cha") 

time_ra_max=[]
time_ra_max_ind=[]
time_ra_median=[]
time_ra_skew=[]
time_ra_kurt=[]
time_ra_min=[]
time_ra_min_ind=[]
time_ra_max_min=[]
time_ra_25=[]
time_ra_75=[]
time_ra_mean=[]
time_std=[]
for i in time_cha_01:
    a=pd.Series(i).astype(float)
    b=a.max()
    c=a.idxmax()
    d=a.median()
    e=a.skew()
    f=a.kurt()
    g=a.min()
    h=a.idxmin()
    j=b-g
    k=a.quantile(0.25)
    l=a.quantile(0.75)
    m=a.mean()
    n=a.std()
    time_ra_max.append(b)
    time_ra_max_ind.append(c)
    time_ra_median.append(d)
    time_ra_skew.append(e)
    time_ra_kurt.append(f)
    time_ra_min.append(g)
    time_ra_min_ind.append(h)
    time_ra_max_min.append(j)
    time_ra_25.append(k)
    time_ra_75.append(l)
    time_ra_mean.append(m)
    time_std.append(n)
    

test["time_ra_max"]=time_ra_max
test["time_ra_max_ind"]=time_ra_max_ind
test["time_ra_median"]=time_ra_median

test["time_ra_skew"]=time_ra_skew
test["time_ra_skew"]=test["time_ra_skew"].fillna(0)

test["time_ra_kurt"]=time_ra_kurt
test["time_ra_kurt"]=test["time_ra_kurt"].fillna(0)

test["time_ra_min"]=time_ra_min
test["time_ra_min_ind"]=time_ra_min_ind
test["time_ra_max_min"]=time_ra_max_min
test["time_ra_25"]=time_ra_25
test["time_ra_75"]=time_ra_75

test["time_ra_mean"] =time_ra_mean
test["time_ra_mean"]=test["time_ra_mean"].replace(0,1)

test["time_std"] =time_std
test["time_std"] =test["time_std"].fillna(0)

##############################3333333333333333time
print("距离开始---------------------------")

dist_one=[]#距离12
for i in test.move:
    dist_two=[]
    for j,k in enumerate(i):
        if (j+1)%3==0:
            pass
        else:
            dist_two.append(k)
    dist_one.append(dist_two)

dist_float1=[]
for i in dist_one:
    dist_float2=[float(item) for item in i]
    dist_float1.append(dist_float2)


dist_x=[]############x
for i in dist_float1:
    dist_x0=[]
    for k,j in enumerate(i):
        if k%2==0:
            dist_x0.append(j)
    dist_x.append(dist_x0)
dist_y=[]
for i in dist_float1:
    dist_y0=[]
    for k,j in enumerate(i):
        if k%2!=0:
            dist_y0.append(j)
    dist_y.append(dist_y0)  

dist_xx=[]#x差
for i in dist_x:
    dist_xx0=[]
    for k,j in enumerate(i):
        if k==0:
            pass
        else:
            a=i[k-1]
            dist_xx0.append(j-a)
    dist_xx.append(dist_xx0)

for i in dist_xx:    
    if len(i)==0:
        i.append(0)
   
       
dist_xx_01=[]#############(asdadasasdsadasda)
for i in dist_xx:
    a=pd.Series(i)
    a=a/7
    a=a.values.tolist()
    dist_xx_01.append(a)
        

dist_yx=[]#y差
for i in dist_y:
    dist_yx0=[]
    for k,j in enumerate(i):
        if k==0:
            pass
        else:
            a=i[k-1]
            dist_yx0.append(j-a)
    dist_yx.append(dist_yx0)
for i in dist_yx:    
    if len(i)==0:
        i.append(0)  
#        
dist_yx_01=[]#############(asdadasasdsadasda)
for i in dist_yx:
    a=pd.Series(i)
    a=a/13
    a=a.values.tolist()
    dist_yx_01.append(a)
    
    
    
    
    
    
    
    
    
    
    
print("dist_x")
dist_xmax=[]
dist_xmax_ind=[]
dist_xmax_med=[]
dist_xmax_skew=[]
x_mean=[]
dist_xmax_kurt=[]
dist_x25=[]
dist_x75=[]
dist_x_std=[]
for i in dist_x:
    a=pd.Series(i)
    b=a.max()
    c=a.idxmax()
    d=a.median()
    e=a.skew()
    f=a.mean()
    g=a.kurt()
    h=a.quantile(0.25)
    j=a.quantile(0.75)
    k=a.std()
    dist_xmax.append(b)
    dist_xmax_ind.append(c)
    dist_xmax_med.append(d)
    dist_xmax_skew.append(e)
    x_mean.append(f)
    dist_xmax_kurt.append(g)
    dist_x25.append(h)
    dist_x75.append(j)
    dist_x_std.append(k)
test["dist_xmax"]=dist_xmax
test["dist_xmax_ind"]=dist_xmax_ind
test["dist_xmax_med"]=dist_xmax_med

test["dist_xmax_skew"]=dist_xmax_skew
test["dist_xmax_skew"]=test["dist_xmax_skew"].fillna(0)

test["x_mean"]=x_mean

test["dist_xmax_kurt"]=dist_xmax_kurt
test["dist_xmax_kurt"]=test["dist_xmax_kurt"].fillna(0)

test["dist_x25"]=dist_x25
test["dist_x75"]=dist_x75

test["dist_x_std"]=dist_x_std
test["dist_x_std"]=test["dist_x_std"].fillna(0)

print("dist_y")
dist_ymax=[]
dist_ymax_ind=[]
dist_ymax_med=[]
y_mean=[]
dist_ymax_skew=[]
dist_ymax_kurt=[]
dist_y25=[]
dist_y75=[]
dist_y_std=[]
for i in dist_y:
    a=pd.Series(i)
    b=a.max()
    c=a.idxmax()
    d=a.median()  
    e=a.skew()
    f=a.mean()
    g=a.kurt()
    h=a.quantile(0.25)
    j=a.quantile(0.75)
    k=a.std()
    dist_ymax.append(b)
    dist_ymax_ind.append(c)
    dist_ymax_med.append(d)
    y_mean.append(f)
    dist_ymax_skew.append(e)
    dist_ymax_kurt.append(g)
    dist_y25.append(h)
    dist_y75.append(j)
    dist_y_std.append(k)
test["dist_ymax"]=dist_ymax
test["dist_ymax_ind"]=dist_ymax_ind
test["dist_ymax_med"]=dist_ymax_med
test["y_mean"]=y_mean

test["dist_ymax_skew"]=dist_ymax_skew
test["dist_ymax_skew"]=test["dist_ymax_skew"].fillna(0)

test["dist_ymax_kurt"]=dist_ymax_kurt
test["dist_ymax_kurt"]=test["dist_ymax_kurt"].fillna(0)

test["dist_y25"]=dist_y25
test["dist_y75"]=dist_y75

test["dist_y_std"]=dist_y_std
test["dist_y_std"]=test["dist_y_std"].fillna(0)

print("dist_xx_01")####
x_cha_max=[]
x_cha_max_ind=[]
x_cha_max_med=[]
x_cha_skew=[]
x_cha_min=[]
x_cha_min_ind=[]
x_cha_kurt=[]
x_cha_mean=[]
x_range=[]
x_cha_25=[]
x_cha_75=[]
x_cha_std=[]

total_x=[]
for i in dist_xx_01:
    a=pd.Series(i)
    b=a.max()
    c=a.idxmax()
    d=a.median()
    e=a.skew()
    f=a.min()
    g=a.idxmin()
    h=a.kurt()
    j=a.mean()
    k=a.max()-a.min()
    l=a.abs().sum()
    m=a.quantile(0.25)
    n=a.quantile(0.75)
    o=a.std()
    x_cha_max.append(b)
    x_cha_max_ind.append(c)
    x_cha_max_med.append(d)
    x_cha_skew.append(e)
    x_cha_min_ind.append(f)
    x_cha_min.append(g)
    x_cha_kurt.append(h)
    x_cha_mean.append(j)
    x_range.append(k)
    total_x.append(l)
    x_cha_25.append(m)
    x_cha_75.append(n)
    x_cha_std.append(o)
test["x_cha_max"]=x_cha_max
test["x_cha_max_ind"]=x_cha_max_ind
test["x_cha_max_med"]=x_cha_max_med

test["x_cha_skew"]=x_cha_skew
test["x_cha_skew"]=test["x_cha_skew"].fillna(0)

test["x_cha_min"]=x_cha_min
test["x_cha_min_ind"]=x_cha_min_ind

test["x_cha_kurt"]=x_cha_kurt
test["x_cha_kurt"]=test["x_cha_kurt"].fillna(0)

test["x_cha_mean"]=x_cha_mean
test["x_range"]=x_range
test["total_x"]=total_x
test["x_cha_25"]=x_cha_25
test["x_cha_75"]=x_cha_75

test["x_cha_std"]=x_cha_std
test["x_cha_std"]=test["x_cha_std"].fillna(0)




print("dist_yx_01")####
y_cha_max=[]
y_cha_max_ind=[]
y_cha_max_med=[]
y_cha_skew=[]
y_cha_kurt=[]
y_cha_min=[]
y_cha_min_ind=[]
y_cha_mean=[]
y_range=[]
total_y=[]
y_cha_25=[]
y_cha_75=[]
y_cha_std=[]

for i in dist_yx_01:
    a=pd.Series(i)
    b=a.max()
    c=a.idxmax()
    d=a.median()
    e=a.skew()
    f=a.kurt()
    g=a.min()
    h=a.idxmin()
    j=a.mean()
    k=a.max()-a.min()
    l=a.abs().sum()
    m=a.quantile(0.25)
    n=a.quantile(0.75)
    o=a.std()
    y_cha_max.append(b)
    y_cha_max_ind.append(c)
    y_cha_max_med.append(d)
    y_cha_skew.append(e)
    y_cha_kurt.append(f)
    y_cha_min.append(g)
    y_cha_min_ind.append(h)
    y_cha_mean.append(j)
    y_range.append(k)
    total_y.append(l)
    y_cha_25.append(m)
    y_cha_75.append(n)
    y_cha_std.append(o)
test["y_cha_max"]=y_cha_max
test["y_cha_max_ind"]=y_cha_max_ind
test["y_cha_max_med"]=y_cha_max_med
test["y_cha_skew"]=y_cha_skew
test["y_cha_skew"]=test["y_cha_skew"].fillna(0)

test["y_cha_kurt"]=y_cha_kurt
test["y_cha_kurt"]=test["y_cha_kurt"].fillna(0)

test["y_cha_min"]=y_cha_min
test["y_cha_min_ind"]=y_cha_min_ind
test["y_cha_mean"]=y_cha_mean
test["y_range"]=y_range
test["total_y"]=total_y
test["y_cha_25"]=y_cha_25
test["y_cha_75"]=y_cha_75

test["y_cha_std"]=y_cha_std
test["y_cha_std"]=test["y_cha_std"].fillna(0)




print("mianji")
test["mianji"]=test.x_range*test.y_range
print('jvli')
test["jvli"]=test.x_range**2+test.y_range**2
test["jvli"]=test["jvli"]**0.5

print("total_juli")
total_juli=[]
juli_max=[]
juli_max_ind=[]
juli_med=[]
juli_skew=[]
juli_kurt=[]
juli_std=[]

for i,j in zip(dist_xx_01,dist_yx_01):
    a=pd.Series(i)
    b=pd.Series(j)
    c=a**2+b**2
    c=c**0.5
    d=c.sum()
    e=c.max()
    f=c.idxmax()
    g=c.median()
    h=c.skew()
    j=c.kurt()
    k=c.std()
    total_juli.append(d)
    juli_max.append(e)
    juli_max_ind.append(f)
    juli_med.append(g)
    juli_skew.append(h)
    juli_kurt.append(j)
    juli_std.append(k)
test["juli_max"]=juli_max
test["total_juli"]=total_juli
test["juli_max_ind"]=juli_max_ind
test["juli_med"]=juli_med
test["juli_skew"]=juli_skew
test["juli_skew"]=test["juli_skew"].fillna(0)

test["juli_kurt"]=juli_kurt
test["juli_kurt"]=test["juli_kurt"].fillna(0)

test["juli_std"]=juli_std
test["juli_std"]=test["juli_std"].fillna(0)

###########################################################速度

print("x_v")
x_v=[]
for i,j in zip(dist_xx_01,time_cha_01):
    a=pd.Series(i)
    b=pd.Series(j)
    c=a/b
    c=c.values.tolist()
    x_v.append(c)
    
    
    
print("y_v")
y_v=[]
for i,j in zip(dist_yx_01,time_cha_01):
    a=pd.Series(i)
    b=pd.Series(j)
    c=a/b
    c=c.values.tolist()
    y_v.append(c)
    
print("x_v")
x_v_mean=[]
x_v_std=[]
x_v_max=[]
x_v_min=[]
x_v_idmax=[]
x_v_idmin=[]

for i in x_v:
    a=pd.Series(i)
    b=a.mean()
    c=a.std()
    d=a.abs().max()
    e=a.abs().min()
    f=a.idxmax()
    g=a.idxmin()
    x_v_mean.append(b)
    x_v_std.append(c)
    x_v_max.append(d)
    x_v_min.append(e)
    x_v_idmax.append(f)
    x_v_idmin.append(g)
test['x_v_mean']=x_v_mean
test['x_v_std']=x_v_std
test['x_v_std']=test['x_v_std'].fillna(0)
test['x_v_max']=x_v_max
test['x_v_min']=x_v_min
test['x_v_idmax']=x_v_idmax
test['x_v_idmin']=x_v_idmin

    
y_v_mean=[]
y_v_std=[]
y_v_max=[]
y_v_min=[]
y_v_idmax=[]
y_v_idmin=[]
for i in y_v:
    a=pd.Series(i)
    b=a.mean()
    c=a.std()
    d=a.abs().max()
    e=a.abs().min()
    f=a.idxmax()
    g=a.idxmin()
    y_v_mean.append(b)
    y_v_std.append(c)
    y_v_max.append(d)
    y_v_min.append(e)
    y_v_idmax.append(f)
    y_v_idmin.append(g)

test['y_v_mean']=y_v_mean
test['y_v_std']=y_v_std
test['y_v_std']=test['y_v_std'].fillna(0)
test['y_v_max']=y_v_max
test['y_v_min']=y_v_min
test['y_v_idmax']=y_v_idmax
test['y_v_idmin']=y_v_idmin

print("total_v")
total_v=[]
for i,j in zip(x_v,y_v):
    a=pd.Series(i)
    b=pd.Series(j)
    c=a**2+b**2
    c=a**0.5
    d=c.sum()
    total_v.append(d)
test['total_v']=total_v


#############################################################频率
print("hz")
hz_up=[]
hz_down=[]
hz_left=[]
hz_right=[]
hz_stop_y=[]
hz_stop_x=[]
for i in dist_xx:
    hz1=0
    hz2=0
    hzt=0
    for j in i:
        if j>0:
            hz1=hz1+1
        elif j<0:
            hz2=hz2+1
        else:
            hzt=hzt+1
    hz_right.append(hz1)
    hz_left.append(hz2)
    hz_stop_x.append(hzt)
 
test["hz_right"]=hz_right
test["hz_right"]=test["hz_right"]/test["hz_right"].max()

test["hz_left"]=hz_left  
test["hz_left"]=test["hz_left"]/test["hz_left"].max()

test["hz_stop_x"]=hz_stop_x
test["hz_stop_x"]=test["hz_stop_x"]/test["hz_stop_x"].max()
      
for i in dist_yx:
    hz1=0
    hz2=0
    hzt=0
    for j in i:
        if j>0:
            hz1=hz1+1
        elif j<0:
            hz2=hz2+1
        else :
            hzt=hzt+1
    hz_up.append(hz1)
    hz_down.append(hz2)
    hz_stop_y.append(hzt)
test["hz_up"]=hz_up
test["hz_up"]=test["hz_up"]/test["hz_up"].max()  

test["hz_down"]=hz_down
test["hz_down"]=test["hz_down"]/test["hz_down"].max() 

test["hz_stop_y"]=hz_stop_y
test["hz_stop_y"]=test["hz_stop_y"]/test["hz_stop_y"].max() 


test["dianpin"]=test.counts/test.time_mean



##
#########################################################target
print("target-end-start")
targ_one=[]#mobiao
for i in test.target:
    targ_two=[]
    for k in i:
        targ_two.append(k)
    targ_one.append(targ_two)

targ_float1=[]
for i in targ_one:
    targ_float2=[float(item) for item in i]
    targ_float1.append(targ_float2)
    
targ_x=[]
targ_y=[]
for i in targ_float1:#######targ
    targ_x.append(i[0])
    targ_y.append(i[1])
#    
test['targ_x']=targ_x
test['targ_y']=targ_y



x_start=[]
y_start=[]
for i in dist_x:#######xstart
    x_start.append(i[0])
    
for i in dist_y:#######ystart
    y_start.append(i[0])
#    
test['x_start']=x_start
test['y_start']=y_start

x_end=[]
y_end=[]
for i in dist_x:#######xend
    x_end.append(i[-1])

for i in dist_y:#######yend
    y_end.append(i[-1])

dist_en_tar_x=[]
a=pd.Series(x_end)
b=pd.Series(targ_x)
c=a-b
c=c.abs()
dist_en_tar_x=c.values.tolist()
test['dist_en_tar_x']=dist_en_tar_x


###################################################################337
##0-5,,,90-200,,,20-50,,,,
##
##

#
isback=[]
for i in dist_xx:
    a=pd.Series(i)
    b=a[a<=0]
    if b.size<=5:
        isback.append(0)
    elif b.size>90 and b.size<180:
        isback.append(0)
    elif b.size>20 and b.size<50:
        isback.append(0)
    else:
        isback.append(1)
test['isback']=isback
back_x=[]
for i in dist_xx:
    a=pd.Series(i)
    b=a[a<=0]
    c=len(b.values)
    back_x.append(c)
    
test['back_x']=back_x


del test['id']
del test['move']
del test['target']
test.to_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\test.csv")