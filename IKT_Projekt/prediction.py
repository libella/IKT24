import joblib
def predict(data):
    model = joblib.load("spam_model.joblib")
    return model.predict(data)

