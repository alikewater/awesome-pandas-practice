叩开统计大门，把函数一网打尽——【求和，求平均，统计导引】
dataframe添加列：采用df['Name'] = seriesA的方式进行
dataframe添加行：采用df.append(seriesA,ingnore_index = True)

mean/sum等统计函数的轴向，默认是按列进行汇总，axis=1表示按行进行统计

获取部分列，采用df[]括号中是列名或者列名的list
如果还要进行细粒度的局部数据提取则用loc
