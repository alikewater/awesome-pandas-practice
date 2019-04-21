import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('文化汇总.xlsx')
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

# df = pd.read_excel('level2.xlsx')
#
# print(df.shape)
# print(df.head())

df_china = df[df['nation']==1].drop(columns='nation')
seed_cols=['PDI02','PDI7','PDI20','PDI23','IDV01','IDV04','IDV06','IDV09','MAS03','MAS05','MAS08','MAS10']
df_china_sub = df_china[seed_cols]
df_zulu = df[df['nation']==2].drop(columns='nation')
df_zulu_sub = df_zulu[seed_cols]


# print(df_china.head())
# print(df_china.describe())

# df_china['idv'].plot(kind='hist')
# plt.show()
# df_china['idv'].plot(kind='kde')
# plt.show()



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


np.random.seed(123456789)
array324 = np.random.randint(1,50,(311,2))
array277 = np.random.randint(1,50,(307,2))

# 中国

df10 = df_china.loc[array277[:,0]].reset_index(drop=True)
df11 = df_china.loc[array277[:,1]].reset_index(drop=True)
# df12 = df_china.loc[array[:,2]].reset_index(drop=True)

df_china_aug=df10++df11#+df12


noise_df01 = pd.DataFrame(np.random.random_sample(df_china_aug.shape),columns=df_china_aug.columns)
# print(noise_df)

df_china_aug = df_china_aug+noise_df01

df_china_aug = (df_china_aug/2).apply(np.round)

df_china_aug['PDI']= 35*(df_china_aug['PDI7'] - df_china_aug['PDI02']) + 25*(df_china_aug['PDI20'] -df_china_aug['PDI23'])
df_china_aug['IDV']= 35*(df_china_aug['IDV04'] - df_china_aug['IDV01']) + 35*(df_china_aug['IDV09'] - df_china_aug['IDV06'])
# df_china_aug['IVR'] = 35*(df_china_aug['IVR12']- df_china_aug['IVR11']) + 40*(df_china_aug['IVR17'] - df_china_aug['IVR16'])

#看法数据(中国)
np.random.seed(987654321)
array_sub324 = np.random.randint(1,50,(311,2))
array_sub277 = np.random.randint(1,50,(307,2))

df10 = df_china_sub.loc[array_sub277[:,0]].reset_index(drop=True)
df11 = df_china_sub.loc[array_sub277[:,1]].reset_index(drop=True)
df_china_aug_sub = df10++df11

noise_df02 = pd.DataFrame(np.random.random_sample(df_china_aug_sub.shape),columns=df_china_aug_sub.columns)


df_china_aug_sub = df_china_aug_sub+noise_df02
df_china_aug_sub = (df_china_aug_sub/2).apply(np.round)

df_china_aug_sub['a'] = df_china_aug_sub['PDI02']+df_china_aug_sub['PDI7']+df_china_aug_sub['PDI20']+df_china_aug_sub['PDI23'];
df_china_aug_sub['b'] = df_china_aug_sub['IDV01']+df_china_aug_sub['IDV04']+df_china_aug_sub['IDV06']+df_china_aug_sub['IDV09'];
# df_china_aug_sub['w'] = df_china_aug_sub['IVR11']+df_china_aug_sub['IVR12']+df_china_aug_sub['IVR16']+df_china_aug_sub['IVR17'];


#添加a列
df_china_aug.sort_values(by='PDI',ascending=False,inplace=True)
df_china_aug_sub.sort_values(by='a',ascending=False,inplace=True)
df_china_aug = df_china_aug.reset_index(drop=True)
df_china_aug_sub = df_china_aug_sub.reset_index(drop=True)

df_china_aug['a01'] = df_china_aug_sub['PDI02'];
df_china_aug['a02'] = df_china_aug_sub['PDI7'];
df_china_aug['a03'] = df_china_aug_sub['PDI20'];
df_china_aug['a04'] = df_china_aug_sub['PDI23'];

#添加b列
df_china_aug.sort_values(by='IDV',ascending=False,inplace=True)
df_china_aug_sub.sort_values(by='b',ascending=True,inplace=True)
df_china_aug = df_china_aug.reset_index(drop=True)
df_china_aug_sub=df_china_aug_sub.reset_index(drop=True)


df_china_aug['b01'] = df_china_aug_sub['IDV01'];
df_china_aug['b02'] = df_china_aug_sub['IDV04'];
df_china_aug['b03'] = df_china_aug_sub['IDV06'];
df_china_aug['b04'] = df_china_aug_sub['IDV09'];

#添加c列
df_china_aug['w01'] = df_china_aug_sub['MAS03'];
df_china_aug['w02'] = df_china_aug_sub['MAS05'];
df_china_aug['w03'] = df_china_aug_sub['MAS08'];
df_china_aug['w04'] = df_china_aug_sub['MAS10'];

df_china_aug = df_china_aug.sort_index()

# 祖鲁
df_zulu = df_zulu.reset_index(drop=True)
df20 = df_zulu.loc[array324[:,0]].reset_index(drop=True)
df21 = df_zulu.loc[array324[:,1]].reset_index(drop=True)
# df22 = df_zulu.loc[array[:,2]].reset_index(drop=True)

df_zulu_aug=df20+df21#+df22
np.random.seed(123456789)
noise_df01 = pd.DataFrame(np.random.random_sample(df_zulu_aug.shape),columns=df_zulu_aug.columns)

df_zulu_aug = df_zulu_aug+noise_df01

df_zulu_aug = (df_zulu_aug/2).apply(np.round)

df_zulu_aug['PDI']= 35*(df_zulu_aug['PDI7'] - df_zulu_aug['PDI02']) + 25*(df_zulu_aug['PDI20'] -df_zulu_aug['PDI23'])
df_zulu_aug['IDV']= 35*(df_zulu_aug['IDV04'] - df_zulu_aug['IDV01']) + 35*(df_zulu_aug['IDV09'] - df_zulu_aug['IDV06'])
# df_zulu_aug['IVR'] = 35*(df_zulu_aug['IVR12']- df_zulu_aug['IVR11']) + 40*(df_zulu_aug['IVR17'] - df_zulu_aug['IVR16'])


#看法数据(祖鲁)
print(df_zulu_sub.index)

df_zulu_sub = df_zulu_sub.reset_index(drop=True)
df20 = df_zulu_sub.loc[array_sub324[:,0]].reset_index(drop=True)
df21 = df_zulu_sub.loc[array_sub324[:,1]].reset_index(drop=True)
df_zulu_aug_sub = df20++df21

# noise_df = pd.DataFrame(np.random.random_sample(df_zulu_aug_sub.shape),columns=df_zulu_aug_sub.columns)
np.random.seed(987654321)
noise_df02 = pd.DataFrame(np.random.random_sample(df_zulu_aug_sub.shape),columns=df_zulu_aug_sub.columns)

df_zulu_aug_sub = df_zulu_aug_sub+noise_df02
df_zulu_aug_sub = (df_zulu_aug_sub/2).apply(np.round)

df_zulu_aug_sub['a'] = df_zulu_aug_sub['PDI02']+df_zulu_aug_sub['PDI7']+df_zulu_aug_sub['PDI20']+df_zulu_aug_sub['PDI23'];
df_zulu_aug_sub['b'] = df_zulu_aug_sub['IDV01']+df_zulu_aug_sub['IDV04']+df_zulu_aug_sub['IDV06']+df_zulu_aug_sub['IDV09'];
# df_zulu_aug_sub['w'] = df_zulu_aug_sub['IVR11']+df_zulu_aug_sub['IVR12']+df_zulu_aug_sub['IVR16']+df_zulu_aug_sub['IVR17'];


#添加a列

df_zulu_aug.sort_values(by='PDI',ascending=False,inplace=True)
df_zulu_aug_sub.sort_values(by='a',ascending=False,inplace=True)
df_zulu_aug = df_zulu_aug.reset_index(drop=True);
df_zulu_aug_sub = df_zulu_aug_sub.reset_index(drop=True)

df_zulu_aug['a01'] = df_zulu_aug_sub['PDI02'];
df_zulu_aug['a02'] = df_zulu_aug_sub['PDI7'];
df_zulu_aug['a03'] = df_zulu_aug_sub['PDI20'];
df_zulu_aug['a04'] = df_zulu_aug_sub['PDI23'];


#添加b列
df_zulu_aug.sort_values(by='IDV',ascending=False,inplace=True)
df_zulu_aug_sub.sort_values(by='b',ascending=True,inplace=True)
df_zulu_aug = df_zulu_aug.reset_index(drop=True);
df_zulu_aug_sub = df_zulu_aug_sub.reset_index(drop=True)

df_zulu_aug['b01'] = df_zulu_aug_sub['IDV01'];
df_zulu_aug['b02'] = df_zulu_aug_sub['IDV04'];
df_zulu_aug['b03'] = df_zulu_aug_sub['IDV06'];
df_zulu_aug['b04'] = df_zulu_aug_sub['IDV09'];

#添加c列
df_zulu_aug['w01'] = df_zulu_aug_sub['MAS03'];
df_zulu_aug['w02'] = df_zulu_aug_sub['MAS05'];
df_zulu_aug['w03'] = df_zulu_aug_sub['MAS08'];
df_zulu_aug['w04'] = df_zulu_aug_sub['MAS10'];



df_zulu_aug.to_excel('china_aug_002.xls')
df_china_aug.to_excel('zulu_aug_002.xls')


