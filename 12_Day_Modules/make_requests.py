import requests


def make_request(query_parameters):
    base_url = "https://api.nasa.gov/neo/rest/v1/feed?"
    response = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?api_key=ek0I7dX19n0OIoe4YJJWV1DrmN9OB2gbsWpZxDwh')
    return response