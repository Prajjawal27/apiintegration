from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv(r"C:\Users\USER\Downloads\card_data.csv")


@app.route('/api/monthly_sales', methods=['GET'])
def get_monthly_sales():
    product = request.args.get('product')
    year = request.args.get('year')

    if product is None or year is None:
        return jsonify({'error': 'Missing query parameters'})

    try:
        year = int(year)
    except ValueError:
        return jsonify({'error': 'Invalid value for year parameter'})

    
    filtered_data = data[(data['Product'] == product) & (data['Year'] == year)]

    
    monthly_sales = filtered_data.groupby('Month')['Sales'].sum().tolist()

    return jsonify({'monthly_sales': monthly_sales})

if __name__ == '__main__':
    app.run(debug=True)


