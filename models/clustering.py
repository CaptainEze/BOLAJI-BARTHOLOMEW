from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_respodents(df, n_clusters=3):
    features = df[["Adoption_Avg", "Sustainability_Avg", "Delivery_Avg", "D_Position", "D_Experience"]]
    X_scaled = StandardScaler().fit_transform(features)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X_scaled)
    
    return df, kmeans
