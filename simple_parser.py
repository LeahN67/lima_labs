import json
import pandas as pd

# Load JSON data from a file
with open("mock_data.json") as f:
    data = json.load(f)

# Normalize the data and create a DataFrame
df = pd.json_normalize(
    data,
    record_path=['farms', 'fields', 'productions'],
    meta=[
        ['farms', 'farm'],
        ['farms', 'location'],
        'customer',
        ['fields', 'name']
    ],
    meta_prefix='fields.'
)

# Rename columns to match the original DataFrame's structure
df.rename(columns={
    'fields.farms.farm': 'farm',
    'fields.farms.location': 'location',
    'fields.name': 'field',
    'month': 'month',
    'production': 'production'
}, inplace=True)

# Display the DataFrame
print(df)
