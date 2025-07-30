import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from scipy.stats import chi2_contingency

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import roc_auc_score,roc_curve,auc
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression



def Bank_Marketing(dataset):

    df = pd.read_csv(dataset,sep=';')
    """

    #first see wheather the df is comma separated(original csv type) or whitespace separated
    or tab- separated or semicolon separated


    df = pd.read_csv(dataset)->normal,comma separated
    df = pd.read_csv(dataset,delim_Whitespace = True)-->whitespace separated
    df = pd.read_csv(dataset,sep='\t')-->tab separated
    df = pd.read_csv(dataset,sep=';')-->semicolon separated

    """
    
    print(df.head)
    print(df.info())

    #to know the 'unknowns' in each column
    print((df == 'unknown').sum())
    
    #wanted to know how many categories with total number of entries in the job column
    grouped_df = df.groupby('job').size()
    print(grouped_df)

    #replacing 'unknown' with null values
    df.replace('unknown',np.nan,inplace=True)

    #to know the "null" values in each column (similar to print((df == 'unknown').sum()))
    print(df.isna().sum())

    #dropping unwanted columns by analysing 'visually'
    df.drop(columns = ["day","month","contact","poutcome"],inplace=True)

    #instead of dropping null values(cant fill them due to they being 'string' datatype,we
    # are converting them into new category-'other')
    df.replace(np.nan,'other',inplace = True)

    #just to check if any 'null' value exists
    print(df.isna().sum())

    #LABEL ENCODING

    df_encoded = df.copy()

    label_encoders = {}#dictornary to store the encoders for each column
    """
    eg {"column_name1:{
    "category1":0,
    "Category2":1
    ...},
    Column_name2:{
    "Category1":0,
    "Categeory2:1,
    "Category2":2}
    ..}...its dictionary within dictionary
    """

    for col in df_encoded.select_dtypes(include = ['object']).columns:
        
        label_encode = LabelEncoder()

        df_encoded[col] = label_encode.fit_transform(df_encoded[col].astype(str))
        label_encoders[col] = label_encode#saves the enocders used for each column in dictionary

    #to see the encoders for each column(chatgpt code)
    for col,label_encode in label_encoders.items():
        print(f"column:{col}")
        for class_,index in zip(label_encode.classes_,label_encode.transform(label_encode.classes_)):
            print(f"{class_}-->{index}")
        print()



    #feature importance
    column_names = df_encoded.columns.values

    # corrmat = df_encoded[column_names].corr()

    # mask = np.zeros_like(corrmat)
    # mask[np.triu_indices_from(mask)]= True

    # sns.heatmap(corrmat,
    #             vmax = 1,vmin=1,
    #             annot = True,annot_kws = {'fontsize':7},
    #             mask = mask,
    #             cmap = sns.diverging_palette(20,220,as_cmap = True))
    # plt.show()

    # sns.pairplot(df_encoded[column_names])
    # plt.show()

    #chi-square test

    # for col in column_names:
        
    #     contingency_table = pd.crosstab(df_encoded[col],df_encoded['y'])
    #     chi2,p,dof,expected = chi2_contingency(contingency_table)

    #     print(f"{col}-->  chi-square:{chi2},  p-value:{p}")

    X = df_encoded.drop(columns = 'y',axis = 1)  
    Y = df_encoded["y"]
    labels = df_encoded["y"].unique()
    scaler = StandardScaler()
    X_scale = scaler.fit_transform(X)

    X_train,X_test,Y_train,Y_test = train_test_split(X_scale,Y,test_size=0.2,random_state=42)

    #model - Logistic regression
    model_1 = LogisticRegression()

    model_1.fit(X_train,Y_train)

    y_pred = model_1.predict(X_test)

    Accuracy_1 = accuracy_score(Y_test,y_pred)

    cls_report_1 = classification_report(Y_test,y_pred)

    conf_mat_1 = confusion_matrix(Y_test,y_pred)

    y_score = model_1.predict_proba(X_test)[:, 1] #probabilites for class 1(positive)

    roc_auc_score_1 = roc_auc_score(Y_test,y_score)#Area under ROC-AUC curve

    fpr_1,tpr_1,thresholds_1 = roc_curve(Y_test,y_score)

    roc_auc_1 = auc(fpr_1,tpr_1)

    #model 2- KNN
    accuracy_scores = []
    k_range = range(1,18)

    for k in k_range:

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train,Y_train)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test,y_pred)

        accuracy_scores.append(accuracy)

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]

    print(f"Best value of k is: {best_k}")

    model_2 = KNeighborsClassifier(n_neighbors=best_k)

    model_2.fit(X_train,Y_train)

    y_pred = model_2.predict(X_test)

    Accuracy_2 = accuracy_score(Y_test,y_pred)

    cls_report_2 = classification_report(Y_test,y_pred)

    conf_mat_2 = confusion_matrix(Y_test,y_pred)

    y_score = model_2.predict_proba(X_test)[:, 1] #probabilites for class 1(positive)

    roc_auc_score_2 = roc_auc_score(Y_test,y_score)#Area under ROC-AUC curve

    fpr_2,tpr_2,thresholds_2 = roc_curve(Y_test,y_score)

    roc_auc_2 = auc(fpr_2,tpr_2)


    #plotting elbow method graph
    plt.figure(figsize = (8,5))
    plt.plot(k_range,accuracy_scores,marker = 'o',linestyle = '--')
    plt.title("Accuracy vs k-value")
    plt.xlabel("value of k")
    plt.ylabel("accuracy")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    # Random forest

    model_3 = RandomForestClassifier(n_estimators=150,max_depth=7,random_state=42)

    model_3.fit(X_train,Y_train)

    y_pred = model.predict(X_test)

    Accuracy_3 = accuracy_score(Y_test,y_pred)

    cls_report_3 = classification_report(Y_test,y_pred)

    conf_mat_3 = confusion_matrix(Y_test,y_pred)

    y_score = model_3.predict_proba(X_test)[:, 1] #probabilites for class 1(positive)

    roc_auc_score_3 = roc_auc_score(Y_test,y_score)#Area under ROC-AUC curve

    fpr_3,tpr_3,thresholds_3 = roc_curve(Y_test,y_score)

    roc_auc_3 = auc(fpr_3,tpr_3)

    #checking feature importance
    importance = pd.Series(model_3.feature_importances_,index = X.columns)
    importance = importance.sort_values(ascending = False)
    #plotting feature importance
    importance.plot(kind = 'bar',figsize = (10,6),title = 'Feature importance')
    plt.show()

    #plotting pre-requisities
    models = [model_1,model_2,model_3]

    Accuracy = [Accuracy_1,Accuracy_2,Accuracy_3]

    Cls_Report = [cls_report_1,cls_report_2,cls_report_3]

    ROC_AUC = [roc_auc_score_1,roc_auc_score_2,roc_auc_score_3]

    Conf_Mat = [conf_mat_1,conf_mat_2,conf_mat_3]

    fpr  = [fpr_1,fpr_2,fpr_3]

    tpr = [tpr_1,tpr_2,tpr_3]
    
    roc_auc = [roc_auc_1,roc_auc_2,roc_auc_3]


    print("------STATSTICAL ANALYSIS FOR EACH MODEL IS AS FOLLOWS-------------")
    #accuracy score,ROC-AUC score,classification report,confusion matrix
    for i in range(3):
        print("-"*70)
        print(f"The {models[i]} has: ")
        print(f"Accuracy score: {Accuracy[i]}")
        print(f"ROC-AUC score: {ROC_AUC[i]}")
        print(f"classification report: \n{Cls_Report[i]}")  
        print(f"Confusion Matrix: \n{Conf_Mat[i]}")
        print("-"*70)
    
    #displaying confusion matrix model wise
    for i in range(3):
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
        plt.title("ROC curve for Bank term deposit subcription classification")
        plt.legend()
        plt.show()

    # All in one model ROC-AUC curve
    plt.figure(figsize=(8,6))
    for i in range(3):
        plt.plot(fpr[i],tpr[i],label = f"Model {i+1} (AUC = {roc_auc[i]:.2f}")
    plt.plot([0,1],[0,1],'k--',label = 'Random Guess')
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.05])
    plt.xlabel("False positive Rate")
    plt.ylabel("True positive Rate")
    plt.title("ROC curve for Bank term deposit subcription classification")
    plt.legend()
    plt.show()

 
def main():
    data_path = "bank-full.csv"

    Bank_Marketing(data_path)


if __name__ == "__main__":
    main()