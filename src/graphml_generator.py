"""This script generates a Graph with OSMnx."""

import geopandas as gpd
import osmnx as ox
import pandas as pd

from logging_config import setup_logger

# Initialize logger
logger = setup_logger(__name__)


def generate_graphml(df_path, file_path):
    """
    Generate and save Graph for Illinois cities and save it as a file.

    Args:
        df_path (str): Path to the dataset with cities coordinates.
        file_path (str): The path to save generated graphml file.
    """
    try:
        df_cities = pd.read_csv(df_path)

        # Build GeoDataFrame from city coordinates
        gdf = gpd.GeoDataFrame(
            df_cities,
            geometry=gpd.points_from_xy(df_cities['lon'], df_cities['lat']),
            crs='EPSG:4326',
        )

        # Use convex hull around cities with smaller buffer
        convex_hull = gdf.geometry.union_all().convex_hull.buffer(0.1)

        # Get graph from polygon
        G = ox.graph_from_polygon(convex_hull, network_type='drive')

        # Save to file
        ox.save_graphml(G, filepath=file_path)
        logger.info(f"{G} successfully saved at: {file_path}")
    except Exception as e:
        logger.error(f"Failed to generate/save graph to {file_path}. Error: {e}")


if __name__ == '__main__':
    generate_graphml('.data/illinois_cities.csv', '.data/illinois_graph.graphml')
