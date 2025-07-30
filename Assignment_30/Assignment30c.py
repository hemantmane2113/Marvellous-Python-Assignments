import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder




from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix

from sklearn.neighbors import KNeighborsClassifier

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

    X = df.drop(columns = 'y',axis = 1)  
    Y = df["y"]

    # One hot encoding

    Y = Y.map({'yes': 1, 'no': 0})

    onehot = OneHotEncoder(sparse_output=True, handle_unknown='ignore')
    encoded_data = onehot.fit_transform(X)


    X_train,X_test,Y_train,Y_test = train_test_split(encoded_data,Y,test_size=0.2,random_state=42)



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

    model = KNeighborsClassifier(n_neighbors=best_k)

    model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test,y_pred)

    cls_report = classification_report(Y_test,y_pred)

    y_score = model.predict_proba(X_test)[:, 1] #probabilites for class 1(positive)

    Roc_Auc_Score = roc_auc_score(Y_test,y_score)#Area under ROC-AUC curve


    conf_mat = confusion_matrix(Y_test,y_pred)

    print("Accuracy is :",Accuracy)
    print("Classification report is: \n",cls_report)
    print("ROC-AUC score is : ",Roc_Auc_Score)
    print("Confusion Matrix is: \n",conf_mat)
    
def main():
    data_path = "bank-full.csv"

    Bank_Marketing(data_path)


if __name__ == "__main__":
    main()


    """
         Model	                                Recommended Encoding

    Linear/Logistic Reg.	    One-Hot (nominal), Ordinal (for ordered categories)

    KNN                     	         One-Hot (for all), OR Gower Distance
 
    Decision Trees	                      Label Encoding, Target Encoding

    Random Forest	                      Label Encoding, Target Encoding

    XGBoost/LightGBM	           Label Encoding or Target Encoding (handles well)

    SVM	                                         One-Hot Encoding

  Neural Networks	              One-Hot or Embedding Layers (for high-cardinality)
    
    """