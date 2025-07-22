import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    Gender = ["Male","Male","Female"]

    df["Gender"] = Gender

    df_grouped = df.groupby("Gender")[["Math","Science","English"]].mean()

    #alternative way
    #df_grouped = df[["Gender", "Math", "Science", "English"]].groupby("Gender").mean()


    print(df_grouped)

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