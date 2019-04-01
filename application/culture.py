import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_excel('文化汇总.xlsx')
# #
# # print(df.shape)
# # print(df.head())
#
# df_china = df[df['nation']==1].drop(columns='nation')
# df_zulu = df[df['nation']==2].drop(columns='nation')
# # print(df_china.head())
# # print(df_china.describe())
#
# df_china['IDV01'].plot(kind='hist')
# plt.show()
# df_china['IDV01'].plot(kind='kde')
# plt.show()

df = pd.read_excel('level2.xlsx')
#
# print(df.shape)
# print(df.head())

df_china = df[df['nation']==1].drop(columns='nation')
df_zulu = df[df['nation']==2].drop(columns='nation')
# print(df_china.head())
# print(df_china.describe())

df_china['idv'].plot(kind='hist')
plt.show()
df_china['idv'].plot(kind='kde')
plt.show()



# df = pd.read_excel('china_aug.xls')
# #
# # print(df.shape)
# print(df.head())
#
# # print(df_china.head())
# # print(df_china.describe())
# #
# df['IDV01'].plot(kind='hist')
# plt.show()
# df['IDV01'].plot(kind='kde')
# plt.show()

# np.random.seed(123456789)
# array = np.random.normal(loc=2.5,scale =0.9,size=100)
# array = np.around(array,0)
# df = pd.Series(array)
# print(df)
# df.hist()
# plt.show()
# df.plot(kind='kde')
# plt.show()




# np.random.seed(123456789)
# array = np.random.randint(1,50,(250,3))
# # 中国
#
# df10 = df_china.loc[array[:,0]].reset_index(drop=True)
# df11 = df_china.loc[array[:,1]].reset_index(drop=True)
# df12 = df_china.loc[array[:,2]].reset_index(drop=True)
#
# df_china_aug=df10++df11+df12
#
#
# noise_df = pd.DataFrame(np.random.random_sample(df_china_aug.shape),columns=df_china_aug.columns)
# print(noise_df)
#
# df_china_aug = df_china_aug+noise_df
#
# df_china_aug = (df_china_aug/3).apply(np.round)
#
#
# # 祖鲁
# df_zulu = df_zulu.reset_index(drop=True)
# df20 = df_zulu.loc[array[:,0]].reset_index(drop=True)
# df21 = df_zulu.loc[array[:,1]].reset_index(drop=True)
# df22 = df_zulu.loc[array[:,2]].reset_index(drop=True)
#
# df_zulu_aug=df20+df21+df22
#
# df_zulu_aug = df_zulu_aug+noise_df
#
# df_zulu_aug = (df_zulu_aug/3).apply(np.round)
#
# df_china_aug.to_excel('china_aug_001.xls')
# df_zulu_aug.to_excel('zulu_aug_001.xls')


