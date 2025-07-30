import pandas as pd
import numpy as np
import gower
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from sklearn.neighbors import NearestNeighbors
from collections import Counter

def Bank_Marketing(dataset):
    df = pd.read_csv(dataset, sep=';')

    # Show initial info
    print(df.head())
    print(df.info())

    # Replace 'unknown' with NaN and count
    df.replace('unknown', np.nan, inplace=True)
    print("Missing values:\n", df.isna().sum())

    # Drop less useful columns
    df.drop(columns=["day", "month", "contact", "poutcome"], inplace=True)

    # Replace missing with 'other'
    df.fillna('other', inplace=True)

    # Separate features and label
    X = df.drop(columns='y')
    y = df['y']

    # Encode target to binary
    Y = y.map({'yes': 1, 'no': 0})

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Compute Gower distances
    gower_train = gower.gower_matrix(X_train)
    gower_test = gower.gower_matrix(X_test, X_train)

    # Use Nearest Neighbors with Gower distance
    k = 5  # Try different k values later
    model = NearestNeighbors(n_neighbors=k, metric='precomputed')
    model.fit(np.zeros((X_train.shape[0], X_train.shape[0])))  # dummy data
    distances, indices = model.kneighbors(gower_test)

    # Predict using majority vote
    y_pred = []
    for neighbors in indices:
        neighbor_labels = y_train.iloc[neighbors]
        most_common = Counter(neighbor_labels).most_common(1)[0][0]
        y_pred.append(most_common)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    cls_report = classification_report(y_test, y_pred)
    y_score = model.predict_proba(X_test)[:, 1] #probabilites for class 1(positive)
    Roc_Auc_Score = roc_auc_score(y_test,y_score)#Area under ROC-AUC curve
    conf_mat = confusion_matrix(y_test, y_pred)

    print("Accuracy:", accuracy)
    print("Classification Report:\n", cls_report)
    print("ROC AUC Score:", Roc_Auc_Score)
    print("Confusion Matrix:\n", conf_mat)


def main():
    data_path = "bank-full.csv"
    Bank_Marketing(data_path)


if __name__ == "__main__":
    main()
