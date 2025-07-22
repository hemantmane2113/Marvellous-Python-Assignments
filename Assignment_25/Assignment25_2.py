import pandas as pd
import numpy as np

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print("Original dtypes:\n", df.dtypes)

    df["Age"] = df["Age"].astype(int)

    print("New dtypes:\n", df.dtypes)

def main():
    
    data = {"Name":["A","B","C"],"Age":[21.0,22.0,23.0]}
    Data_Frame(data)



if __name__ == "__main__":
    main()