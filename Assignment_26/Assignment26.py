import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


def PlayPredictor(data_path):

    #step 1: Get Data
    df = pd.read_csv(data_path)

    print("The sample dataset is as follows: \n")
    #print(df)

    #step 2: Clean,Prepare and Manipulate data

    df = df.drop(columns = ["Unnamed: 0"])

    #print(df)

    df["Play"] = df["Play"].replace({"Yes": 1,"No":0})

    df = pd.get_dummies(df, drop_first=True)

    #print(df)

    #step 3:train data

    x= df.drop(columns = "Play")

    y = df["Play"]

    #print(x)
    #print(y)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.2,random_state=42)

    #for k = 3
    model = KNeighborsClassifier(n_neighbors=3)#default = 5

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)
    cm = confusion_matrix(y_test,y_pred)

    print("Accuracy for k = 3 is :",accuracy*100)
    print("Confusion matrix for k = 3: ")
    print(cm)

    #Tesing accuracy for different values of k
    accuracy_scores = []
    k_range = range(1,18)

    for k in k_range:

        model = KNeighborsClassifier(n_neighbors=k)#default = 5

        model.fit(x_train,y_train)

        y_pred = model.predict(x_test)

        accuracy = accuracy_score(y_test,y_pred)

        accuracy_scores.append(accuracy)

    plt.figure(figsize = (8,5))
    plt.plot(k_range,accuracy_scores,marker = 'o',linestyle = '--')
    plt.title("Accuracy vs k-value")
    plt.xlabel("value of k")
    plt.ylabel("accuracy")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of k is: ",best_k)

    model = KNeighborsClassifier(n_neighbors=best_k)

    model.fit(x_train,y_train)

    #step 4: Test data
    y_pred = model.predict(x_test)
    
    #step 5:Caculate accuracy
    accuracy = accuracy_score(y_test,y_pred)
    cm = confusion_matrix(y_test,y_pred)

    print(f"Accuracy for best value of k = {best_k} is :",accuracy*100)
    print(f"Confusion matrix for best value of k = {best_k} is: ")
    print(cm)

def main():

    datapath = "PlayPredictor.csv"

    PlayPredictor(datapath)

if __name__ == "__main__":
    main()

"""
 we could use .replace for the other columns(weather,temperature) as well but here is the catch

1.KNN interprets numeric closeness literally (e.g., Rainy=2 is "closer" to Overcast=1 than
 to Sunny=0)

If there’s no natural order, this can introduce bias in distance-based models like KNN

"""

