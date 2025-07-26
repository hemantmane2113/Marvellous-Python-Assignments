import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def WinePredictor(DataPath):
    #step 1: Get the data
    df = pd.read_csv(DataPath)
    
    #step 2: Clean,prepare and manipulate the data
    df.dropna(inplace = True)

    x = df.drop(columns = ["Class"])
    y = df['Class']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)
    x_train,x_test,y_train,y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)

    #Analyse the data

    corr_matrix = df.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

    #step 3: Train the data

    # for k = 5
    model = KNeighborsClassifier()#default = 5

    model.fit(x_train,y_train)

    #step 4: Test the data
    y_pred = model.predict(x_test)

    #step 5: Calculate accuracy
    accuracy = accuracy_score(y_test,y_pred)
    cm = confusion_matrix(y_test,y_pred)

    print("Accuracy of the model for k = 5 is :",accuracy*100)
    print("Confusion matrix of the model for k = 5 is: \n",cm)
    print("The classification report for k = 5 is as follows: ")
    print(classification_report(y_test, y_pred))

    #calculating best value of k
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

    model = KNeighborsClassifier(n_neighbors=best_k)#default = 5

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)
    cm = confusion_matrix(y_test,y_pred)

    print(f"Accuracy of model when best value of k = {best_k} is :",accuracy*100)
    print(f"Confusion matrix of the model for best of k = {best_k} is: \n",cm)
    print("The classification report for k = 5 is as follows: ")
    print(classification_report(y_test, y_pred))

def main():

    data = "WinePredictor.csv"
    WinePredictor(data)

if __name__ == "__main__":
    main()