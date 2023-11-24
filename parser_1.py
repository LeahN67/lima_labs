# Import modules
import json
import pandas as pd
import matplotlib.pyplot as plt

# Load JSON data from a file
with open("mock_data.json") as f:
    data = json.load(f)


# Extract relevant information and create a DataFrame
df_list = []

for farm in data['farms']:
    for field in farm['fields']:
        df_list.extend(
            {
                'customer': data['customer'],
                'farm': farm['farm'],
                'location': farm['location'],
                'field': field['name'],
                'month': production['month'],
                'production': production['production'],
            }
            for production in field['productions']
        )
# Create DataFrame
df = pd.DataFrame(df_list)

# Display the DataFrame
print(df)


grouped_df = df.groupby('month')['production'].sum()
print(grouped_df)

pivoted_df = df.pivot(index='field', columns='month', values='production')
pivoted_df = pivoted_df[['January', 'February']]

print(pivoted_df)

# Plot production by Field and Month
pivoted_df.plot(kind='bar')

plt.xlabel('Field')
plt.ylabel('Production')
plt.title('Production by Field and Month')
plt.legend(title='Month')

plt.show()


# Save to csv
df.to_csv('mock_data.csv', index=False)










