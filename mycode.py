
import pandas as pd
import os

data = { 'name': ['Alice', 'Bob', 'Charlie', 'David'],
         'age': [25, 30, 35, 40],
         'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'] }

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")
