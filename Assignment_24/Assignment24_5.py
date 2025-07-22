import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    df["Total"] = df[['Math','Science','English']].sum(axis = 1)# axis = 1,sum across rows(horizontal) for each row (i.e., for each student)
    #axis = 0(vertical),will give total marks per subject
    df.loc[df['Total'] >= 250,"Status"]= "Pass"
    df.loc[df['Total'] < 250,"Status"]= "Fail"

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