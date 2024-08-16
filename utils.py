import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_error(error_msg):
    logging.error(f"An error occurred: {error_msg}")
    raise Exception(error_msg)
