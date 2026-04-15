# 📌 Step 1: Import Libraries
import pandas as pd

# 📌 Step 2: Upload Dataset (Colab)
from google.colab import files
uploaded = files.upload()
# Loading Dataset
df = pd.read_csv('cde_ipaas_dataset.csv')

# 📌 Step 3: Display Dataset
print("Original Dataset:")
print(df.head())

# 📌 Step 4: HDFS Simulation (Data Storage)
# (Here we just treat DataFrame as stored data)
hdfs_data = df.copy()

# 📌 Step 5: Data Filtering

# Condition 1: High Energy Consumption
high_energy = hdfs_data[hdfs_data['Energy_Consumption'] > hdfs_data['Energy_Consumption'].mean()]

# Condition 2: Low Transmission Efficiency
low_efficiency = hdfs_data[hdfs_data['Transmission_Efficiency'] < hdfs_data['Transmission_Efficiency'].mean()]

print("\nHigh Energy Consumption Sensors:")
print(high_energy)

print("\nLow Transmission Efficiency Sensors:")
print(low_efficiency)

# 📌 Step 6: HBase Simulation using Dictionary

hbase_table = {}

for index, row in df.iterrows():
    row_key = f"sensor_{index}"

    hbase_table[row_key] = {
        "meta": {
            "sensor_type": row["Sensor_Type"]
        },
        "metrics": {
            "energy_consumption": row["Energy_Consumption"],
            "data_yield": row["Data_Yield"],
            "transmission_efficiency": row["Transmission_Efficiency"]
        }
    }

# 📌 Step 7: Display Sample HBase Data
print("\nSample HBase Data:")
for key, value in list(hbase_table.items())[:5]:
    print(key, ":", value)

# 📌 Step 8: Filter Data from HBase

filtered_hbase = {}

for key, value in hbase_table.items():
    if (value["metrics"]["energy_consumption"] > df["Energy_Consumption"].mean()) or \
       (value["metrics"]["transmission_efficiency"] < df["Transmission_Efficiency"].mean()):
        filtered_hbase[key] = value

print("\nFiltered HBase Data:")
for key, value in filtered_hbase.items():
    print(key, ":", value)
