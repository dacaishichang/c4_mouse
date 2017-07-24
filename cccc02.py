import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

head=["id","move","target","label"]
train=pd.read_table(r"F:\桌面的东西\赛事数据\腾讯cccc\dsjtzs_txfz_training.txt",sep=" ",names=head)

train.move=train.move.str.replace(';',',')
train.move=train.move.str.split(',')
train.target=train.target.str.split(',')


print("count")
for i,j in enumerate(train.move):
    j.pop()
count=[]
for i in train.move:
    j=len(i)/3
    count.append(j)
train["counts"]=count #次数

time_one=[]
for i in train.move:
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
        i.append(1)
        

print("time max")  ######
time_max=[]#时间间隔max
for i in time_int1:
    a=pd.Series(i)
    a=a.max()
    time_max.append(a)
train["ti_max"]=time_max    

print("time min") 
time_min=[]#min
for i in time_int1:
    a=pd.Series(i)
    a=a.min()
    time_min.append(a)
train["ti_min"]=time_min  
  
print("time间隔max+index+众数+中位数++") 

time_ra_max=[]#ra max
time_ra_max_ind=[]
time_ra_median=[]
time_ra_skew=[]
for i in time_cha1:
    a=pd.Series(i).astype(float)
    b=a.max()
    c=a.idxmax()
    d=a.median()
    e=a.skew()
    time_ra_max.append(b)
    time_ra_max_ind.append(c)
    time_ra_median.append(d)
    time_ra_skew.append(e)
train["time_ra_max"]=time_ra_max
train["time_ra_max_ind"]=time_ra_max_ind############################################11
train["time_ra_median"]=time_ra_median#############################################
train["time_ra_skew"]=time_ra_skew
train["time_ra_skew"]=train["time_ra_skew"].fillna(0)

print("time间隔min+index++") 

time_ra_min=[]#ra min
time_ra_min_ind=[]#ra min
time_ra_median=[]

for i in time_cha1:
    a=pd.Series(i)
    b=a.min()
    c=a.idxmin()
    d=a.median()
    time_ra_min.append(b)
    time_ra_min_ind.append(c)
    time_ra_median.append(d)

train["time_ra_min"]=time_ra_min
train["time_ra_min_ind"]=time_ra_min_ind###########################################111
train["time_ra_median"]=time_ra_median



print("time chuo max") ######
time_chuo_max=[]
for i in time_int1:
    a=pd.Series(i)
    a=a.max()
    time_chuo_max.append(a)
train["time_chuo_max"] =time_chuo_max
   
print("time chuo min")######
time_chuo_min=[]
for i in time_int1:
    a=pd.Series(i)
    a=a.min()
    time_chuo_min.append(a)
train["time_chuo_min"] =time_chuo_min

print("时间max-min")######
timemax_min=[]
for i in time_int1:
    a=pd.Series(i)
    a=a.max()-a.min()
    timemax_min.append(a)
    
train["timemax_min"] =timemax_min

print("time_mean")######
time_mean=[]
for i in time_cha1:
    a=pd.Series(i)
    a=a.mean()
    time_mean.append(a)
 
train["time_mean"] =time_mean
print("time_std")
time_std=[]
for i in time_cha1:
    a=pd.Series(i)
    a=a.std()##########注意这里【0】的std为nan
    time_std.append(a)

train["time_std"] =time_std
train["time_std"] =train["time_std"].fillna(0)

###############################3333333333333333time
print("距离开始")

dist_one=[]#距离12
for i in train.move:
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
print("x最大点+ind++")
dist_xmax=[]
dist_xmax_ind=[]
dist_xmax_med=[]
dist_xmax_skew=[]
for i in dist_x:
    a=pd.Series(i)
    b=a.max()
    c=a.idxmax()
    d=a.median()
    e=a.skew()
    dist_xmax.append(b)
    dist_xmax_ind.append(c)
    dist_xmax_med.append(d)
    dist_xmax_skew.append(e)
train["dist_xmax"]=dist_xmax
train["dist_xmax_ind"]=dist_xmax_ind#####################################
train["dist_xmax_med"]=dist_xmax_med#########################333333##########
train["dist_xmax_skew"]=dist_xmax_skew
train["dist_xmax_skew"]=train["dist_xmax_skew"].fillna(0)



print("y最大点+ind++")
dist_ymax=[]
dist_ymax_ind=[]
dist_ymax_med=[]

for i in dist_y:
    a=pd.Series(i)
    b=a.max()
    c=a.idxmax()
    d=a.median()  
    dist_ymax.append(b)
    dist_ymax_ind.append(c)
    dist_ymax_med.append(d)
    
train["dist_ymax"]=dist_ymax
train["dist_ymax_ind"]=dist_ymax_ind
train["dist_ymax_med"]=dist_ymax_med###################################################

print("x_mean")
x_mean=[]
for i in dist_x:
    a=pd.Series(i)
    a=a.mean()
    x_mean.append(a)
    
train["x_mean"]=x_mean

print("y_mean")####
y_mean=[]
for i in dist_y:
    a=pd.Series(i)
    a=a.mean()
    y_mean.append(a)
    
train["y_mean"]=y_mean 


print("x_cha_max++")####
x_cha_max=[]
x_cha_max_ind=[]
x_cha_max_med=[]
x_cha_skew=[]
for i in dist_xx:
    a=pd.Series(i)
    b=a.max()
    c=a.idxmax()
    d=a.median()
    e=a.skew()
    x_cha_max.append(b)
    x_cha_max_ind.append(c)
    x_cha_max_med.append(d)
    x_cha_skew.append(e)
    
train["x_cha_max"]=x_cha_max
train["x_cha_max_ind"]=x_cha_max_ind#######################################
train["x_cha_max_med"]=x_cha_max_med########################################33######
train["x_cha_skew"]=x_cha_skew
train["x_cha_skew"]=train["x_cha_skew"].fillna(0)




    
print("x_cha_min++")####
x_cha_min=[]
x_cha_min_ind=[]
#x_cha_min_ind=[]
for i in dist_xx:
    a=pd.Series(i)
    b=a.min()
    c=a.idxmin()
    x_cha_min_ind.append(c)
#    d=a.median()
    x_cha_min.append(b)
    
train["x_cha_min"]=x_cha_min
train["x_cha_min_ind"]=x_cha_min_ind########################################33
#     
#
print("y_cha_max++")####
y_cha_max=[]
y_cha_max_ind=[]
y_cha_max_med=[]
y_cha_skew=[]
for i in dist_yx:
    a=pd.Series(i)
    b=a.max()
    c=a.idxmax()
    d=a.median()
    e=a.skew()
    y_cha_max.append(b)
    y_cha_max_ind.append(c)
    y_cha_max_med.append(d)
    y_cha_skew.append(e)
train["y_cha_max"]=y_cha_max
train["y_cha_max_ind"]=y_cha_max_ind#########################################
train["y_cha_max_med"]=y_cha_max_med#######################################111
train["y_cha_skew"]=y_cha_skew
train["y_cha_skew"]=train["y_cha_skew"].fillna(0)




print("y_cha_min")####
y_cha_min=[]
y_cha_min_ind=[]
for i in dist_yx:
    a=pd.Series(i)
    b=a.min()
    c=a.idxmin()
    y_cha_min.append(b)
    y_cha_min_ind.append(c)
train["y_cha_min"]=y_cha_min
train["y_cha_min_ind"]=y_cha_min_ind######################################

print("x_cha_mean")####
x_cha_mean=[]
for i in dist_xx:
    a=pd.Series(i)
    a=a.mean()
    x_cha_mean.append(a)
    
train["x_cha_mean"]=x_cha_mean



print("y_cha_mean")####
y_cha_mean=[]
for i in dist_yx:
    a=pd.Series(i)
    a=a.mean()
    y_cha_mean.append(a)
    
train["y_cha_mean"]=y_cha_mean

print("x_range")
x_range=[]
for i in dist_xx:
    a=pd.Series(i)
    a=a.max()-a.min()
    x_range.append(a)
    
train["x_range"]=x_range

print("y_range")
y_range=[]
for i in dist_yx:
    a=pd.Series(i)
    a=a.max()-a.min()
    y_range.append(a)
    
train["y_range"]=y_range

print("mianji")
train["mianji"]=train.x_range*train.y_range

print('jvli')
train["jvli"]=train.x_range**2+train.y_range**2
train["jvli"]=train["jvli"]**0.5

print("total_juli")
total_juli=[]
juli_max=[]
juli_max_ind=[]
juli_med=[]
juli_skew=[]
for i,j in zip(dist_xx,dist_yx):
    a=pd.Series(i)
    b=pd.Series(j)
    c=a**2+b**2
    c=c**0.5
    d=c.sum()
    e=c.max()
    f=c.idxmax()
    g=c.median()
    h=c.skew()
    total_juli.append(d)
    juli_max.append(e)
    juli_max_ind.append(f)
    juli_med.append(g)
    juli_skew.append(h)
train["juli_max"]=juli_max
train["total_juli"]=total_juli
train["juli_max_ind"]=juli_max_ind
train["juli_med"]=juli_med##########################################333#########
train["juli_skew"]=juli_skew##################################################
train["juli_skew"]=train["juli_skew"].fillna(0)





print("total_x")
total_x=[]
for i in dist_xx:
    a=pd.Series(i)
    a=a.abs()
    a=a.sum()
    total_x.append(a)
    
train["total_x"]=total_x

print("total_y")
total_y=[]
for i in dist_yx:
    a=pd.Series(i)
    a=a.abs()
    a=a.sum()
    total_y.append(a)
    
train["total_y"]=total_y

##########################################################速度
print("total_v")
total_v=[]
for i,j in zip(total_juli,time_mean):
    if j==0:
        a=1
    else:
        a=i/j
    total_v.append(a)
    
train["total_v"]=total_v    

print("x_v")
x_v=[]
for i,j in zip(total_x,time_mean):
    if j==0:
        a=1
    else:
        a=i/j
    x_v.append(a)
    
train["x_v"]=x_v     
    
print("y_v")
y_v=[]
for i,j in zip(total_y,time_mean):
    if j==0:
        a=1
    else:
        a=i/j
    y_v.append(a)
    
train["y_v"]=y_v 
#
############################################################频率
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
 
train["hz_right"]=hz_right
train["hz_right"]=train["hz_right"]/train["hz_right"].max()

train["hz_left"]=hz_left  
train["hz_left"]=train["hz_left"]/train["hz_left"].max()

train["hz_stop_x"]=hz_stop_x
train["hz_stop_x"]=train["hz_stop_x"]/train["hz_stop_x"].max()  
      
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
train["hz_up"]=hz_up
train["hz_up"]=train["hz_up"]/train["hz_up"].max()  

train["hz_down"]=hz_down
train["hz_down"]=train["hz_down"]/train["hz_down"].max() 

train["hz_stop_y"]=hz_stop_y
train["hz_stop_y"]=train["hz_stop_y"]/train["hz_stop_y"].max() 


train["dianpin"]=train.counts/train.time_mean



#
#######################################################target
print("target-end-start")
targ_one=[]#mobiao
for i in train.target:
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
    
x_start=[]
y_start=[]
for i in dist_x:#######xstart
    x_start.append(i[0])
    
for i in dist_y:#######ystart
    y_start.append(i[0])
    
x_end=[]
y_end=[]
for i in dist_x:#######xend
    x_end.append(i[-1])

for i in dist_y:#######yend
    y_end.append(i[-1])

    
    
dist_st_tar_x=[]
for i,j in zip(x_start,targ_x):
    a=abs(i-j)
    dist_st_tar_x.append(a)
    
dist_st_tar_y=[]
for i,j in zip(y_start,targ_y):
    a=abs(i-j)
    dist_st_tar_y.append(a)
    
dist_st_tar=[]
for i,j in zip(dist_st_tar_x,dist_st_tar_y):
    a=i**2+j**2
    a=a**0.5
    dist_st_tar.append(a)
    
train["dist_st_tar"]=dist_st_tar  
train["dist_st_tar_x"]=dist_st_tar_x

    
dist_en_tar_x=[]
for i,j in zip(x_end,targ_x):
    a=abs(i-j)
    dist_en_tar_x.append(a)
    
dist_en_tar_y=[]
for i,j in zip(y_end,targ_y):
    a=abs(i-j)
    dist_en_tar_y.append(a)
    
dist_en_tar=[]
for i,j in zip(dist_en_tar_x,dist_en_tar_y):
    a=i**2+j**2
    a=a**0.5
    dist_en_tar.append(a)
    
train["dist_en_tar"]=dist_en_tar  
train["dist_en_tar_x"]=dist_en_tar_x
##################################################################337
#0-5,,,90-200,,,20-50,,,,
#
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
train['isback']=isback

#dist_xx_01=[]
#for i in dist_xx:
#    a=pd.Series(i)
#    b=a/7
#    
#    dist_xx_01.append()
    





label=train.label
del train['id']
del train['move']
del train['target']

#del train['label']
#
#from imblearn.over_sampling import SMOTE#oversampling
#sm = SMOTE(random_state=42)
#train_res, label_res = sm.fit_sample(train, label)
#
#train_res, label_res=pd.DataFrame(train_res),pd.DataFrame(label_res)
print("--------------------------------------------------------------------------------")
print("for test data")
##
#test=pd.read_table(r"F:\桌面的东西\赛事数据\腾讯cccc\dsjtzs_txfz_test1.txt",sep=" ",names=["id","move","target"])
#test.move=test.move.str.replace(';',',')
#test.move=test.move.str.split(',')
#test.target=test.target.str.split(',')
#
#
#
#
#print("count")
#for i,j in enumerate(test.move):
#    j.pop()
#count=[]
#for i in test.move:
#    j=len(i)/3
#    count.append(j)
#test["counts"]=count #次数
#
#time_one=[]
#for i in test.move:
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
#        i.append(1)
#        
#
#print("time max")  ######
#time_max=[]#时间间隔max
#for i in time_int1:
#    a=pd.Series(i)
#    a=a.max()
#    time_max.append(a)
#test["ti_max"]=time_max    
#
#print("time min") 
#time_min=[]#min
#for i in time_int1:
#    a=pd.Series(i)
#    a=a.min()
#    time_min.append(a)
#test["ti_min"]=time_min    
#print("time间隔max+index+众数+中位数++") 
#
#time_ra_max=[]#ra max
#time_ra_max_ind=[]
#time_ra_median=[]
#time_ra_skew=[]
#for i in time_cha1:
#    a=pd.Series(i).astype(float)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    e=a.skew()
#    time_ra_max.append(b)
#    time_ra_max_ind.append(c)
#    time_ra_median.append(d)
#    time_ra_skew.append(e)
#test["time_ra_max"]=time_ra_max
#test["time_ra_max_ind"]=time_ra_max_ind############################################11
#test["time_ra_median"]=time_ra_median#############################################
#test["time_ra_skew"]=time_ra_skew
#test["time_ra_skew"]=test["time_ra_skew"].fillna(0)
#
#
#print("time间隔min+index++") 
#
#time_ra_min=[]#ra min
#time_ra_min_ind=[]#ra min
#time_ra_median=[]
#
#for i in time_cha1:
#    a=pd.Series(i)
#    b=a.min()
#    c=a.idxmin()
#    d=a.median()
#    time_ra_min.append(b)
#    time_ra_min_ind.append(c)
#    time_ra_median.append(d)
#test["time_ra_min"]=time_ra_min
#test["time_ra_min_ind"]=time_ra_min_ind###########################################111
#test["time_ra_median"]=time_ra_median
#
#print("time chuo max") ######
#time_chuo_max=[]
#for i in time_int1:
#    a=pd.Series(i)
#    a=a.max()
#    time_chuo_max.append(a)
#test["time_chuo_max"] =time_chuo_max
#   
#print("time chuo min")######
#time_chuo_min=[]
#for i in time_int1:
#    a=pd.Series(i)
#    a=a.min()
#    time_chuo_min.append(a)
#test["time_chuo_min"] =time_chuo_min
#
#print("时间max-min")######
#timemax_min=[]
#for i in time_int1:
#    a=pd.Series(i)
#    a=a.max()-a.min()
#    timemax_min.append(a)
#    
#test["timemax_min"] =timemax_min
#
#print("time_mean")######
#time_mean=[]
#for i in time_cha1:
#    a=pd.Series(i)
#    a=a.mean()
#    time_mean.append(a)
# 
#test["time_mean"] =time_mean
#print("time_std")
#time_std=[]
#for i in time_cha1:
#    a=pd.Series(i)
#    a=a.std()##########注意这里【0】的std为nan
#    time_std.append(a)
#
#test["time_std"] =time_std
#test["time_std"] =test["time_std"].fillna(0)
#
###############################3333333333333333time
#print("距离开始")
#
#dist_one=[]#距离12
#for i in test.move:
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
#print("x最大点+ind++")
#dist_xmax=[]
#dist_xmax_ind=[]
#dist_xmax_med=[]
#dist_xmax_skew=[]
#for i in dist_x:
#    a=pd.Series(i)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    e=a.skew()
#    dist_xmax.append(b)
#    dist_xmax_ind.append(c)
#    dist_xmax_med.append(d)
#    dist_xmax_skew.append(e)
#test["dist_xmax"]=dist_xmax
#test["dist_xmax_ind"]=dist_xmax_ind#####################################
#test["dist_xmax_med"]=dist_xmax_med#########################333333##########
#test["dist_xmax_skew"]=dist_xmax_skew
#test["dist_xmax_skew"]=test["dist_xmax_skew"].fillna(0)
#
#
#print("y最大点+ind++")
#dist_ymax=[]
#dist_ymax_ind=[]
#dist_ymax_med=[]
#for i in dist_y:
#    a=pd.Series(i)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    dist_ymax.append(b)
#    dist_ymax_ind.append(c)
#    dist_ymax_med.append(d)
#test["dist_ymax"]=dist_ymax
#test["dist_ymax_ind"]=dist_ymax_ind
#test["dist_ymax_med"]=dist_ymax_med###################################################
#
#print("x_mean")
#x_mean=[]
#for i in dist_x:
#    a=pd.Series(i)
#    a=a.mean()
#    x_mean.append(a)
#    
#test["x_mean"]=x_mean
#
#print("y_mean")####
#y_mean=[]
#for i in dist_y:
#    a=pd.Series(i)
#    a=a.mean()
#    y_mean.append(a)
#    
#test["y_mean"]=y_mean 
#
#    
#print("x_cha_max++")####
#x_cha_max=[]
#x_cha_max_ind=[]
#x_cha_max_med=[]
#x_cha_skew=[]
#for i in dist_xx:
#    a=pd.Series(i)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    e=a.skew()
#    x_cha_max.append(b)
#    x_cha_max_ind.append(c)
#    x_cha_max_med.append(d)
#    x_cha_skew.append(e)
#    
#test["x_cha_max"]=x_cha_max
#test["x_cha_max_ind"]=x_cha_max_ind#######################################
#test["x_cha_max_med"]=x_cha_max_med########################################33######
#test["x_cha_skew"]=x_cha_skew
#test["x_cha_skew"]=test["x_cha_skew"].fillna(0)
#
#
#
#    
#print("x_cha_min++")####
#x_cha_min=[]
#x_cha_min_ind=[]
##x_cha_min_ind=[]
#for i in dist_xx:
#    a=pd.Series(i)
#    b=a.min()
#    c=a.idxmin()
#    x_cha_min_ind.append(c)
##    d=a.median()
#    x_cha_min.append(b)
#    
#test["x_cha_min"]=x_cha_min
#test["x_cha_min_ind"]=x_cha_min_ind########################################33
#     
#
#print("y_cha_max++")####
#y_cha_max=[]
#y_cha_max_ind=[]
#y_cha_max_med=[]
#y_cha_skew=[]
#for i in dist_yx:
#    a=pd.Series(i)
#    b=a.max()
#    c=a.idxmax()
#    d=a.median()
#    e=a.skew()
#    y_cha_max.append(b)
#    y_cha_max_ind.append(c)
#    y_cha_max_med.append(d)
#    y_cha_skew.append(e)
#test["y_cha_max"]=y_cha_max
#test["y_cha_max_ind"]=y_cha_max_ind#########################################
#test["y_cha_max_med"]=y_cha_max_med#######################################111
#test["y_cha_skew"]=y_cha_skew
#test["y_cha_skew"]=test["y_cha_skew"].fillna(0)
#
#print("y_cha_min")####
#y_cha_min=[]
#y_cha_min_ind=[]
#for i in dist_yx:
#    a=pd.Series(i)
#    b=a.min()
#    c=a.idxmin()
#    y_cha_min.append(b)
#    y_cha_min_ind.append(c)
#test["y_cha_min"]=y_cha_min
#test["y_cha_min_ind"]=y_cha_min_ind#####################
#
#print("x_cha_mean")####
#x_cha_mean=[]
#for i in dist_xx:
#    a=pd.Series(i)
#    a=a.mean()
#    x_cha_mean.append(a)
#    
#test["x_cha_mean"]=x_cha_mean
#
#
#
#print("y_cha_mean")####
#y_cha_mean=[]
#for i in dist_yx:
#    a=pd.Series(i)
#    a=a.mean()
#    y_cha_mean.append(a)
#    
#test["y_cha_mean"]=y_cha_mean
#
#print("x_range")
#x_range=[]
#for i in dist_xx:
#    a=pd.Series(i)
#    a=a.max()-a.min()
#    x_range.append(a)
#    
#test["x_range"]=x_range
#
#print("y_range")
#y_range=[]
#for i in dist_yx:
#    a=pd.Series(i)
#    a=a.max()-a.min()
#    y_range.append(a)
#    
#test["y_range"]=y_range
#
#print("mianji")
#test["mianji"]=test.x_range*test.y_range
#
#print('jvli')
#test["jvli"]=test.x_range**2+test.y_range**2
#test["jvli"]=test["jvli"]**0.5
#
#print("total_juli")
#total_juli=[]
#juli_max=[]
#juli_max_ind=[]
#juli_med=[]
#juli_skew=[]
#for i,j in zip(dist_xx,dist_yx):
#    a=pd.Series(i)
#    b=pd.Series(j)
#    c=a**2+b**2
#    c=c**0.5
#    d=c.sum()
#    e=c.max()
#    f=c.idxmax()
#    g=c.median()
#    h=c.skew()
#    total_juli.append(d)
#    juli_max.append(e)
#    juli_max_ind.append(f)
#    juli_med.append(g)
#    juli_skew.append(h)
#test["juli_max"]=juli_max
#test["total_juli"]=total_juli
#test["juli_max_ind"]=juli_max_ind
#test["juli_med"]=juli_med##########################################333#########
#test["juli_skew"]=juli_skew##################################################
#test["juli_skew"]=test["juli_skew"].fillna(0)
#
#print("total_x")
#total_x=[]
#for i in dist_xx:
#    a=pd.Series(i)
#    a=a.abs()
#    a=a.sum()
#    total_x.append(a)
#    
#test["total_x"]=total_x
#
#print("total_y")
#total_y=[]
#for i in dist_yx:
#    a=pd.Series(i)
#    a=a.abs()
#    a=a.sum()
#    total_y.append(a)
#    
#test["total_y"]=total_y
#
##########################################################速度
#print("total_v")
#total_v=[]
#for i,j in zip(total_juli,time_mean):
#    if j==0:
#        a=1
#    else:
#        a=i/j
#    total_v.append(a)
#    
#test["total_v"]=total_v    
#
#print("x_v")
#x_v=[]
#for i,j in zip(total_x,time_mean):
#    if j==0:
#        a=1
#    else:
#        a=i/j
#    x_v.append(a)
#    
#test["x_v"]=x_v     
#    
#print("y_v")
#y_v=[]
#for i,j in zip(total_y,time_mean):
#    if j==0:
#        a=1
#    else:
#        a=i/j
#    y_v.append(a)
#    
#test["y_v"]=y_v 
##
############################################################频率
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
#test["hz_right"]=hz_right
#test["hz_right"]=test["hz_right"]/test["hz_right"].max()
#
#test["hz_left"]=hz_left  
#test["hz_left"]=test["hz_left"]/test["hz_left"].max()
#
#test["hz_stop_x"]=hz_stop_x
#test["hz_stop_x"]=test["hz_stop_x"]/test["hz_stop_x"].max()  
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
#test["hz_up"]=hz_up
#test["hz_up"]=test["hz_up"]/test["hz_up"].max()  
#
#test["hz_down"]=hz_down
#test["hz_down"]=test["hz_down"]/test["hz_down"].max() 
#
#test["hz_stop_y"]=hz_stop_y
#test["hz_stop_y"]=test["hz_stop_y"]/test["hz_stop_y"].max() 
#
#
#
#
#test["dianpin"]=test.counts/test.time_mean
#test.dianpin[test.dianpin==np.inf]=1
#######################################################target
#print("target-end-start")
#targ_one=[]#mobiao
#for i in test.target:
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
#    
#x_start=[]
#y_start=[]
#for i in dist_x:#######xstart
#    x_start.append(i[0])
#    
#for i in dist_y:#######ystart
#    y_start.append(i[0])
#    
#x_end=[]
#y_end=[]
#for i in dist_x:#######xend
#    x_end.append(i[-1])
#
#for i in dist_y:#######yend
#    y_end.append(i[-1])
#
#    
#    
#dist_st_tar_x=[]
#for i,j in zip(x_start,targ_x):
#    a=abs(i-j)
#    dist_st_tar_x.append(a)
#    
#dist_st_tar_y=[]
#for i,j in zip(y_start,targ_y):
#    a=abs(i-j)
#    dist_st_tar_y.append(a)
#    
#dist_st_tar=[]
#for i,j in zip(dist_st_tar_x,dist_st_tar_y):
#    a=i**2+j**2
#    a=a**0.5
#    dist_st_tar.append(a)
#    
#test["dist_st_tar"]=dist_st_tar  
#test["dist_st_tar_x"]=dist_st_tar_x  
#
#    
#dist_en_tar_x=[]
#for i,j in zip(x_end,targ_x):
#    a=abs(i-j)
#    dist_en_tar_x.append(a)
#    
#dist_en_tar_y=[]
#for i,j in zip(y_end,targ_y):
#    a=abs(i-j)
#    dist_en_tar_y.append(a)
#    
#dist_en_tar=[]
#for i,j in zip(dist_en_tar_x,dist_en_tar_y):
#    a=i**2+j**2
#    a=a**0.5
#    dist_en_tar.append(a)
#    
#test["dist_en_tar"]=dist_en_tar  
#test["dist_en_tar_x"]=dist_en_tar_x  
#
#
#isback=[]
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
#test['isback']=isback
#
#del test['id']
#del test['move']
#del test['target']
#
#train.to_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\train.csv")
#test.to_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\test.csv")



#              metrics=['accuracy'])
#
#
#model.fit(train02,label02,nb_epoch=1000,batch_size=300)  
#
#
#predict=model.predict(test02)
    
#a=gbm3.predict(test02)
#a=pd.DataFrame(a)
##
#a['id']=range(1,100001)

##print("write")
#a.to_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\result.csv")
