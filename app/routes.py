from flask import Flask, jsonify, request, render_template
from data.collect_data import collect_data
from data.process_data import process_data
from ml.train_model import train_model
from app.models import recommend_treatment
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_treatment', methods=['POST'])
def get_treatment():
    data = request.json
    sequence = data['sequence']
    
    df = collect_data()
    X, y, vectorizer = process_data(df)
    model, lb = train_model(X, y)
    treatment_plan = recommend_treatment(sequence, model, vectorizer, lb)
    
    return jsonify({'treatment_plan': treatment_plan})

if __name__ == '__main__':
    app.run(debug=True)
