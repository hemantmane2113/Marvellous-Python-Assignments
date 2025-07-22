import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)
    print("The dataframe is as follows")
    print(df)

    print("The updated dataframe is as follows")
    df_updated = df.drop(columns='English')# returns updated df,keeping original entact
    #df.drop(columns = 'English',inplace = True)->will replace orignal data frame
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