import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    df = df.rename(columns = {'Math':'Mathematics'})

    print(df)

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

