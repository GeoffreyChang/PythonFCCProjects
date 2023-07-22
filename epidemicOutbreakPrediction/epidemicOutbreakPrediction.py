import pandas as pd


def data_preprocessing():
    df = pd.read_csv("covid-case-counts.csv")
    # Check for missing data
    print(df.isnull().sum())
    # I notice that "Overseas travel" has a large number of missing values.
    # Given the nature of the column, it can be infered that a missing value means "No"

    # Fill missing data with "No"
    df['Overseas travel'].fillna('No', inplace=True)
    # Check for missing data
    print(df.isnull().sum())
    # No more missing data

    # Check the data types
    print(df.dtypes)
    # "Report Date" col is type object, convert to datetime type
    df['Report Date'] = pd.to_datetime(df['Report Date'])
    # "Case Status", "Sex", "Age group", "District", "Overseas travel" and "Infection Status" are categorical.
    # perform one-hot encoding
    df_encoded = pd.get_dummies(df, columns=['Case Status', 'Sex', 'Age group', 'District', 'Overseas travel',
                                             'Infection status'])
    


if __name__ == "__main__":
    data_preprocessing()