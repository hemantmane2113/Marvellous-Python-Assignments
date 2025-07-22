import pandas as pd
import numpy as np

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print(df)

    df_min = df["Age"].min()
    df_max = df["Age"].max()

    df["Age_scaled"] = ((df["Age"] - df_min)/(df_max - df_min))

    print(df[["Age","Age_scaled"]])


def main():
    
    data = {"Age":[18,22,25,30,35]}
    Data_Frame(data)



if __name__ == "__main__":
    main()