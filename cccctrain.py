import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
train=pd.read_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\train.csv")
test=pd.read_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\testB.csv")
train=train.drop(['Unnamed: 0'],axis=1)
test=test.drop(['Unnamed: 0'],axis=1)
train_index=[ 'counts', 'counts_ss', 'time_range', 'time_qu25',
       'time_qu75', 'time_median', 'ti_max', 'ti_min', 'timemax_min',
       'time_sum', 'time_mean', 'time_ra_max', 'time_ra_max_ind',
       'time_ra_median', 'time_ra_skew', 'time_ra_kurt', 'time_ra_min',
       'time_ra_min_ind', 'time_ra_max_min', 'time_ra_25', 'time_ra_75',
       'time_ra_mean', 'time_std', 'dist_xmax', 'dist_xmax_ind',
       'dist_xmax_med', 'dist_xmax_skew', 'x_mean', 'dist_xmax_kurt',
       'dist_x25', 'dist_x75', 'dist_x_std', 'dist_ymax', 'dist_ymax_ind',
       'dist_ymax_med', 'y_mean', 'dist_ymax_skew', 'dist_ymax_kurt',
       'dist_y25', 'dist_y75', 'dist_y_std', 'x_cha_max', 'x_cha_max_ind',
       'x_cha_max_med', 'x_cha_skew', 'x_cha_min', 'x_cha_min_ind',
       'x_cha_kurt', 'x_cha_mean', 'x_range', 'total_x', 'x_cha_25',
       'x_cha_75', 'x_cha_std', 'y_cha_max', 'y_cha_max_ind',
       'y_cha_max_med', 'y_cha_skew', 'y_cha_kurt', 'y_cha_min',
       'y_cha_min_ind', 'y_cha_mean', 'y_range', 'total_y', 'y_cha_25',
       'y_cha_75', 'y_cha_std', 'mianji', 'jvli', 'juli_max', 'total_juli',
       'juli_max_ind', 'juli_med', 'juli_skew', 'juli_kurt', 'juli_std',
       'x_v_mean', 'x_v_std', 'x_v_max', 'x_v_min', 'x_v_idmax',
       'x_v_idmin', 'y_v_mean', 'y_v_std', 'y_v_max', 'y_v_min',
       'y_v_idmax', 'y_v_idmin', 'total_v', 'hz_right', 'hz_left',
       'hz_stop_x', 'hz_up', 'hz_down', 'hz_stop_y', 'dianpin', 'targ_x',
       'targ_y', 'x_start', 'y_start', 'dist_en_tar_x', 'isback', 'back_x']

label_index=['label']
#

#
#
#
#
#
from imblearn.combine import SMOTEENN,SMOTETomek
#from keras.models import Sequential
#from keras.layers.core import Dense,Dropout,Activation
#from keras.optimizers import Adam
#from keras.utils import np_utils
#from keras.activations import elu
#import tensorflow as tf
from sklearn.cross_validation import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV
from sklearn.feature_selection import SelectPercentile,chi2,f_classif
from sklearn.feature_selection import SelectFromModel
import lightgbm as lgb
#
sm1 = SMOTEENN(random_state=99)
train_res1,label_res1=sm1.fit_sample(train[train_index],train[label_index])
sm2=SMOTETomek(random_state=99)
train_res2,label_res2=sm1.fit_sample(train[train_index],train[label_index])
train_res=np.concatenate((train_res1,train_res2),axis=0)
label_res=np.concatenate((label_res1,label_res2),axis=0)


####
sta=StandardScaler()
sta.fit(train_res)
train00=sta.transform(train_res)
test00=sta.transform(test)

lgm=lgb.LGBMClassifier()
sel=SelectFromModel(estimator=lgm,threshold='mean')
sel.fit(train00,label_res)
train01=sel.transform(train00)
test01=sel.transform(test00)

train_X,test_X,train_y,test_y=train_test_split(train01,label_res,test_size=0.01)

#xgb=XGBClassifier(
#                  colsample_bytree=0.7,
#                  gamma=0.6,
#                  max_depth=8,
#                  min_child_weight=0.9,
#                  reg_alpha=1.1,
#                  reg_lambda=1.2,
#                  subsample=0.002,
#                  learning_rate=0.0008,
#                  n_estimators=4000)
#train_XX=sel.transform(train_X)
#xgb.fit(train_XX,train_y)
#a=xgb.predict(test01)
#a=pd.DataFrame(a)
#a[0].value_counts()
#a['id']=range(1,100001)
#a.to_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\result.csv")


#{'max_depth': 5, 'min_child_weight': 0.6}
#{'colsample_bytree': 0.5}
#{'gamma': 0.0}
#{'subsample': 0.3}
#
#par={ 'max_depth':list(range(5,8,1)),
# 'min_child_weight':np.linspace(0.6,1.5,5)}
#grid=GridSearchCV(estimator =XGBClassifier(
#                  colsample_bytree=0.6,
#                  gamma=0.2,
#                  max_depth=6,
#                  min_child_weight=1,
#                  reg_alpha=1,
#                  reg_lambda=1,
#                  subsample=0.5,
#                  learning_rate=0.01,
#                  n_estimators=600)
#,param_grid = par,
#scoring='roc_auc',iid=False,cv=5,verbose=2)
#grid.fit(train_X,train_y)
#grid.best_params_


#a=(base_score=0.5,----1
#   colsample_bylevel=1,----2       (1)
#   colsample_bytree=1,----3         (0.5-1)       111111'colsample_bytree': 0.65
#       gamma=0, ----4              (0-0.5)        1111  'gamma': 0.3
#       learning_rate=0.1,----5  eta(0.01   , 0.2) 1111  'learning_rate': 0.01
#       max_delta_step=0,----6      (0)
#       max_depth=3,----7           (3-10)       1  111 'max_depth': 6
#       min_child_weight=1,----8    (0.6,2.0)     1111 'min_child_weight': 0.6
#       missing=None,----
#       n_estimators=100,----9     (50,500)     1111 'n_estimators': 280
#       nthread=-1,
#       objective='binary:logistic',----10(就他)
#       reg_alpha=0,----11   alpha (0.8-1.2)    1111'reg_alpha': 0.85
#       reg_lambda=1,----12   lambda(0.8-1.2)   1111,'reg_lambda': 0.85
#       scale_pos_weight=1,----13    (1)
#       seed=0, 
#       silent=True,
#       subsample=1)----14         (0.5-1)      11111'subsample': 0.8

#_-------------------------------------------------------litgbm

#par={'reg_alpha':np.linspace(0,1,10),
#     'reg_lambda':np.linspace(0,1,10)}
#grid=GridSearchCV(estimator =lgb.LGBMClassifier(
#        colsample_bytree=1,
#        drop_rate=0.1,
#        learning_rate=0.1,
#        max_bin=255,
#        max_depth=-1,
#        max_drop=50,
#        min_child_samples=10,
#        min_child_weight=5,
#        min_split_gain=0,
#        n_estimators=10,
#        num_leaves=31,
#        reg_alpha=0,
#        reg_lambda=0,
#        scale_pos_weight=1,
#        sigmoid=1.0,
#        skip_drop=0.5,
#        subsample=1,
#        subsample_for_bin=50000, 
#        subsample_freq=1,)
#,param_grid = par,
#scoring='roc_auc',iid=False,cv=10,verbose=2)
#grid.fit(train_X,train_y)
#grid.best_params_
#
#{'reg_alpha': 0.0, 'reg_lambda': 0.22222222222222221}
#{'max_bin': 257, 'min_child_weight': 4.0}
##{'max_drop': 47, 'min_child_samples': 8}
#{'max_drop': 42, 'min_child_samples': 5}
#{'n_estimators': 140}
# {'scale_pos_weight': 0.80000000000000004, 'sigmoid': 1.1000000000000001}
# {'drop_rate': 0.01, 'skip_drop': 0.29999999999999999}
# {'max_bin': 267}
# {'num_leaves': 20}
# {'subsample': 1.0}
# {'subsample_freq': 1}
# {'colsample_bytree': 0.29999999999999999}
#{'drop_rate': 0.05}
#{'min_child_weight':4.6}
#{'reg_alpha': 0.0, 'reg_lambda': 0.0}
#{'max_bin': 249}
#{'max_drop': 30}
#{'n_estimators': 70}
#{'num_leaves': 20}
#{'scale_pos_weight': 1.0}
#{'skip_drop': 0.2}
#{'sigmoid': 0.9}
#{'subsample': 1.0}
#{'subsample_for_bin': 40000}
#reg_alpha=0, reg_lambda=0,
#subsample=1
#min_child_weight=5
#colsample_bytree

lgm=lgb.LGBMClassifier(
        colsample_bytree=0.3,
        drop_rate=0.01,
        learning_rate=0.1,
        max_bin=267,
        max_depth=-1,
        max_drop=20,
        min_child_samples=5,
        min_child_weight=4.0,
        min_split_gain=0,
        n_estimators=140,
        num_leaves=31,
        reg_alpha=0,
        reg_lambda=0.2,
        scale_pos_weight=0.8,
        sigmoid=1.1,
        skip_drop=0.3,
        subsample=1,
        subsample_for_bin=50000, 
        subsample_freq=1,)

lgm.fit(train_X,train_y)
a=lgm.predict(test01)
a=pd.DataFrame(a)
a[0].value_counts()
a['id']=range(1,100001)
a.to_csv(r"F:\桌面的东西\赛事数据\腾讯cccc\result.csv")