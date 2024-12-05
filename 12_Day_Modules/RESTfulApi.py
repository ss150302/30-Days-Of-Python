from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "ek0I7dX19n0OIoe4YJJWV1DrmN9OB2gbsWpZxDwh"
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed?"

@app.route('/search_asteroids', methods=['GET'])
def search_asteroids():
    query_parameters = request.args.to_dict()
    response = requests.get(BASE_URL, params=query_parameters)
    return jsonify(response.json()), response.status_code

@app.route('/search_asteroids_with_success', methods=['GET'])
def search_asteroids_with_success():
    response = requests.get(f'{BASE_URL}api_key={API_KEY}')
    return jsonify(response.json()), response.status_code

@app.route('/search_asteroids_with_query_parameters_empty', methods=['GET'])
def search_asteroids_with_query_parameters_empty():
    response = requests.get(f'{BASE_URL}api_key={API_KEY}')
    return jsonify(response.json()), response.status_code

@app.route('/search_asteroids_with_start_date', methods=['GET'])
def search_asteroids_with_start_date():
    start_date = request.args.get('start_date', '2023-11-10')
    response = requests.get(f'{BASE_URL}api_key={API_KEY}&start_date={start_date}')
    return jsonify(response.json()), response.status_code

@app.route('/search_asteroids_with_end_date', methods=['GET'])
def search_asteroids_with_end_date():
    end_date = request.args.get('end_date', '2024-12-10')
    response = requests.get(f'{BASE_URL}api_key={API_KEY}&end_date={end_date}')
    return jsonify(response.json()), response.status_code

@app.route('/search_asteroids_in_valid_range', methods=['GET'])
def search_asteroids_in_valid_range():
    start_date = request.args.get('start_date', '2023-11-09')
    end_date = request.args.get('end_date', '2023-11-10')
    response = requests.get(f'{BASE_URL}api_key={API_KEY}&start_date={start_date}&end_date={end_date}')
    return jsonify(response.json()), response.status_code

@app.route('/search_asteroids_in_invalid_range', methods=['GET'])
def search_asteroids_in_invalid_range():
    start_date = request.args.get('start_date', '2023-11-19')
    end_date = request.args.get('end_date', '2023-11-10')
    response = requests.get(f'{BASE_URL}api_key={API_KEY}&start_date={start_date}&end_date={end_date}')
    return jsonify(response.json()), response.status_code

@app.route('/search_asteroids_with_invalid_token', methods=['GET'])
def search_asteroids_with_invalid_token():
    invalid_api_key = "invalid_api_key"
    response = requests.get(f'{BASE_URL}api_key={invalid_api_key}')
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)