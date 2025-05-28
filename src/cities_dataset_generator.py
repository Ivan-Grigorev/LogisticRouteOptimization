"""This script generates a dataset of Illinois cities for project analysis tasks."""

import pandas as pd

from logging_config import setup_logger

# Initialize logger
logger = setup_logger(__name__)


def generate_illinois_cities_dataset(output_path):
    """
    Generate a dataset of Illinois cities and save it as a CSV file.

    Args:
        output_path (str): File path to save the generated CSV dataset.

    Raises:
        Exception: If an error occurs during file creation or saving.
    """
    try:
        illinois_cities = [
            {'city': 'Chicago', 'lat': 41.8781, 'lon': -87.6298},
            {'city': 'Aurora', 'lat': 41.7606, 'lon': -88.3201},
            {'city': 'Rockford', 'lat': 42.2711, 'lon': -89.0937},
            {'city': 'Naperville', 'lat': 41.7508, 'lon': -88.1535},
            {'city': 'Joliet', 'lat': 41.5250, 'lon': -88.0817},
            {'city': 'Springfield', 'lat': 39.7817, 'lon': -89.6501},
            {'city': 'Peoria', 'lat': 40.6936, 'lon': -89.5889},
            {'city': 'Champaign', 'lat': 40.1164, 'lon': -88.2434},
        ]

        df = pd.DataFrame(illinois_cities)
        df.to_csv(output_path, index=False)
        logger.info(f"Dataset saved to: {output_path}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    generate_illinois_cities_dataset('./data/illinois_cities.csv')
