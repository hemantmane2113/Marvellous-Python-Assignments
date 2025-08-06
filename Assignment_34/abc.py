import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
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

    variance = numeric_df.var()
    skewness = numeric_df.apply(skew)

    summary = pd.DataFrame({
        "Variance":variance,
        "Skewness":skewness,
        "MissingValue(%)":numeric_df.isnull().mean() * 100
         })
    
    summary_sorted = summary.sort_values(by = ["Variance","Skewness"],ascending = False)

    print(summary_sorted.head(10))

    top_features = summary_sorted.head(5).index
    
    for col in top_features:
        plt.figure(figsize=(12,4))

        plt.subplot(1,2,1)
        sns.histplot(df[col].dropna(),kde = True)
        plt.title(f"Histogram & KDE: {col}")

        plt.subplot(1,2,1)
        sns.histplot(x = df[col])
        plt.title(f"Boxplot: {col}")

        plt.tight_layout()

        plt.show()

    correlations = df.corr()["Target"].sort_values(key = abs,ascending=False)

    print(correlations.head(10))


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