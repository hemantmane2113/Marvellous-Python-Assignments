import pandas as pd
import numpy as np
import random

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print(df)

    df = df.sample(frac = 1,random_state=42).reset_index(drop = True)
    #frac-how much to resuffle,random_state = 42-the shuffle will be same every time,
    # reset_index = resets the index,drop = true->drop the old index

    split_ratio = 0.7

    split_index = int(len(df)*split_ratio)

    train_data = df[:split_index]

    test_data = df[split_index:]

    x_train = train_data[["Age","Salary"]]
    y_train = train_data["Purchased"]
    x_test = test_data[["Age","Salary"]]
    y_test = test_data["Purchased"]

    print("The training features are: \n")
    print(x_train)

    print("The training labels are: \n")
    print(y_train)

    print("The testing features are: \n")
    print(x_test)

    print("The testing labels are: \n")
    print(y_test)


def main():
    
    data = {"Age":[25,30,45,35,22],"Salary":[50000,60000,80000,65000,45000],"Purchased":[1,0,1,0,1]}
    Data_Frame(data)



if __name__ == "__main__":
    main()