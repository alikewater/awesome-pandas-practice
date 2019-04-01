import pandas as pd
import numpy as np

def get_circle_area(l,h):
    r = np.sqrt(l**2+h**2)/2
    return r**2*np.pi


rects = pd.read_excel('Reactangles.xlsx',index_col='ID')

rects['CA'] = rects.apply(lambda row:get_circle_area(row['Length'],row['Height']))

print(rects)


