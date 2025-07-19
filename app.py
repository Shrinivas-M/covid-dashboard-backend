from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Load CSV data
df = pd.read_csv('data/covid_demo_data.csv')

@app.route('/')
def home():
    return "COVID Dashboard Backend Running!"

@app.route('/api/data')
def get_data():
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
