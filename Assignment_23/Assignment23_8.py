import pandas as pd
import matplotlib.pyplot as plt

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print("The original dataframe is: ")
    print(df)

    df_subjects = df.columns.drop("Name")# to select required column names
    print(df_subjects)

    df_amit_marks = df.loc[df["Name"] == "Amit",df_subjects].values.flatten()

    
    print(df_amit_marks)

    plt.plot(df_subjects,df_amit_marks)
    plt.xlabel('Subject Name')
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

"""

df_amit_marks = df.loc[df["Name"] == "Amit",df_subjects].values.flatten()

1.[df["Name"] == "Amit"-->returns a  boolean series 

2.df.loc[df["Name"] == "Amit"->select row fulfilling the condition

3.df.loc[df["Name"] == "Amit",df_subjects]--> gives 2D(1,3) data frame
meaning row of just amit along with selected subjects(df.subjects) 

 Math Science English
  x     y         z

4.df.loc[df["Name"] == "Amit",df_subjects].values-> gives just values
 [[x, y, z]] in 2D(1,3)

5.df.loc[df["Name"] == "Amit",df_subjects].values.flatten()->converts it into 1D(3,) array
 [x, y, z]

"""
  

