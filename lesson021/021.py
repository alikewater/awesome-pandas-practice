import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 999
videos = pd.read_excel('Videos.xlsx',index_col='Month')
print(videos.head(3))

table = videos.transpose();
print(table)

