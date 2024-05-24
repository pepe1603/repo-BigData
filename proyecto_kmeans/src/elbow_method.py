import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Cargar datos limpios
df = pd.read_csv('data/cleaned_WallCityTap_Consumer.csv')

# Preparar los datos para el clustering
df_clustering = df[['Age', 'Annual_Income', 'Spending Score (1-100)']]

# Calcular WCSS para diferentes valores de K
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_clustering)
    wcss.append(kmeans.inertia_)

# Graficar la relación entre K y WCSS
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Método del Codo')
plt.xlabel('Número de clusters (K)')
plt.ylabel('WCSS')
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()
