import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder



class Preprocess(object):
    def __init__(self, df_train, df_test):
        '''
            set dataframe
        '''
        self.df_train = df_train
        self.df_test = df_test

    def fill_na(self):
        '''
            データの欠損を補完
            df[column].fillna()を使う
            example.
            self.df_train['Age'].fillna(self.df_train['Age'].median(), inplace=True)
            
        '''
        pass

    def drop_features(self, features):
        '''
            特定コラムの列を消去
            example.
            self.df_train.drop(features, axis=1, inplace=True)
        '''
        self.df_train.drop(features, axis=1, inplace=True)
        self.df_test.drop(features, axis=1, inplace=True)


    def create_features(self):
        '''
        '''
        pass

    def convert_features(self):
        '''
            文字列を符号化
            label_encoding = LabelEncoder()
            self.df_train['Sex_Code'] = label_encoding.fit_transform(self.df_train['Sex'])
        '''
        pass
