"""This script solves the Traveling Salesman Problem (TSP) using Google OR-Tools."""

import json

import pandas as pd
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

from logging_config import setup_logger

# Initialize logger
logger = setup_logger(__name__)


def solve_tsp(distance_matrix_miles, city_names):
    """
    Solve TSP for given distance matrix and return the optimal route and distance.

    Args:
        distance_matrix_miles (List[List[float]]): 2D list with distances in miles.
        city_names (List[str]): List of city names matching the order of the matrix.

    Returns:
        tuple: (rout as list of city names, total distance in miles)
    """
    # Convert to integer for OR-Tools
    distance_matrix = [[int(dist * 100) for dist in row] for row in distance_matrix_miles]

    # Routing setup
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)  # 1 vehicle, start at city 0
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    solution = routing.SolveWithParameters(search_params)

    if solution:
        index = routing.Start(0)
        route = []
        route_distance = 0

        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            route.append(city_names[node])
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)

        route.append(city_names[manager.IndexToNode(index)])  # return to start
        logger.info("Optimal route was successfully found.")
        return route, round(route_distance / 100, 2)  # convert back to miles
    else:
        logger.warning("No TSP solution found.")
        return None


def save_tsp():
    """
    Solve the TSP and save the result as a JSON file.

    Raises:
        Exception: If an unexpected error occurs while reading files or saving the result.
    """
    try:
        df = pd.read_csv('../data/distance_matrix.csv', index_col=0)
        distance_matrix_miles = df.values.tolist()
        city_names = df.index.tolist()

        result = solve_tsp(distance_matrix_miles, city_names)

        if result:
            route, total_distance = result
            output = {'route': route, 'total_distance': total_distance}

            with open('../data/tsp_result.json', 'w') as f:
                json.dump(output, f, indent=4)
                logger.info("TSP result saved to JSON file.")
        else:
            logger.warning("TSP result not saved because no solution was found.")
    except Exception as e:
        logger.error(f"Saving TSP result as JSON file failed: {e}")


if __name__ == '__main__':
    save_tsp()
