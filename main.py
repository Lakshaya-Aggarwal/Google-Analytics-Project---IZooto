from fetch_data import fetch_ga4_data
from process_data import process_data
from export_data import export_data
from logger import get_logger

# Initialize logger for tracking execution
logger = get_logger()

if __name__ == "__main__":
    """
    Main script to extract, process, and export GA4 data.

    - Fetches raw data from Google Analytics 4 (GA4).
    - Processes the data into a structured format.
    - Exports the cleaned data for further analysis or reporting.
    """

    logger.info("🚀 Starting GA4 Data Extraction Script...")
    print("🚀 Running GA4 Data Extraction...")

    # Step 1: Fetch GA4 data
    response, start_date, end_date = fetch_ga4_data()

    if response:
        # Step 2: Process the raw response into a structured dataframe
        df = process_data(response)

        # Step 3: Export the processed data to a file (CSV, Excel)
        export_data(df, start_date, end_date)

        logger.info("🎯 GA4 Data Extraction Completed Successfully.")
        print("✅ GA4 Data Extraction Completed Successfully.")
    else:
        # Log and print an error if data fetch fails
        logger.error("❌ Failed to fetch GA4 data.")
        print("❌ GA4 Data Extraction Failed. Check logs for details.")
