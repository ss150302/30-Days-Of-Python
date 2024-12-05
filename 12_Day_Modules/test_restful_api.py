import requests

BASE_URL = "http://127.0.0.1:5000"

def test_search_asteroids():
    response = requests.get(f'{BASE_URL}/search_asteroids')
    assert response.status_code == 200

def test_search_asteroids_with_success():
    response = requests.get(f'{BASE_URL}/search_asteroids_with_success')
    assert response.status_code == 200

def test_search_asteroids_with_query_parameters_empty():
    response = requests.get(f'{BASE_URL}/search_asteroids_with_query_parameters_empty')
    assert response.status_code == 200

def test_search_asteroids_with_start_date():
    response = requests.get(f'{BASE_URL}/search_asteroids_with_start_date?start_date=2023-11-10')
    assert response.status_code == 200

def test_search_asteroids_with_end_date():
    response = requests.get(f'{BASE_URL}/search_asteroids_with_end_date?end_date=2024-12-10')
    assert response.status_code == 200

def test_search_asteroids_in_valid_range():
    response = requests.get(f'{BASE_URL}/search_asteroids_in_valid_range?start_date=2023-11-09&end_date=2023-11-10')
    assert response.status_code == 200

def test_search_asteroids_in_invalid_range():
    response = requests.get(f'{BASE_URL}/search_asteroids_in_invalid_range?start_date=2023-11-19&end_date=2023-11-10')
    assert response.status_code == 200

def test_search_asteroids_with_invalid_token():
    response = requests.get(f'{BASE_URL}/search_asteroids_with_invalid_token')
    assert response.status_code == 200
#Run the tests and generate an HTML report:
#pytest --html=report.html
