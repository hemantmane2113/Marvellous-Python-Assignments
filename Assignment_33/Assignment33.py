import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


def Student_performance(DataPath):

    df = pd.read_csv(DataPath,sep = ";")

    #print(df.head())

    #print(df.info())

#1. Using G1,G2 and G3

    X1 = df[["G1","G2","G3"]]

    scalar = StandardScaler()

    X1_scaled = scalar.fit_transform(X1)

    model = KMeans(n_clusters=3,init = 'k-means++',n_init=10,random_state=42)

    df['Cluster_G1_G2_G3'] = model.fit_predict(X1_scaled)


    #plotting
    sns.pairplot(df, vars=["G1","G2","G3"], hue='Cluster_G1_G2_G3', palette='Set2')
    plt.suptitle("Pair Plot of Clusters", y=1.02)
    plt.show()

#2 Using Study time

    X2 = df[["studytime"]].values

    X2_scaled = scalar.fit_transform(X2)

    model = KMeans(n_clusters=3,init = 'k-means++',n_init=10,random_state=42)

    df['Cluster_studytime'] = model.fit_predict(X2_scaled)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(df['studytime'], [0]*len(df), c=df['Cluster_studytime'], cmap='viridis', s=50)
    plt.xlabel("studytime")
    plt.yticks([])  # Hide Y-axis for clarity
    plt.title("1D K-Means Clustering on studytime")
    plt.grid(True)
    plt.show()


#3 Using failures

    X3 = df[["failures"]].values

    X3_scaled = scalar.fit_transform(X3)

    model = KMeans(n_clusters=3,init = 'k-means++',n_init=10,random_state=42)

    df['Cluster_failures'] = model.fit_predict(X3_scaled)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(df['failures'], [0]*len(df), c=df['Cluster_failures'], cmap='viridis', s=50)
    plt.xlabel("failures")
    plt.yticks([])  # Hide Y-axis for clarity
    plt.title("1D K-Means Clustering on failures")
    plt.grid(True)
    plt.show()


#4 Using absences

    X4 = df[["absences"]].values

    X4_scaled = scalar.fit_transform(X4)

    model = KMeans(n_clusters=3,init = 'k-means++',n_init=10,random_state=42)

    df['Cluster_absences'] = model.fit_predict(X4_scaled)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(df['absences'], [0]*len(df), c=df['Cluster_absences'], cmap='viridis', s=50)
    plt.xlabel("absences")
    plt.yticks([])  # Hide Y-axis for clarity
    plt.title("1D K-Means Clustering on absences")
    plt.grid(True)
    plt.show()


 #5.Using all important features together

    X = df[["studytime","failures","absences","G1","G2","G3"]]

    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    model = KMeans(n_clusters=3,init = 'k-means++',n_init=10,random_state=42)

    df['Cluster_all_features_combined'] = model.fit_predict(X_scaled)

    #plotting

    #attempt1
    # trying to plot any two features at any given time to see clustering

    #plt.figure(figsize=(8,6))
    # plt.scatter(df['absences'], df['failures'], c=df['Cluster'], cmap='viridis', s=50)
    # plt.xlabel("Studytime")
    # plt.ylabel("failures")
    # plt.title("K-Means Clusters")
    # plt.colorbar(label="Cluster")
    # plt.grid(True)
    # plt.show()

    #attempt2
    #trying to plot all features vs all features at once to see clustering

    # sns.pairplot(df, vars=["studytime","failures","absences","G1","G2","G3"], hue='Cluster', palette='Set2')
    # plt.suptitle("Pair Plot of Clusters", y=1.02)
    # plt.show()

    

    #attempt3
    #As we have more than 2 features we are using principal component analysis to reduce
    #the dimensionality for 2D clustering

    features = ["studytime","failures","absences","G1","G2","G3"]
    #features = df.columns.to_list()-->to print all features

    pca = PCA(n_components=2)
    components = pca.fit_transform(X_scaled)

    print("Original shape of dataframe: ",X_scaled.shape)# original shape of df
    print("Shape of dataframe after PCA: ",components.shape)# data in pc1 and pc2
    print("(PCA components,Features) --> ",pca.components_.shape)#PCA components how much 6 features contribute to 2 components
    print()
    centers = pca.transform(model.cluster_centers_)#for centroid(s)

    # Get the components
    components_df = pd.DataFrame(pca.components_, columns=features, index=["PC1", "PC2"])

    print("Principal Component Loading or Matrix Loading or Component co-efficients: ")
    print(components_df)
    print()
    print("Principal Component Loading-Transposed")
    print(components_df.T)  # Transpose to see nicely
    print()


    plt.figure(figsize=(8,6))
    plt.scatter(components[:, 0], components[:, 1], c=df['Cluster_all_features_combined'], cmap='plasma', s=50) 
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.6, marker='X', label='Centroids')
    plt.legend()
    plt.title("Clusters Visualized in 2D using PCA")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.colorbar(label="Cluster_all_features_combined")
    plt.show()

    # Create a mapping
    cluster_map = {0:'Average student',1:'Top Performer',2:'Struggling student'}
    

    # Replace values in the DataFrame
    df['cluster_label'] = df['Cluster_all_features_combined'].map(cluster_map)

    print("Statistical analysis of clustering is as follows: ")
    print(df.groupby('cluster_label')[['studytime', 'failures', 'absences', 'G1', 'G2', 'G3']].mean())
    print()

    print("Total students per cluster are: ")
    print(df['cluster_label'].value_counts())


    #Adding two components to original df and saving it as newer csv file
    df_selected = df[['Cluster_all_features_combined', 'cluster_label']]
    df_original = pd.read_csv("student-mat.csv",sep = ";") 
    df_combined = pd.concat([df_original, df_selected], axis=1)

    df_combined.to_csv("student_performance_clusters_.csv", index=False)




def main():

    DataSet = "student-mat.csv"

    Student_performance(DataSet)


if __name__ == "__main__":
    main()