# model_utils.py

import joblib

# Load once (important for performance)
pipeline = joblib.load("career_pipeline.pkl")
le = joblib.load("label_encoder.pkl")


def predict_top_roles(user_input):
    """
    Takes user input (text) and returns top 3 predicted roles
    """
    
    # Get probabilities
    probs = pipeline.predict_proba([user_input])
    
    # Get top 3 indices
    top_3 = probs[0].argsort()[-3:][::-1]
    
    # Convert to role names
    roles = le.inverse_transform(top_3)
    
    return roles