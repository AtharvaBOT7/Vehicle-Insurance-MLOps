## Below is the code to check if the logging module is working correctly.

# from src.logger import logging

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

## Below is the code to check if the custom exception class is working correctly.

# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     # Simulating an error
#     a = 1 / 0
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()