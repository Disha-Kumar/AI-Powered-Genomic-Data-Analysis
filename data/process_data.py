import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def process_data(df):
    vectorizer = CountVectorizer(analyzer='char')
    X = vectorizer.fit_transform(df['sequence'])
    return X, df['disorder'], vectorizer

# Example usage
df = collect_data()
X, y, vectorizer = process_data(df)
print(X.shape, y.shape)
