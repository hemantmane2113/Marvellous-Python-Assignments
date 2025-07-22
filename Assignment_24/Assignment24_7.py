import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    gender_data = {"Amit":"Male","Sagar":"Male","Pooja":"Female"}

    df.insert(1,"Gender",df["Name"].map(gender_data))
    #df.insert(position,new_col_name,mapping_column.map(dict))

    print(df)

    df["Total"] = df[['Math','Science','English']].sum(axis = 1)
    
    df.loc[df['Total'] >= 250,"Status"]= "Pass"
    df.loc[df['Total'] < 250,"Status"]= "Fail"

    print(df)

    df.to_csv('students_data.csv', index=False)


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