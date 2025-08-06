import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score,roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

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

    numerical_columns = df.select_dtypes(include = ["int64",'float64']).columns
    

    # #Histogram for each numerical column
    # for col in numerical_columns:
    #     plt.figure(figsize = (8,6))
    #     sns.histplot(df[col],kde = True)
    #     plt.title(f"Histogram and KDE of {col}")
    #     plt.show()

    # #BoxPlot for each numerical column
    # for col in numerical_columns:
    #     plt.figure(figsize = (8,6))
    #     sns.boxplot(df[col])
    #     plt.title(f"Boxplot of {col}")
    #     plt.show()

    
    numeric_df = df.select_dtypes(include = ["int64",'float64'])

    cov_matrix = numeric_df.cov()

    
    # plt.figure(figsize = (8,6))
    # sns.heatmap(cov_matrix,annot = True,cmap = 'coolwarm',fmt = ".2f",linewidths=.5)
    # plt.title("Covariance matrix")
    # plt.show()
    
    # correlation_matrix = df.corr()
    
    # plt.figure(figsize = (8,6))
    # sns.heatmap(correlation_matrix,annot = True,cmap = 'coolwarm',fmt = ".2f",linewidth = .5)
    # plt.title("Correlation Matrix Heatmap")
    # plt.show()

    # custom_palette = {0:"lightblue",1:"pink"}

    # sns.pairplot(df,hue = "Target",diag_kind="kde",palette = custom_palette)
    # plt.show()

    # BUILDING a MODEL

    X = df.drop(columns = "Target")#df.drop("Target",,axis = 1)

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    Y = df["Target"]

    X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

    models = {
        "Logistic Regression":LogisticRegression(),
        "KNN Classifier": KNeighborsClassifier(),
        "Decision Tree Classifier": DecisionTreeClassifier(),
        "Random Forest Classifier":RandomForestClassifier()
    }

    plt.figure(figsize=(10, 8))

    for name_of_model,clf_model in models.items():
        clf_model.fit(X_train,Y_train)
        y_pred = clf_model.predict(X_test)
        y_score = clf_model.predict_proba(X_test)[:,1]
        fpr,tpr,thresholds = roc_curve(Y_test,y_score)
        auc = roc_auc_score(Y_test,y_score)

        print("#" * 60)
        print(f"{name_of_model} Accuracy : {accuracy_score(Y_test,y_pred)}")
        print(f"{name_of_model} Confusion Matrix  :\n {confusion_matrix(Y_test,y_pred)}")
        print(f"{name_of_model} Classification_report :\n {classification_report(Y_test,y_pred)}")
        print(f"{name_of_model} ROC AUC Score : {auc}")
        print("#" * 60)

        plt.plot(fpr,tpr,label = f"{name_of_model} (AUC = {auc})")

    plt.plot([0,1],[0,1],'k--')
    plt.title("ROC curve for multiple models")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc = "lower right")
    plt.grid(True)
    plt.show()


def main():
    Breast_Cancer()


if __name__ == "__main__":
    main()