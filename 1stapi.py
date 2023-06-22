from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv(r"C:\Users\USER\Downloads\card_data.csv")

@app.route('/api/total_items', methods=['GET'])
def get_total_items():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    department = request.args.get('department')

    if start_date is None or end_date is None or department is None:
        return jsonify({'error': 'Missing query parameters: start_date, end_date, department'})

    filtered_data = data[(data['date'] >= start_date) &
                         (data['date'] <= end_date) &
                         (data['department'] == department)]

    filtered_data['Quarter'] = pd.to_datetime(filtered_data['date']).dt.quarter

    filtered_data = filtered_data[filtered_data['Quarter'] == 3]

    total_items = filtered_data['seats'].sum()

    print("Total items sold:", total_items)

    return jsonify({'total_items': int(total_items)})

if __name__ == '__main__':
    app.run(debug=True)

