"""This script generates a dataset of Illinois cities for project analysis tasks."""

import pandas as pd


def generate_illinois_cities_dataset(cities, output_path):
    """
    Generate a dataset of Illinois cities and saves it as a CSV file.

    Args:
        cities (list): A list of dictionaries, each containing 'city', 'lat', and 'lon' keys.
        output_path (str): File path to save the generated CSV dataset.

    Returns:
        str: Confirmation message or error details if an exception occurs.
    """
    try:
        df = pd.DataFrame(cities)
        df.to_csv(output_path, index=False)
        return f"Dataset saved to: {output_path}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


if __name__ == '__main__':
    result = generate_illinois_cities_dataset(
        cities=[
            {'city': 'Chicago', 'lat': 41.8781, 'lon': -87.6298},
            {'city': 'Aurora', 'lat': 41.7606, 'lon': -88.3201},
            {'city': 'Rockford', 'lat': 42.2711, 'lon': -89.0937},
            {'city': 'Naperville', 'lat': 41.7508, 'lon': -88.1535},
            {'city': 'Joliet', 'lat': 41.5250, 'lon': -88.0817},
            {'city': 'Springfield', 'lat': 39.7817, 'lon': -89.6501},
            {'city': 'Peoria', 'lat': 40.6936, 'lon': -89.5889},
            {'city': 'Champaign', 'lat': 40.1164, 'lon': -88.2434},
        ],
        output_path='./data/illinois_cities.csv',
    )
    print(result)
