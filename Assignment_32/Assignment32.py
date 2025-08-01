import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
from sklearn.metrics import roc_auc_score,auc,roc_curve

from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression




def Fake_News_Prediction(DataSet1_Path,DataSet2_Path):

    df1 = pd.read_csv(DataSet1_Path)
    #print(df1.shape)
    

    df2 = pd.read_csv(DataSet2_Path)
    #print(df2.shape)

    #last_column_name2 = df1.columns[-1]
    #print(last_column_name2)

    # Inserting column 'Label' to both data frames
    df1.insert(4, 'Label', 0)
    #print(df1.shape)
    #print(df1.head())

    df2.insert(4, 'Label', 1)
    #print(df2.shape)
    #print(df2.head())


    df= pd.concat([df1,df2], ignore_index=True)#by default axis = 0(combine dfs one below the other)

    #print(df.shape)
    #print(list(df))

    #print(df.info())
    #print(df.head())

    #print(df.tail())

    #pd.set_option('display.max_colwidth', None)

    #print(list(df))#gives list of header columns or you one can use: list(my_dataframe.columns.values)

    #df.to_csv('clean_output.csv', index=False)

    df["Text"] = df["title"].str.cat(df["text"],sep = " ")
    #can also use df["Text"] = df["title"] + df["text"],here both columns must be string with no missing values

    df.drop(columns=["title", "text"], inplace=True)
    df.drop(columns=["subject", "date"], inplace=True)

    # Move "Text" to the front (index 0)
    Text_col = df.pop("Text")       # remove and get the column
    df.insert(0, "Text", Text_col)  # insert at position 0

    #print(list(df))
    #print(df.shape)


    #TF-IDF 
    
    corpus = df["Text"]

    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(corpus)

    # View feature names
    #print(vectorizer.get_feature_names_out())

    Y = df["Label"]
    labels = df["Label"].unique()

    

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

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

    model_2 = LogisticRegression()


    model_2.fit(X_train,Y_train)

    y_pred = model_2.predict(X_test)

    Accuracy_2 = accuracy_score(Y_test,y_pred)

    Conf_Mat_2 = confusion_matrix(Y_test,y_pred)

    Cls_rpt_2 = classification_report(Y_test,y_pred)

    y_score = model_2.predict_proba(X_test)[:, 1] #probabilites for class 1(positive)

    roc_auc_score_2 = roc_auc_score(Y_test,y_score)#Area under ROC-AUC curve

    fpr_2,tpr_2,thresholds_2 = roc_curve(Y_test,y_score)

    roc_auc_2 = auc(fpr_2,tpr_2) #Area under ROC-AUC curve


    ensemble_model_1 = VotingClassifier(estimators=[
        ('dt', model_1), 
        ('lr', model_2)
        ], 
        voting='soft')  # Use 'soft' if using probabilities

    ensemble_model_1.fit(X_train, Y_train)

    y_pred = ensemble_model_1.predict(X_test)

    Accuracy_3 = accuracy_score(Y_test,y_pred)

    Conf_Mat_3 = confusion_matrix(Y_test,y_pred)

    Cls_rpt_3 = classification_report(Y_test,y_pred)

    y_score = ensemble_model_1.predict_proba(X_test)[:, 1] #probabilites for class 1(positive)

    roc_auc_score_3 = roc_auc_score(Y_test,y_score)#Area under ROC-AUC curve

    fpr_3,tpr_3,thresholds_3 = roc_curve(Y_test,y_score)

    roc_auc_3 = auc(fpr_3,tpr_3) #Area under ROC-AUC curve


    ensemble_model_2 = VotingClassifier(estimators=[
        ('dt', model_1), 
        ('lr', model_2)
        ], 
        voting='hard')  # Use 'soft' if using probabilities

    ensemble_model_2.fit(X_train, Y_train)

    y_pred = ensemble_model_2.predict(X_test)

    Accuracy_4 = accuracy_score(Y_test,y_pred)

    Conf_Mat_4 = confusion_matrix(Y_test,y_pred)

    Cls_rpt_4 = classification_report(Y_test,y_pred)


    models = [model_1,model_2,ensemble_model_1,ensemble_model_2]

    model_names = ["Decision Tree","Logistic Regression","Voting Classifier(soft-voting)","Voting Classifier(hard-voting)"]

    Accuracy = [Accuracy_1,Accuracy_2,Accuracy_3,Accuracy_4]

    Cls_Report = [Cls_rpt_1,Cls_rpt_2,Cls_rpt_3,Cls_rpt_4]

    ROC_AUC = [roc_auc_score_1,roc_auc_score_2,roc_auc_score_3,]#Area under ROC-AUC curve

    Conf_Mat = [Conf_Mat_1,Conf_Mat_2,Conf_Mat_3,Conf_Mat_4]

    fpr  = [fpr_1,fpr_2,fpr_3,]

    tpr = [tpr_1,tpr_2,tpr_3,]
    
    roc_auc = [roc_auc_1,roc_auc_2,roc_auc_3]#Area under ROC-AUC curve

    thresholds = [thresholds_1,thresholds_2,thresholds_3]

    print("------STATSTICAL ANALYSIS FOR EACH MODEL IS AS FOLLOWS-------------")
    #accuracy score,ROC-AUC score,classification report,confusion matrix
    for i in range(len(models)):
        print("-"*70)
        print(f"The {model_names[i]} has: ")
        print(f"Accuracy score: {Accuracy[i]}")
            # Print ROC-AUC only if available
        if i < len(ROC_AUC):
            print(f"ROC-AUC score: {ROC_AUC[i]}")
        else:
            print("ROC-AUC score: Not Available")
        print(f"classification report: \n{Cls_Report[i]}")  
        print(f"Confusion Matrix: \n{Conf_Mat[i]}")
        print("-"*70)
    
    #displaying confusion matrix model wise
    for i in range(len(models)):
        disp = ConfusionMatrixDisplay(confusion_matrix= Conf_Mat[i],display_labels = labels)
        disp.plot(cmap = plt.cm.Blues)
        plt.title(f"Conusion Matrix for {model_names[i]}")
        plt.show()

    #displaying ROC-AUC curve plot model wise
            
        if i in range(len(roc_auc)): 
            plt.figure(figsize=(8,6))
            plt.plot(fpr[i],tpr[i],label = "ROC curve (area = %0.2f)" % roc_auc[i])
            plt.plot([0,1],[0,1],'k--',label = 'Random Guess')
            plt.xlim([0.0,1.0])
            plt.ylim([0.0,1.05])
            plt.xlabel("False positive Rate")
            plt.ylabel("True positive Rate")
            plt.title(f"ROC curve of {model_names[i]} for Fake News Prediction")
            plt.legend()
            plt.show()
        else:
            print(f"roc-auc plot not available for {model_names[i]}")

    # All in one model ROC-AUC curve
    plt.figure(figsize=(8,6))
    for i in range(len(roc_auc)):
        plt.plot(fpr[i],tpr[i],label = f"{model_names[i]} (AUC = {roc_auc[i]:.2f}")
    plt.plot([0,1],[0,1],'k--',label = 'Random classification')
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.05])
    plt.xlabel("False positive Rate")
    plt.ylabel("True positive Rate")
    plt.title("Combined ROC curve for fake News classification")
    plt.legend()
    plt.show()


def main():
    DataSet1 = "Fake.csv"
    DataSet2 = "True.csv"
    Fake_News_Prediction(DataSet1,DataSet2)


if __name__ == "__main__":
    main()