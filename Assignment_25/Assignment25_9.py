import pandas as pd
import numpy as np

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print(df)

    df["Marks"] = df["Marks"].where(df["Marks"] < 50,"Fail")

    print(df)
    
def main():
    
    data = {"Marks":[45,67,88,32,76]}
    Data_Frame(data)

if __name__ == "__main__":
    main()