import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    #df['Total'] = df['Math']+df['Science']+df["English"]
    df['Total']  = df[['Math','Science','English']].sum(axis = 1)#axis = 1 -> horizontal

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
