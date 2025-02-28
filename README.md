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

## 📊 Output Format
The script generates structured reports in the following format:

| Date     | Source / Medium | Country | City  | Sessions | Engaged Sessions | Engagement Rate (%) | Total Users | Total Views |
|----------|---------------|---------|------|----------|----------------|------------------|------------|------------|
| 2025-02-17 | (direct) / (none) | India | Noida | 589 | 453 | 76.91 | 153 | 2889 |
| 2025-01-28 | (direct) / (none) | India | Noida | 585 | 472 | 80.68 | 164 | 3665 |
| 2025-02-25 | (direct) / (none) | India | Noida | 571 | 425 | 74.43 | 149 | 2859 |
| 2025-01-29 | (direct) / (none) | India | Noida | 570 | 440 | 77.19 | 158 | 3234 |

The files are saved as:
- `ga_4_traffic_sources_YYYY_MM_DD_to_YYYY_MM_DD.csv`
- `ga_4_traffic_sources_YYYY_MM_DD_to_YYYY_MM_DD.xlsx`

---

## 🏗️ Installation & Setup
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
3. **Grant Access:**
   - In Google Analytics, go to **Admin > Account Settings** and add the service account email with **Read & Analyze** permission.
4. **Set Up Credentials:**
   - Save the downloaded JSON key file and set its path as an environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-key.json"
   ```
   Alternatively, update the script to reference your credentials file directly.

### 3️⃣ Run the Script
Execute the script with default settings (last 30 days):
```bash
python main.py
```
For a custom date range, specify start and end dates:
```bash
python main.py --start_date 2024-01-01 --end_date 2024-02-01
```

---

## 🔍 How It Works (Step-by-Step)
1. **Authenticate**: The script uses **OAuth 2.0** to authenticate with the Google Analytics API.
2. **Fetch Data**: It queries **blog.izooto.com**'s GA4 data, retrieving session metrics, engagement rates, user counts, and total views.
3. **Process Data**: The data is formatted into a structured **Pandas DataFrame**.
4. **Export Data**: Saves the output as a **CSV** and **Excel** file.
5. **Handle Errors & Logging**: Logs issues like API rate limits, missing data, or authentication failures.
6. **(Optional) Auto-Download in Colab**: If running in Google Colab, files are automatically downloaded.

---

## 📝 Additional Information
- **Company:** This assignment was provided by **IZooto** as part of an assessment.
- **Project ID:** `354503001`
- **Service Account JSON File:** [Download Here](https://drive.google.com/file/d/1h6KvJ_0A76JIA-4N3OCF4bsEJ_ODOkQu/view?usp=drive_link)

---

## ❗ Troubleshooting
### 1️⃣ `ModuleNotFoundError: No module named 'openpyxl'`
- Install `openpyxl` using:
  ```bash
  pip install openpyxl
  ```

### 2️⃣ `google.auth.exceptions.DefaultCredentialsError`
- Ensure the **GOOGLE_APPLICATION_CREDENTIALS** environment variable is correctly set.

### 3️⃣ `Quota Exceeded` or `403 Forbidden`
- Check if your **Google Analytics API** usage quota is exceeded.
- Ensure the **Service Account Email** has **Read & Analyze** permissions in Google Analytics.

---

## 📌 Future Improvements
- Add **Dashboard Visualization** for better insights.
- Automate scheduled runs using **Cron Jobs**.
- Include **Email Notifications** for generated reports.

---

## 📩 Contact & Support
For any queries or issues, reach out to **IZooto Team** or create an issue in the repository.

