import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    print("The descriptive statistics of the datafram is as follows:")

    print(df.describe())

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