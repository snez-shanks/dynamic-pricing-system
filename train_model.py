import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
data = pd.read_csv("dataset/pricing_data.csv")

# Define input features
X = data[['demand','competitor_price','stock','rating','season','discount']]

# Target variable
y = data['price']

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create machine learning model
model = RandomForestRegressor()

# Train the model
model.fit(X_train, y_train)

# Save trained model
pickle.dump(model, open("model/pricing_model.pkl", "wb"))

print("Model trained and saved successfully!")