import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print("The original dataframe is: ")
    print(df)

    df['Total']  = df[['Math','Science','English']].sum(axis = 1)#axis = 1 -> horizontal
    print(df)
    print("The updated dataframe is: ")
    df_updated = df.sort_values(by="Total",ascending=False)#->to get whole data frame
    #df_updated = df["Total"].sort_values(ascending=False)->to get that single column

    print(df_updated)

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