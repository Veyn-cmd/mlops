
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('data_ingestion')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(os.path.join(log_dir, 'data_ingestion.log'))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)