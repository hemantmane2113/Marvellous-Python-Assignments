import pandas as pd
import numpy as np

def Data_Frame(DataSet):

    df = pd.DataFrame(DataSet)

    print(df)

    sort_data = np.sort(df["Salary"])#gives numpy array
    #sort_data = df["Salary"].sort_values().values gives pandas dataframe 

    print(sort_data)

    data_array = sort_data.flatten()# we are not using xxx.values.yyyy because its already a numpy array
    #.values-numpy array,.flatten-1D numpy array
    # data_array is already a 1D numpy array
    print(data_array)

    # Calculating Q1,Q2 and Q3

    Q1 = np.percentile(sort_data,25,method = 'midpoint')
    Q2 = np.percentile(sort_data,50,method = 'midpoint')
    Q3 = np.percentile(sort_data,75,method = 'midpoint')

    print("Q1 25 percentile of given data is ",Q1)
    print("Q2 50 percentile of given data is ",Q2)
    print("Q3 75 percentile of given data is ",Q3)

    IQR = Q3 - Q1
    print("Interquartile range is ",IQR)

    #Outlier detection

    Lower_Bound = Q1 - 1.5 * IQR

    Upper_Bound = Q3 + 1.5 * IQR

    print(Lower_Bound,Upper_Bound)
    #The value below lower_bound or value above considered is an outlier

    outlier = []
    
    for data in data_array:
        if data < Lower_Bound or data  > Upper_Bound:
            outlier.append(data)

    return outlier


def main():
    
    data = {"Salary":[25000,27000,29000,31000,50000,100000]}

    iRet = Data_Frame(data)

    print("The outlier values in the dataset are: ")
    for i in iRet:
        print(i)


if __name__ == "__main__":
    main()