from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset
iris = load_iris()

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(iris.data, iris.target)

# Save the trained model
joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")