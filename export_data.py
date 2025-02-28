import pandas as pd
import os
from logger import get_logger

# Initialize logger for tracking errors and info messages
logger = get_logger()


def export_data(df, start_date, end_date):
    """Saves processed data to CSV and Excel files."""

    # Check if the DataFrame is empty or None
    if df is None or df.empty:
        logger.error(
            "❌ No data available to export."
        )  # Log an error if there's no data
        return  # Exit the function since there's nothing to save

    # Create a filename based on the date range, replacing problematic characters
    filename_base = f"ga4_traffic_{start_date}_to_{end_date}".replace(":", "_").replace(
        "/", "_"
    )
    csvfile, excelfile = f"{filename_base}.csv", f"{filename_base}.xlsx"

    # Save DataFrame to CSV file (UTF-8 encoded to handle special characters)
    df.to_csv(csvfile, index=False, encoding="utf-8-sig")

    # Save DataFrame to Excel file (using 'openpyxl' engine for better compatibility)
    df.to_excel(excelfile, index=False, engine="openpyxl")

    # Log and print confirmation of saved files
    logger.info(f"✅ Files saved: {csvfile}, {excelfile}")
    print(f"📁 Files saved: {csvfile}, {excelfile}")

    # Open the folder where the files are saved
    os.startfile(os.getcwd())
