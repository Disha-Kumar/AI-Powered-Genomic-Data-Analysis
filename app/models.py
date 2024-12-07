import numpy as np

def recommend_treatment(sequence, model, vectorizer, lb):
    X_sequence = vectorizer.transform([sequence])
    prediction = model.predict(X_sequence.toarray())
    predicted_disorder = lb.inverse_transform(prediction)[0]
    treatment_plan = f"Recommended treatment plan for {predicted_disorder}"
    return treatment_plan
