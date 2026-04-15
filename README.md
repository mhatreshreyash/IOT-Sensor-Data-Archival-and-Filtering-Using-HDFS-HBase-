# 📊 IoT Sensor Data Archival and Filtering Using HDFS & HBase

## 📌 Project Overview
This project demonstrates how large-scale IoT sensor data can be efficiently stored, processed, and analyzed using Big Data concepts inspired by the Hadoop ecosystem. It focuses on data archival, filtering, and performance optimization.

---

## 🎯 Objectives
- Archive IoT sensor data using HDFS-inspired storage  
- Enable fast access using HBase-style data modeling  
- Filter and analyze sensor performance  
- Identify:
  - High energy consumption sensors  
  - Low transmission efficiency sensors  

---

## 🛠️ Technologies Used
- Python  
- Google Colab  
- Pandas  
- HDFS (Simulated)  
- HBase (Simulated using Python Dictionary)  

---

## 📂 Dataset Description
The dataset includes:
- Sensor Type  
- Data Size  
- Duration  
- Energy Consumption  
- Data Yield  
- Transmission Efficiency  

---

## ⚙️ Workflow

### 1. Data Upload
- Upload CSV file into Google Colab  

### 2. HDFS Simulation
- Store large-scale sensor data  
- Perform initial filtering  

### 3. Data Filtering
- Extract sensors with:
  - High energy consumption  
  - Low transmission efficiency  

### 4. HBase Simulation
- Store filtered data using structured format:
  - Row Key → query_id  
  - Column Families → meta, metrics  
  - Columns → sensor_type, energy_consumption, data_yield, transmission_efficiency  

### 5. Analysis
- Display filtered results  
- Analyze sensor performance  

---

## 📊 Output
The project outputs filtered sensor data highlighting inefficient sensors based on energy and transmission metrics.

---

## 🚀 Features
- Simulates Big Data architecture  
- Handles large datasets efficiently  
- Multi-layer filtering (HDFS + HBase)  
- Structured data storage approach  
- Useful for IoT optimization  

---

## 🧾 Conclusion
This project shows how Big Data tools can be applied to IoT systems for efficient data storage and analysis. It helps identify inefficient sensors and improves overall system performance.

---

## 🔮 Future Enhancements
- Integration with real Hadoop ecosystem  
- Real-time data processing using Apache Kafka  
- Data visualization dashboards (Power BI / Tableau)  
- Cloud deployment  

---

## 👨‍💻 Author
**Shreyash Santosh Mhatre**
