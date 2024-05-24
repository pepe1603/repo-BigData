import pandas as pd
from sklearn.cluster import KMeans

# Cargar datos limpios
df = pd.read_csv('data/cleaned_WallCityTap_Consumer.csv')

# Definir el número óptimo de clusters (K) basado en el método del codo
optimal_k = 3  # Supongamos que el método del codo sugiere que 3 es el valor óptimo

# Aplicar K-means
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Age', 'Annual_Income', 'Spending Score (1-100)']])

# Guardar los resultados del clúster
df.to_csv('data/WallCityTap_Consumer_clustered.csv', index=False)
