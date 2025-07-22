import pandas as pd

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print(df)

    Math_Max = df['Math'].max()
    Math_Min = df['Math'].min()
    print(Math_Max)
    print(Math_Min)
    
    df['Math_Scaled'] = ((df['Math'] - Math_Min)/(Math_Max - Math_Min))

    print(df[['Math','Math_Scaled']])

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
    Inbuilt methods
    1.

    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    df['Math_scaled'] = scaler.fit_transform(df[['Math']])

    2.
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    df['Math_standardized'] = scaler.fit_transform(df[['Math']])



    📝 Summary of Use Cases:
    Method	             Output Range	          Good For
    MinMaxScaler	       0 to 1	         Algorithms like KNN, Neural Networks
    StandardScaler	  Mean = 0, SD = 1	     Most ML models (linear regression, etc.)
    Manual formula	       Custom	         Quick use, simple normalization

    
    """