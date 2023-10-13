from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib
import numpy as np
import pickle

# Assuming you have X and Y as your data and labels
# Load your CSV file into a pandas DataFrame
df = pd.read_csv('final_training_data.csv')

# Extract features and labels
y = df['attack']
X = df.drop(columns=['attack'])  # Drop the 'class_name' column to get features

# Split the data into training and testing sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)


# Create a Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=1)


# Train the Random Forest model
rf_classifier.fit(X_train, y_train)

# Make predictions on the Validation set
Y_pred = rf_classifier.predict(X_val)

# Evaluate the model
accuracy = accuracy_score(y_val, Y_pred)
print("Accuracy:", accuracy)

model_params = rf_classifier.get_params()

with open('model_params.pkl', 'wb') as file:
    pickle.dump(model_params, file)

# Access the feature names
feature_names = rf_classifier.feature_names_in_
array_with_strings = feature_names.astype(np.str_)

# Add a string to the array
string_to_add = 'attack'
array_with_strings = np.append(array_with_strings, 'attack')

#print("Feature Names:", array_with_strings)

# You can also print a classification report for more detailed metrics
print(classification_report(y_val, Y_pred, digits=10))


# Create a dictionary to store both feature names and the model
data_to_save = {
    'feature_names': array_with_strings,
    'model': rf_classifier
}

# Save the dictionary using joblib
joblib.dump(data_to_save, 'model_and_feature_names.joblib')