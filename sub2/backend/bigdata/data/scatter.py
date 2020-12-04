import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv("./userNewData5.csv", encoding = 'utf-8')
del df['email']
df_scaled = StandardScaler().fit_transform(df)

pca = PCA(n_components=2)

x_values = []
y_values = []

pca.fit(df_scaled)
df_pca = pca.transform(df_scaled)

pca_columns = ['x','y']
result = pd.DataFrame(df_pca, columns=pca_columns)

x_values = result['x'].tolist()
y_values = result['y'].tolist()

plt.scatter(x_values,y_values)
plt.show()