import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score

def Advertising(data_path):

    #step 1: Get Data
    df = pd.read_csv(data_path)

    print("The sample dataset is as follows: \n")
    #print(df)

    #step 2: Clean,Prepare and Manipulate data

    df = df.drop(columns = ["Unnamed: 0"])

    print(df)

    #to look for null values
    print(df.isnull().sum())

    #step 3:Train the model

    x = df.drop(columns = "sales")
    y = df["sales"]

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 ,random_state = 42 )

    #step 4: Test the data
    model = LinearRegression()

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    #step 5: Check the accuracy of the model
    mae = mean_absolute_error(y_test,y_pred)
    mse = mean_squared_error(y_test,y_pred)
    rmse = root_mean_squared_error(y_test,y_pred)
    #rmse2 = np.sqrt(mse)
    r2 = r2_score(y_test,y_pred)

    print('Mean absolute error is: ',mae)
    print('Mean squared error is: ',mse)
    print('Root mean squared error is: ',rmse)
    #print(rmse2)
    print('R2 score(coefficient of determination) is: ',r2)

    # Plotting actual vs predicted values

    x = [y_test.min(), y_test.max()]# will be a x-axis values

    y = [y_test.min(), y_test.max()]#  will be a y_axis values

    #this done to plot a perfect prediction line where x = y

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, color='blue', edgecolor='k')
    plt.plot(x,y, color='red', linestyle='--')
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual vs Predicted Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():

    datapath = "Advertising.csv"

    Advertising(datapath)

if __name__ == "__main__":
    main()
