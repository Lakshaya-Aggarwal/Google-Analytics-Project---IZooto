import logging

"""Configure logging settings for the script."""

logging.basicConfig(
    filename="log_report.log",  # Log messages will be saved in this file
    level=logging.INFO,  # Set logging level to INFO (captures INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define log message format
)


def get_logger():
    """Returns a logger instance for logging messages in the script."""

    return logging.getLogger(
        __name__
    )  # Creates and returns a logger specific to this module
