from flask import Flask, jsonify
from fpgrowth_py import fpgrowth
import pickle
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/generate_rules', methods=['GET'])
def generate_rules():

    try:
        csv_file_path = '2023_spotify_ds1.csv'

        df = pd.read_csv(csv_file_path)

        df.describe()

        transactions = df['track_name'].tolist()

        rules = fpgrowth(transactions, minSupRatio=0.5, minConf=0.5)

        with open('rules.pkl', 'wb') as f:
            pickle.dump(rules, f)

        return jsonify({'status': 'success', 'rules': rules})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True, port=5002)