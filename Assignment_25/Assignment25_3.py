import pandas as pd
import numpy as np

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print(df)

    #one hot encoding
    df["City"] = df["City"].replace({"Pune":0,"Mumbai":1,"Delhi":2})

    print(df)


def main():
    
    data = {"City":["Pune","Mumbai","Delhi","Pune","Delhi"]}
    Data_Frame(data)



if __name__ == "__main__":
    main()