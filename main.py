import logging

log_format = "%(asctime)s %(levelname)s: \n%(message)s\n"

logging.basicConfig(filename="logging.log", level=logging.INFO, format=log_format)
