from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv(r"C:\Users\USER\Downloads\card_data.csv")


@app.route('/api/percentage_of_department_wise_sold_items', methods=['GET'])
def get_percentage_of_department_wise_sold_items():
    
    grouped_data = data.groupby('department')['seats'].sum().reset_index()

    
    total_seats_sold = grouped_data['seats'].sum()

    
    grouped_data['percentage_sold'] = (grouped_data['seats'] / total_seats_sold) * 100

    
    department_wise_percentage_sold = grouped_data.set_index('department')['percentage_sold'].to_dict()

    return jsonify(department_wise_percentage_sold)

if __name__ == '__main__':
    app.run(debug=True)
