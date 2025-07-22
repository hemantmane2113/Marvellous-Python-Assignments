import pandas as pd
import numpy as np

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print(df)

    #one hot encoding
    df["Department"] = df["Department"].replace({"HR":0,"I.T.":1,"Finance":2})

    print(df)


def main():
    
    data = {"Department":["HR","I.T.","Finance","HR","I.T."]}
    Data_Frame(data)



if __name__ == "__main__":
    main()