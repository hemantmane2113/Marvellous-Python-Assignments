import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    print("Shape of the data is :",df.shape)
    print("Info of columns: ",df.columns)
    print("Data type is : ",df.dtypes)

def main():

    data  = {
        "Name" :["Amit","Sagar","Pooja"],
        "Math" : [85,90,72],
        "Science":[92,88,90],
        "English":[75,85,82]
    }

    dataframe(data)

if __name__ == "__main__":
    main()