import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix,ConfusionMatrixDisplay
from sklearn.metrics import roc_auc_score,auc,roc_curve


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def Breast_Cancer(data_path):

    df = pd.read_csv(data_path)

    # print(df.head)
    # print(df.describe())
    # print(df.info())
    # print(df.columns)

    df["BareNuclei"] = df["BareNuclei"].replace("?",np.nan)#convert to null value

    df["BareNuclei"] = pd.to_numeric(df["BareNuclei"])#-->object to float

    df["BareNuclei"] = df["BareNuclei"].fillna(df["BareNuclei"].mode()[0])# fill with mode([0]..first most occuring value)

    df["BareNuclei"] =df["BareNuclei"].astype(int)# type cast to int
    #keep in mind we can convert float to int directly ,but if there are any np.nan values in a column, we can't -->ValueError: cannot convert float NaN to integer
    #Therefore missing value -> np.nan->convert datatype to numeric(float)->fill np.nan with mode ->now typecast  

    print(df.dtypes)

    df["CancerType"] = df["CancerType"].replace({2:0,4:1})

    # for values in df["BareNuclei"]:
    #     print(values)

    X = df.drop(columns = "CancerType")#X = df.drop("BareNuclei", axis=1)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    Y = df["CancerType"]

    labels = df["CancerType"].unique()

    X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

    model_1 = DecisionTreeClassifier()

    model_1.fit(X_train,Y_train)

    y_pred = model_1.predict(X_test)

    Accuracy_1 = accuracy_score(Y_test,y_pred)

    Conf_Mat_1 = confusion_matrix(Y_test,y_pred)

    Cls_rpt_1 = classification_report(Y_test,y_pred)

    y_score = model_1.predict_proba(X_test)[:, 1] #probabilites for class 1(positive)

    roc_auc_score_1 = roc_auc_score(Y_test,y_score)#Area under ROC-AUC curve

    fpr_1,tpr_1,thresholds_1 = roc_curve(Y_test,y_score)

    roc_auc_1 = auc(fpr_1,tpr_1) #Area under ROC-AUC curve


    model_2 = RandomForestClassifier(n_estimators=150,max_depth=7,random_state=42)

    model_2.fit(X_train,Y_train)

    y_pred = model_2.predict(X_test)

    Accuracy_2 = accuracy_score(Y_test,y_pred)

    Conf_Mat_2 = confusion_matrix(Y_test,y_pred)

    Cls_rpt_2 = classification_report(Y_test,y_pred)

    y_score = model_2.predict_proba(X_test)[:, 1]

    roc_auc_score_2 = roc_auc_score(Y_test,y_score)#Area under ROC-AUC curve

    fpr_2,tpr_2,thresholds_2 = roc_curve(Y_test,y_score)

    roc_auc_2 = auc(fpr_2,tpr_2) #Area under ROC-AUC curve

    #checking feature importance
    importance = pd.Series(model_2.feature_importances_,index = X.columns)
    importance = importance.sort_values(ascending = False)
    #plotting feature importance
    importance.plot(kind = 'bar',figsize = (10,6),title = 'Feature importance')
    plt.show()

        #plotting pre-requisities
    models = [model_1,model_2]

    Accuracy = [Accuracy_1,Accuracy_2]

    Cls_Report = [Cls_rpt_1,Cls_rpt_2]

    ROC_AUC = [roc_auc_score_1,roc_auc_score_2]#Area under ROC-AUC curve

    Conf_Mat = [Conf_Mat_1,Conf_Mat_2]

    fpr  = [fpr_1,fpr_2]

    tpr = [tpr_1,tpr_2]
    
    roc_auc = [roc_auc_1,roc_auc_2]#Area under ROC-AUC curve

    thresholds = [thresholds_1,thresholds_2]
    


   
    print("------STATSTICAL ANALYSIS FOR EACH MODEL IS AS FOLLOWS-------------")
    #accuracy score,ROC-AUC score,classification report,confusion matrix
    for i in range(2):
        print("-"*70)
        print(f"The {models[i]} has: ")
        print(f"Accuracy score: {Accuracy[i]}")
        print(f"ROC-AUC score: {ROC_AUC[i]}")
        print(f"classification report: \n{Cls_Report[i]}")  
        print(f"Confusion Matrix: \n{Conf_Mat[i]}")
        print("-"*70)
    
    #displaying confusion matrix model wise
    for i in range(2):
        disp = ConfusionMatrixDisplay(confusion_matrix= Conf_Mat[i],display_labels = labels)
        disp.plot(cmap = plt.cm.Blues)
        plt.title(f"Conusion Matrix for {models[i]}")
        plt.show()

    #displaying ROC-AUC curve plot model wise
        plt.figure(figsize=(8,6))
        plt.plot(fpr[i],tpr[i],label = "ROC curve (area = %0.2f)" % roc_auc[i])
        plt.plot([0,1],[0,1],'k--',label = 'Random Guess')
        plt.xlim([0.0,1.0])
        plt.ylim([0.0,1.05])
        plt.xlabel("False positive Rate")
        plt.ylabel("True positive Rate")
        plt.title("ROC curve for Breast Cancer Prediction")
        plt.legend()
        plt.show()

    # All in one model ROC-AUC curve
    plt.figure(figsize=(8,6))
    for i in range(2):
        plt.plot(fpr[i],tpr[i],label = f"Model {i+1} (AUC = {roc_auc[i]:.2f}")
    plt.plot([0,1],[0,1],'k--',label = 'Random Guess')
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.05])
    plt.xlabel("False positive Rate")
    plt.ylabel("True positive Rate")
    plt.title("ROC curve for Bank term deposit subcription classification")
    plt.legend()
    plt.show()


    for values in ROC_AUC:
        print("ROC_AUC:",values)
    print("-" * 40)

    for model_index, thresholds in enumerate(thresholds, start=1):
        print(f"Model {model_index} Thresholds:")
        for t in thresholds:
            print(f"{t:.4f}")
    print("-" * 40)

    for values in roc_auc:
        print("roc_auc:",values)

def main():

    dataset = "breast-cancer-wisconsin.csv"

    Breast_Cancer(dataset)


if __name__ == "__main__":
    main()


    """
Very Important

roc_auc_score(Y_test, y_score) ≡ auc(fpr, tpr) (when fpr, tpr are calculated correctly from y_score)

🔍 So, which one should you keep?

    ✅ Use roc_auc_score() if you just want the AUC number — it's simpler and cleaner.

    roc_auc = roc_auc_score(Y_test, y_score)

    ✅ Use roc_curve() + auc() if you also want to plot the ROC curve:

    fpr, tpr, _ = roc_curve(Y_test, y_score)
    roc_auc = auc(fpr, tpr)

    If you're plotting the ROC curve anyway, you can stick with the second one.
    🧠 TL;DR:
     Do you need to plot ROC?	                       Keep this line
         ❌ No	                                  roc_auc_score(Y_test, y_score)
         ✅ Yes	                                  roc_curve(...) + auc(...)

    """