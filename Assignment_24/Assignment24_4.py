import pandas as pd
import matplotlib.pyplot as plt



def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    sagar_row = df[df["Name"] == "Sagar"]

    subject_marks = sagar_row[['Math','Science','English']].values.flatten()

    label = ["Math","Science","English"]

    plt.pie(subject_marks,labels = label,autopct='%1.1f%%', startangle=90)

    plt.axis('equal')

    plt.title("Sagar Marks distribution")

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