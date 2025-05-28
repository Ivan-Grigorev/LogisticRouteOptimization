"""Provides centralized logging configuration."""

import logging

from colorlog import ColoredFormatter


def setup_logger(logger_name):
    """
    Set up and return a logger with colored console output.

    Args:
        logger_name (str): The name of the logger.

    Returns:
        logging.Logger: Configured logger instance with colored output to the console.
    """
    handler = logging.StreamHandler()
    handler.setFormatter(
        ColoredFormatter(
            '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S',
            log_colors={
                'DEBUG': 'white',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
        )
    )

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
