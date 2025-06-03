import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv('crypto_data.csv')

data['Volatility'] = (data['High'] - data['Low']) / data['Price']

X = data[['Volatility', 'Market Cap', 'Volume']].dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

linked = linkage(X_scaled, method='ward')

plt.figure(figsize=(12,6))
dendrogram(linked, labels=data['Symbol'].values, leaf_rotation=90, leaf_font_size=8)
plt.title('Dendrograma Cryptocurrencies')
plt.show()

clusters = fcluster(linked, 3, criterion='maxclust')
data['Cluster'] = clusters

print(data.groupby('Cluster')[['Volatility', 'Market Cap', 'Volume']].mean())