from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv(r"C:\Users\USER\Downloads\card_data.csv")


@app.route('/api/nth_most_total_item', methods=['GET'])
def get_nth_most_total_item():
    item_by = request.args.get('item_by')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    n = request.args.get('n')

    if item_by is None or start_date is None or end_date is None or n is None:
        return jsonify({'error': 'Missing query parameters'})

    try:
        n = int(n)
    except ValueError:
        return jsonify({'error': 'Invalid value for n parameter'})

    
    filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

    
    if item_by == 'quantity':
        grouped_data = filtered_data.groupby('department')['seats'].sum().reset_index()
    elif item_by == 'price':
        grouped_data = filtered_data.groupby('department')['amount'].sum().reset_index()
    else:
        return jsonify({'error': 'Invalid value for item_by parameter'})

    
    sorted_data = grouped_data.sort_values(item_by, ascending=False)

    
    if n <= len(sorted_data):
        nth_most_sold_item = sorted_data.iloc[n - 1]['department']
    else:
        nth_most_sold_item = "Not enough departments"

    return jsonify({'nth_most_sold_item': nth_most_sold_item})

if __name__ == '__main__':
    app.run(debug=True)
