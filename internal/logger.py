import logging
import sys

# Create a logger
logger = logging.getLogger()

# Create a handler for stdout (for DEBUG, INFO, WARNING)
stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setLevel(logging.DEBUG)  # Capture everything up to WARNING
stdout_handler.addFilter(lambda record: record.levelno < logging.ERROR)  # Exclude ERROR and above
stdout_formatter = logging.Formatter('%(levelname)-8s -> %(message)s')
stdout_handler.setFormatter(stdout_formatter)

# Create a handler for stderr (for ERROR, CRITICAL)
stderr_handler = logging.StreamHandler(stream=sys.stderr)
stderr_handler.setLevel(logging.ERROR)  # Capture ERROR and CRITICAL
stderr_formatter = logging.Formatter('%(levelname)-8s -> %(message)s')
stderr_handler.setFormatter(stderr_formatter)

# Add the handlers to the logger
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)
