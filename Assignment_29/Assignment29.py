import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix




def Diabetes(data_path):
    
#Exploratory data analysis(EDA)

    #1.Load the dataset using pandas
    df = pd.read_csv(data_path)

    print(df)
    #2.Display the first 5 rows
    print(df.head())

    #3.Show column info and check for null values

    print(df.info())

    #4.Display basic statistics using .describe()

    print(df.describe())

    #5.Plot the distribution of the target varible(Outcome)

    sns.countplot(x=df["Outcome"], data=df)
    plt.xticks([0, 1])  
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('Distribution of Binary Values')
    plt.show()

    #6.Use graphs like hist,boxplot or parplot to identify patterns and outliers

    sns.pairplot(df)
    plt.show()

    #boxplot
    df_melted = df.melt(id_vars='Outcome', 
                    value_vars=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'],
                    var_name='Feature', 
                    value_name='Value')
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Feature', y='Value', hue='Outcome', data=df_melted)
    plt.title('Distribution of Features Grouped by Diabetes Outcome')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    #2. Data Preprocessing
    #check and handle missing or zero values in columns like Glucose,BloodPressure,etc

    print((df == 0).sum())# number of zeroes in each column
    print((df == 0).sum().sum())#totoal number of zeroes in whole dataframe(will include zeroes 
    # #of 'outcome' column as well,but mind you it is a categorical value)

    print(df.isnull().sum())

    feature_only_df = df.drop(columns = 'Outcome')#to drop categorical column
    print(feature_only_df)

    feature_only_df = feature_only_df.apply(lambda x: x.replace(0, x[x != 0].mean()))#removing 0s

    df['Outcome'] = df['Outcome']

    df.update(feature_only_df)

    print((feature_only_df == 0).sum())

    df_final = pd.concat([feature_only_df,df['Outcome']],axis = 1)

    
    #Apply feature scaling using StandardScalar or MinMaxScaler
    #Split the dataset into features(X) and target(y)

    x = feature_only_df
    y = df["Outcome"]

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x_scale,y,test_size= 0.2,random_state=42)

    #3.Model Building
    #Train at least 2 different algorithms on the dataset

    #Logistic Regression

    model_1 = LogisticRegression()
    model_1.fit(x_train,y_train)

    y_pred = model_1.predict(x_test)

    accuracy_1 = accuracy_score(y_test,y_pred)

    conf_mat_1 = confusion_matrix(y_test,y_pred)
    report_1 = classification_report(y_test,y_pred)

    #K-Nearest Neighbours

    accuracy_scores = []
    k_range = range(1,18)

    for k in k_range:

        model = KNeighborsClassifier(n_neighbors=k)#default = 5

        model.fit(x_train,y_train)

        y_pred = model.predict(x_test)

        accuracy = accuracy_score(y_test,y_pred)

        accuracy_scores.append(accuracy)

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of k is: ",best_k)


    model_2 = KNeighborsClassifier(best_k)
    model_2.fit(x_train,y_train)

    y_pred = model_2.predict(x_test)

    accuracy_2 = accuracy_score(y_test,y_pred)

    conf_mat_2 = confusion_matrix(y_test,y_pred)
    report_2 = classification_report(y_test,y_pred)

    #Decision tree

    model_3 = KNeighborsClassifier()
    model_3.fit(x_train,y_train)

    y_pred = model_3.predict(x_test)

    accuracy_3 = accuracy_score(y_test,y_pred)

    conf_mat_3 = confusion_matrix(y_test,y_pred)
    report_3 = classification_report(y_test,y_pred)

    models = ['Logistic Regression', 'K-Nearest Neighbors', 'Decision Tree']
    accuracies = [accuracy_1, accuracy_2, accuracy_3]
    reports = [report_1, report_2, report_3]
    
    for i in range(3):
        print("-" * 60)
        print(f"Model: {models[i]}")
        print(f"Accuracy score is: {accuracies[i]}")
        print("Classification Report: ")
        print(f"{reports[i]}")
        print("-" * 60)


    #5Final Output
    #Predict whether a patient is diabetic based on a test data

    print(y_pred,y_test)
    
    Prev_vs_actual_data = {
              "Actual_label":y_test,
              "Prediction_label":y_pred
              
    }
    result_df = pd.DataFrame(Prev_vs_actual_data)

    print("The predictions for test data vs actual labels are as given below: ")
    print(result_df)

    # Save to CSV
    
    result_df.to_csv('Predictions_vs_Actual_Output.csv', index=False)



def main():

    data = "diabetes.csv"

    Diabetes(data)


if __name__ == "__main__":
    main()