# Automating Google Analytics Reports for Blog.izooto.com

## 📌 Project Overview
This project automates the process of fetching, processing, and exporting Google Analytics data for the domain **blog.izooto.com**. The script connects to the **Google Analytics API**, retrieves traffic and performance metrics, and stores the data in structured CSV and Excel files. The automation ensures that data is consistently fetched, formatted, and ready for further analysis.

## 🚀 Features
- **Automated Data Retrieval:** Fetches performance metrics such as sessions, engaged sessions, engagement rate, total users, and total views.
- **Date Range Selection:** Allows fetching reports for a custom date range (default: last 30 days).
- **Data Storage:** Saves results in CSV and Excel formats with an easy-to-read naming convention.
- **Logging and Error Handling:** Implements robust logging and error handling to manage API failures, rate limits, and authentication issues.
- **Extensible and Modular:** The code is well-structured for easy customization and scalability.

---

## 🛠️ Technology Stack
- **Programming Language:** Python
- **APIs Used:** Google Analytics API (GA4)
- **Authentication:** OAuth 2.0 via service account
- **Data Processing:** Pandas
- **File Formats:** CSV, Excel

---
## 🔧 Installation & Setup
### 1️⃣ Install Required Dependencies
Ensure you have Python installed. Then, install the necessary packages:
```bash
pip install pandas google-auth google-auth-oauthlib google-auth-httplib2 googleapiclient openpyxl
```


### 2️⃣ Set Up Google Analytics API Access
1. **Create a Google Cloud Project** and enable the **Google Analytics API**.
2. **Generate Service Account Credentials:**
   
   - Go to the **Google Cloud Console**.
   - Create a **Service Account** and download the JSON key file.
     
4. **Grant Access:**
   - In Google Analytics, go to **Admin > Account Settings** and add the service account email with **Read & Analyze** permission.
5. **Set Up Credentials:**
   - Save the JSON key file and keep it in the same folder/repository as your script.

     
### 3️⃣ Run the Script
- **Run with Default Settings (Last 30 Days):**
```bash
python main.py
```
- **Run with a Custom Date Range:**
```bash
python main.py --start_date 2024-01-01 --end_date 2024-02-01
```
---




## 📊 Output Format
The script generates structured reports in the following format:

| Date     | Source / Medium | Country | City  | Sessions | Engaged Sessions | Engagement Rate (%) | Total Users | Total Views |
|----------|---------------|---------|------|----------|----------------|------------------|------------|------------|
| 2025-02-17 | (direct) / (none) | India | Noida | 589 | 453 | 76.91 | 153 | 2889 |
| 2025-01-28 | (direct) / (none) | India | Noida | 585 | 472 | 80.68 | 164 | 3665 |
| 2025-02-25 | (direct) / (none) | India | Noida | 571 | 425 | 74.43 | 149 | 2859 |
| 2025-01-29 | (direct) / (none) | India | Noida | 570 | 440 | 77.19 | 158 | 3234 |

The files are saved as:
- **CSV File:** `ga_4_traffic_sources_YYYY_MM_DD_to_YYYY_MM_DD.csv`
- **Excel FIle:** `ga_4_traffic_sources_YYYY_MM_DD_to_YYYY_MM_DD.xlsx`

---



## 🔍 How It Works
1. **Authenticate**: The script uses **OAuth 2.0** to authenticate with the Google Analytics API.
2. **Fetch Data**: It queries **blog.izooto.com**'s GA4 data, retrieving session metrics, engagement rates, user counts, and total views.
3. **Process Data**: The data is formatted into a structured **Pandas DataFrame**.
4. **Export Data**: Saves the output as a **CSV** and **Excel** file.
5. **Handle Errors & Logging**: Logs issues like API rate limits, missing data, or authentication failures.


---


## ❗ Troubleshooting
### 1️⃣ `ModuleNotFoundError: No module named 'openpyxl'`
- Install `openpyxl` using:
  ```bash
  pip install openpyxl
  ```

### 3️⃣ `Quota Exceeded` or `403 Forbidden`
- Check if your **Google Analytics API** usage quota is exceeded.
- Ensure the **Service Account Email** has **Read & Analyze** permissions in Google Analytics.

---

## 📌 Future Improvements
- Add **Dashboard Visualization** for better insights.
- Automate scheduled runs.
- Include **Email Notifications** for generated reports.


