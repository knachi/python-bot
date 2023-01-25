# Code you have previously used to load data
import pandas as pd
from sklearn import preprocessing
from sklearn.tree import DecisionTreeRegressor


def convert(data):
    number = preprocessing.LabelEncoder()
    data['tag'] = number.fit_transform(data.tag)
    data['patterns'] = number.fit_transform(data.patterns)
    data['response'] = number.fit_transform(data.response)
    data = data.fillna(-999)
    return data, number


# Path of the file to read
iowa_file_path = 'resources/train.csv'

home_data, number = convert(pd.read_csv(iowa_file_path))

# print the list of columns in the dataset to find the name of the prediction target
print(home_data.columns)

# Prediction target
y = home_data.response

# Predictive features (Deciding parameters)
feature_names = ['tag', 'patterns']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Review data
# print description or statistics from X
# print(X.describe())

# print the top few lines
print("X-head", X.head())

iowa_model = DecisionTreeRegressor(random_state=1)

le = preprocessing.LabelEncoder()

# Fit the model
iowa_model.fit(X, le.fit_transform(y))

print("after fitting")

predictions = iowa_model.predict(X.head())
print("Predictions are:" , predictions)

ip = []
for i in predictions:
    ip.append(int(i))

print(number.inverse_transform(ip))

