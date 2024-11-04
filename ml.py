from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib
import numpy as np

# Sample dataset: features = questions, target = Ikigai area
data = {
    'motivation': ['Helping others', 'Achieving success', 'Creative expression', 'Learning new things', 'Solving problems', 'Exploring the world'],
    'skill': ['Communication', 'Analytical thinking', 'Leadership', 'Craftsmanship', 'Empathy', 'Creativity'],
    'environment': ['A structured and organized setting', 'A fast-paced, challenging workplace', 'A creative and artistic space', 'A supportive and collaborative team', 'A flexible and independent work style', 'An outdoor, nature-oriented environment'],
    'impact': ['Making a difference', 'Innovating new technologies', 'Promoting equality and justice', 'Fostering education and knowledge', 'Protecting the environment', 'Creating beauty or art'],
    'known_for': ['Empathy', 'Creativity', 'Knowledge and expertise', 'Leadership and influence', 'Contributions to society', 'Adventurous spirit'],
    'ikigai': ['Social Worker', 'Engineer', 'Artist', 'Educator', 'Environmentalist', 'Leader']
}

df = pd.DataFrame(data)

# Features and target variable
X = df[['motivation', 'skill', 'environment', 'impact', 'known_for']]
y = df['ikigai']

# Converting categorical data to numerical (one-hot encoding)
X_encoded = pd.get_dummies(X)

# Train the model
model = RandomForestClassifier()
model.fit(X_encoded, y)

# Export the model to a file
joblib.dump(model, 'ikigai_model.pkl')
