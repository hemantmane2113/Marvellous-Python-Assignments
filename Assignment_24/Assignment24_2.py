import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)
    # creating column Gender
    Gender = ["Male","Male","Female"]

    df["Gender"] = Gender

    #alternative way
    #Gender = {"Amit":"Male","Sagar":"Male","Pooja":"Female"}

    #df["Gender"] = df["Name"].map(Gender)

    #one hot encoding
    df["Gender"] = df["Gender"].replace({"Male":1,'Female': 0})

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


 