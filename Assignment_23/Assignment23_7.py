import pandas as pd
import matplotlib.pyplot as plt

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print("The original dataframe is: ")
    print(df)

    df['Total']  = df[['Math','Science','English']].sum(axis = 1)#axis = 1 -> horizontal
    print(df)

    plt.bar(df["Name"],df['Total'])
    plt.xlabel('Student Name')
    plt.ylabel('Total Marks')
    plt.title('Bar Plot')

    plt.show()

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