import pandas as pd
import numpy as np

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print(df)

    df["Grade"] = df["Grade"].replace({"A+":"Excellent","A":"Good","B+":"Good","B":"Average","C":"Poor"})

    print(df)


def main():
    
    data = {"Grade":["A+","B","A","C","B+"]}
    Data_Frame(data)



if __name__ == "__main__":
    main()