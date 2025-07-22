import pandas as pd
import matplotlib.pyplot as plt

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    math_marks = df['Math'].values.flatten()
    print(math_marks)

    names = df["Name"].values.flatten()
    print(names)

    plt.bar(names, math_marks, color='skyblue')
    plt.title("Math Marks of Students")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.show()

    df.hist(column="Math")
    plt.title('Histogram of math marks')
    plt.xlabel('marks')
    plt.ylabel('Frequency')
    plt.show()

    #  wanted to know the differnce between histogram and bar plot

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

