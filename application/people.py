import pandas as pd
import numpy as np


#根据描述字典生成分布
def gen_dis(dis):
    list=[]
    idx = 0
    for key in dis:
        dis_key = dis[key]
        low = dis_key['low']
        high = dis_key['high']
        size = dis_key['size']
        if(low<high):
            array1 = np.random.randint(low,high,size).reshape(size,1)
        else:
            array1 = np.repeat(low,size).reshape(size,1)

        array2 =np.repeat(key,size).reshape(size,1)
        list.append(np.concatenate([array1,array2],axis=1))

        idx=idx+1
    return list
    # array_male = np.repeat(1,np.round(total*))
    # array_female = np.repeat(2,total-np.round(total*percent))

    # print(array_male)

    # array = np.concatenate([array_male,array_female])
    # np.random.shuffle(array)
    # print(array)
    # china_male_dis = pd.DataFrame(array,columns=['Sex'])
    # return china_male_dis

#生成分布描述字典
def gen_dis_dict(total,dis_percent):
    dict={}
    idx=1
    counted = 0
    for key in dis_percent:
        o = {}
        o['low'] = dis_percent[key]['low']
        o['high'] = dis_percent[key]['high']
        if(idx<len(dis_percent)):
            o['size'] = np.round(total*dis_percent[key]['percent']).astype(int)
        else:
            o['size'] = total - counted
        # print(o['size'])
        idx=idx+1
        counted=counted+o['size']

        dict[key] = o

    return dict


#中国

#性别生成
total = 311
dis_percent ={ 'm':{'low':1,'high':1,'percent':0.12},'f':{'low':2,'high':2,'percent':0.88}}
dict = gen_dis_dict(total,dis_percent)

sex = gen_dis(dict)
sex = np.concatenate(sex)

#年龄生成
dis_percent ={ '50-59': {'low': 50, 'high': 59, 'percent': 0.09},'20-24':{'low':20,'high':24,'percent':0.07},
               '25-29':{'low':25,'high':29,'percent':0.11},
               '30-34':{'low':30,'high':34,'percent':0.16},'35-39':{'low':35,'high':39,'percent':0.25},
               '40-49': {'low': 40, 'high': 49, 'percent': 0.32}}
dict = gen_dis_dict(total,dis_percent)

age = gen_dis(dict)
age = np.concatenate(age)
np.random.shuffle(age)

#教育
dis_percent ={ '13': {'low': 13, 'high': 13, 'percent': 0}, '14': {'low': 14, 'high': 14, 'percent': 0},
                '0-9':{'low':0,'high':9,'percent':0.77},'10':{'low':10,'high':10,'percent':0.08},
               '11':{'low':11,'high':11,'percent':0.13},'12':{'low':12,'high':12,'percent':0.02}
               }
dict = gen_dis_dict(total,dis_percent)

edu = gen_dis(dict)
edu = np.concatenate(edu)
np.random.shuffle(edu)


#职业

dis_percent ={ 'Unskilled': {'low': 1, 'high': 1, 'percent': 0.94},
               'General': {'low': 2, 'high':2, 'percent': 0},
                'Vocationally':{'low':3,'high':3,'percent':0.06}
               }
dict = gen_dis_dict(total,dis_percent)

ocu = gen_dis(dict)
ocu = np.concatenate(ocu)
np.random.shuffle(ocu)

overall = np.concatenate([sex,age,edu,ocu],axis=1)

np.random.shuffle(overall)

# print(overall)

cols = ['Sex','SexDecs','Age','AgeDesc','Edu','EduDesc','Ocu','OcuDesc']

china_people = pd.DataFrame(overall,columns = cols)

china_people.to_excel('china_people.xls')

#==============================================祖鲁===========================================
#性别生成
total = 307
dis_percent ={ 'm':{'low':1,'high':1,'percent':0.12},'f':{'low':2,'high':2,'percent':0.88}}
dict = gen_dis_dict(total,dis_percent)

sex = gen_dis(dict)
sex = np.concatenate(sex)
#乱序
np.random.shuffle(sex)

#年龄生成
dis_percent ={ '50-59': {'low': 50, 'high': 59, 'percent': 0.03},'20-24':{'low':20,'high':24,'percent':0.24},
               '25-29':{'low':25,'high':29,'percent':0.37},
               '30-34':{'low':30,'high':34,'percent':0.13},'35-39':{'low':35,'high':39,'percent':0.17},
               '40-49': {'low': 40, 'high': 49, 'percent': 0.06}}
dict = gen_dis_dict(total,dis_percent)

age = gen_dis(dict)
age = np.concatenate(age)
np.random.shuffle(age)

#教育
dis_percent ={ '13': {'low': 13, 'high': 13, 'percent': 0.01}, '14': {'low': 14, 'high': 14, 'percent': 0.01},
                '0-9':{'low':0,'high':9,'percent':0.53},'10':{'low':10,'high':10,'percent':0.05},
               '11':{'low':11,'high':11,'percent':0.06},'12':{'low':12,'high':12,'percent':0.34}
               }
dict = gen_dis_dict(total,dis_percent)

edu = gen_dis(dict)
edu = np.concatenate(edu)
np.random.shuffle(edu)


#职业

dis_percent ={ 'Unskilled': {'low': 1, 'high': 1, 'percent': 0.97},
               'General': {'low': 2, 'high':2, 'percent': 0.01},
                'Vocationally':{'low':3,'high':3,'percent':0.02}
               }
dict = gen_dis_dict(total,dis_percent)

ocu = gen_dis(dict)
ocu = np.concatenate(ocu)
np.random.shuffle(ocu)

overall = np.concatenate([sex,age,edu,ocu],axis=1)

# print(overall)

cols = ['Sex','SexDecs','Age','AgeDesc','Edu','EduDesc','Ocu','OcuDesc']

zulu_people = pd.DataFrame(overall,columns = cols)

zulu_people.to_excel('zulu_people.xls')




