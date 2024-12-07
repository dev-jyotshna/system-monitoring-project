---

# **System Monitoring Project**

This project is a Python-based system monitoring tool that tracks CPU, memory, and disk usage using the **psutil** library. The data is visualized in **Grafana**, which is powered by metrics collected using **Prometheus**. It is a lightweight and user-friendly monitoring solution that runs entirely on your local machine.

OverView [Click here](https://docs.google.com/presentation/d/13kf9kBuV06y3CAOekVWuekw7ZfWDhWL18TagEM8mRv8/edit?usp=sharing)

---

## **Features**
- **Real-time monitoring** of CPU, memory, and disk usage.
- **Email alerts** for high resource usage.
- Integration with **Prometheus** for collecting metrics.
- **Grafana dashboards** for advanced visualization.
- Completely free and runs locally without relying on cloud services.

---

## **Technologies Used**
1. **Python**: For monitoring system metrics and sending alerts.
2. **Prometheus**: For scraping and storing metrics.
3. **Grafana**: For building interactive dashboards.
4. **psutil**: Python library for retrieving system metrics.

---

## **Project Structure**
```bash
System-Monitoring-Project/
│
├── monitoring.py                # Python script for collecting metrics
├── prometheus.yml               # Prometheus configuration file
├── grafana_dashboard.json       # Exported Grafana dashboard
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Files to exclude from GitHub
```

---

## **Setup and Usage**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/system-monitoring-project.git
cd system-monitoring-project
```

---

### **Step 2: Install Dependencies**
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have **Prometheus** and **Grafana** installed on your system:
   - Download Prometheus from [Prometheus Downloads](https://prometheus.io/download/).
   - Download Grafana from [Grafana Downloads](https://grafana.com/grafana/download/).

---

### **Step 3: Set Up Prometheus**
1. Edit the `prometheus.yml` file to configure Prometheus to scrape metrics from your Python script:
   ```yaml
   scrape_configs:
     - job_name: 'system_monitor'
       static_configs:
         - targets: ['localhost:8000']
   ```

2. Start Prometheus by running:
   ```bash
   prometheus --config.file=prometheus.yml
   ```

---

### **Step 4: Run the Python Monitoring Script**
Start the Python monitoring script that exposes the metrics:
```bash
python monitoring.py
```

---

### **Step 5: Set Up Grafana**
1. Navigate to new commmand prompt and folder in which grafana.exe is stored , Start Grafana:
   ```bash
   grafana-server.exe
   ```

2. Open Grafana in your browser at [http://localhost:3000](http://localhost:3000).
3. Log in with default credentials:
   - Username: `admin`
   - Password: `admin`
4. Add Prometheus as a data source:
   - Go to **Configuration > Data Sources > Add Data Source**.
   - Select **Prometheus** and enter the URL: `http://localhost:9090`.
5. Import the provided Grafana dashboard:
   - Go to **Dashboards > Import**.
   - Upload the `dashboard-grafana.json` file from this project.

---

### **Step 6: Visualize Metrics**
- Open the Grafana dashboard to view real-time metrics for CPU, memory, and disk usage.

---

## **Customizing the Project**

### **Email Alerts**
To receive email alerts for high CPU, memory, or disk usage:
1. Make `.env` file and Configure your email credentials in the `.env` file:
   ```text
   SENDER_EMAIL=your-email@gmail.com
   SENDER_PASSWORD=your-email-password
   RECIPIENT_EMAIL=recipient-email@gmail.com
   ```

2. Sensitive Information: SENDER_EMAIL, SENDER_PASSWORD, and RECIPIENT_EMAIL are now loaded from a .env file using the dotenv package.
   - Install the python-dotenv package:
```bash
pip install python-dotenv
```

3. Adjust the thresholds for alerts:
   ```python
   CPU_THRESHOLD = 80
   MEMORY_THRESHOLD = 80
   DISK_THRESHOLD = 80
   ```

---

## **Best Practices**
1. Do not include Prometheus or Grafana binaries in your repository.
2. Use the `.gitignore` file to exclude sensitive files:
   ```
   prometheus*
   grafana*
   *.log
   *.exe
   ```
3. Provide detailed setup instructions to ensure reproducibility.

---

## **Screenshots**
1. The Grafana dashboard.

![Screenshot 2024-12-07 103248](https://github.com/user-attachments/assets/1dc2a722-b5ca-4011-b7df-78cc897f8356)

2. The Prometheus interface showing the metrics.

![Screenshot 2024-12-06 223131](https://github.com/user-attachments/assets/f494ce9b-86ab-4cc4-9d9e-71250f8ff166)

---

## **Limitations**
- This project runs locally and is not suitable for large-scale deployments without further modifications.
- Prometheus and Grafana must be installed manually on the user's system.

---

## **Future Enhancements**
1. Add Docker support for easier deployment.
2. Monitor additional metrics like network usage or process information.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [psutil](https://github.com/giampaolo/psutil)

---
