import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN

dt = pd.read_csv('gxdc_gj20201221.csv')

data = dt[['LATITUDE','LONGITUDE']]

db = DBSCAN(eps=0.002, min_samples=2000).fit(data)

labels = db.labels_
dt['cluster_db'] = labels
dt.sort_values('cluster_db')

