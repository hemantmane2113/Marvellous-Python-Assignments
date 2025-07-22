import pandas as pd
import numpy as np

def dataframe(data_set):

    df =pd.DataFrame(data_set)

    print("The dataframe is :")
    print(df)

    #df['Math'].fillna(df['Math'].mean(),inplace = True)
    #df['Science'].fillna(df['Science'].mean(),inplace = True)

    df.fillna({'Science': df['Science'].mean(),
               'Math': df['Math'].mean()}, 
               inplace=True)# as told by pandas-see below comments

    print("The updated dataframe is :")

    print(df)
    
def main():

    data  = {
        "Name" :["Amit","Sagar","Pooja"],
        "Math" : [np.nan,76,88],
        "Science":[91,np.nan,85]
        
    }

    dataframe(data)

if __name__ == "__main__":
    main()

    """
    inplace()
    #Optional, default False. 
    #If True: the replacing is done on the current DataFrame. If False: returns a copy where the replacing is done.
    print(df)


    when inplace  = False,new df is returned,so there should be a variable(column) to accept the 
    returned value

    df['Math'] = df['Math'].fillna(df['Math'].mean(),inplace = False)
    df['Math'].fillna(df['Math'].mean(),inplace = False) will give new column which is be named
    "Math
    
    if inplace = True,no new df is returned,changes are made in current df only
    df['Math'] = df['Math'].fillna(df['Math'].mean(),inplace = True) is COMPLETELY WRONG

    the correct way is 
    df['Math'].fillna(df['Math'].mean(),inplace = True)

    """

    """
    FutureWarning: A value is trying to be set on a copy of a DataFrame or Series 
    through chained assignment using an inplace method.
    The behavior will change in pandas 3.0. This inplace method will never work 
    because the intermediate object on which we are setting values always behaves as a copy.

    For example, when doing 'df[col].method(value, inplace=True)', 
    try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) 
    instead, to perform the operation inplace on the original object.

      df['Math'].fillna(df['Math'].mean(),inplace = True)
      df['Science'].fillna(df['Science'].mean(),inplace = True)

    """