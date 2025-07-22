import pandas as pd
import numpy as np

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print("original Dataframe")
    print(df)

    df = df.interpolate()
    print("Dataframe after interpation")
    print(df)
    

def main():
    
    data = {"Marks":[85,np.nan,90,np.nan,95]}
    Data_Frame(data)

if __name__ == "__main__":
    main()