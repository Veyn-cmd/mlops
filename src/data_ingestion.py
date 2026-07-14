
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')   


console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def load_data(data_url: str) -> pd.DataFrame:
    """Load data from a CSV file."""

    try:
        df = pd.read_csv(data_url)
        logger.debug(f"Data loaded successfully from {data_url}. Shape: {df.shape}")
        return df
    except pd.errors.ParserError as e:
        logger.error(f"failed to parse CSV file from {data_url}: {e}")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading data from {data_url}: {e}")
        raise





def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data by handling missing values and encoding categorical variables."""

    try:
        # Handle missing values
        df.rename(columns={'Category': 'target', 'Message': 'text'}, inplace =True)
        logger.debug('data preprocessing completed successfully')
        
        return df
    

    except KeyError as e:
        logger.error(f"Missing expected column in the DataFrame: {e}")
        raise

    except Exception as e:
        logger.error(f"An error occurred during preprocessing: {e}")
        raise



def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str) -> None:
    """Save the DataFrame to a CSV file."""

    try:
        raw_data_path = os.path.join(data_path, 'raw')
        os.makedirs(raw_data_path, exist_ok=True)
        train_data.to_csv(f"{raw_data_path}/train.csv", index=False)
        test_data.to_csv(f"{raw_data_path}/test.csv", index=False)
        logger.debug(f"Data saved successfully to {raw_data_path}.")
    except Exception as e:
        logger.error(f"An error occurred while saving data to {output_path}: {e}")
        raise


def main():
    try:
        test_size = 0.21
        data_path = "https://raw.githubusercontent.com/Veyn-cmd/mlops/refs/heads/main/data/spam.csv"
        df = load_data(data_url=data_path)
        final_df = preprocess_data(df)
        train_data, test_data = train_test_split(final_df, test_size=test_size, random_state=42)
        save_data(train_data, test_data, data_path='./data')

    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}")
        print(f"erroer: {e}")


if __name__ == "__main__":
    main()