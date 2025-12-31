# 🌱 Smart AgroMonitor

Smart AgroMonitor is a smart agriculture monitoring system designed to support data-driven farming decisions. It collects, stores, and visualizes environmental sensor data using a hybrid database architecture that combines relational and time-series databases to efficiently manage both real-time and historical agricultural data.

## 🚜 Key Features

* **Hybrid Storage:** Utilizes both PostgreSQL (for structured persistence) and InfluxDB (for high-speed time-series data).
* **Real-time Monitoring:** Collects sensor data via REST APIs for immediate analysis.
* **Data Visualization:** Generates dynamic server-side graphs using Matplotlib to track trends.
* **Web Dashboard:** A Flask-based interface to view current status and historical trends.

## 🧪 Parameters Monitored

The system tracks the following critical environmental factors:
* Temperature
* Humidity
* Soil Moisture
* pH Level
* Light Intensity

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python (Flask) | REST API and application logic |
| **Relational DB** | PostgreSQL | Structured, persistent storage for historical records |
| **Time-Series DB** | InfluxDB | High-performance storage for real-time sensor streams |
| **Visualization** | Matplotlib | Generates trend graphs and charts |

## ⚙️ System Architecture

1.  **Data Ingestion:** Sensors send data to the Flask REST API.
2.  **Dual Storage:**
    * **PostgreSQL:** Stores structured records for long-term auditing.
    * **InfluxDB:** Stores time-stamped data for fast querying and trend analysis.
3.  **Presentation:** Flask renders HTML templates, embedding Matplotlib graphs for user visualization.
