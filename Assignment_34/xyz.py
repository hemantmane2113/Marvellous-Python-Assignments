import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer

def Breast_Cancer():
    breast_cancer  = load_breast_cancer()

    df = pd.DataFrame(data = breast_cancer.data,columns = breast_cancer.feature_names)
    df["Target"] = breast_cancer.target

    #df["Diagnosis"] = df["Target"].apply(lambda x: breast_cancer.target_names[x])

    # EXPLORATORY DATA ANALYSIS

    #1.Understand the structure of the data

    print("Inspecting the initial few rows: ")
    print(df.head())

    print("Inspecting the final few rows: ")
    print(df.tail())

    print("Understanding column and datatypes: ")
    print(df.info())

    print("Checking shape of dataframe: ")
    print(df.shape)

    #2.Descriptive Statistics
    print("Numerical summary of dataframe: ")
    print(df.describe())

    print("Total value count: ")
    print(df.value_counts)

    print("Checking for null values,if any: ")
    print(df.isna().sum().sum())

    #3.Data cleaning
    print("Checking for  duplicate values, if any: ")
    print(df.duplicated().sum())

    #4.Univariate Analysis(one variable at a time)

    numeric_df = df.select_dtypes(include = ["int64",'float64'])

    num_cols = len(numeric_df.columns)

    cols = 3
    rows = math.ceil(num_cols/cols)

    fig,axes = plt.subplots(rows,cols,figsize = (cols * 5,rows * 4))
    axes = axes.flatten()

    for i,col in enumerate(numeric_df.columns):
        sns.histplot(numeric_df[col].dropna(),kde = True,ax = axes[i])
        axes[i].set_title(col)

    for j in range(i+1,len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

 

    correlation_matrix = df.corr()
    
    plt.figure(figsize = (8,6))
    sns.heatmap(correlation_matrix,annot = True,cmap = 'coolwarm',fmt = ".2f",linewidth = .5)
    plt.title("Correlation Matrix Heatmap")
    plt.show()

    custom_palette = {0:"lightblue",1:"pink"}
    sns.pairplot(df,hue = "Target",palette = custom_palette)
    plt.show()




def main():
    Breast_Cancer()


if __name__ == "__main__":
    main()