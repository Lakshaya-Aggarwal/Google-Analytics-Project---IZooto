import pandas as pd
from logger import get_logger

# Initialize logger to track errors and info messages
logger = get_logger()


def process_data(response):
    """Processes API response and returns a DataFrame."""

    # Check if the response is empty or missing
    if not response:
        logger.error(
            "❌ No data available to process."
        )  # Log an error if no data is found
        return None  # Return None to indicate failure

    data = []  # Initialize an empty list to store processed rows

    # Loop through each row in the API response
    for row in response.rows:
        data.append(
            {
                "Date": row.dimension_values[0].value,  # Extract date from response
                "Source / Medium": f"{row.dimension_values[1].value} / {row.dimension_values[2].value}",  # Combine source & medium
                "Country": row.dimension_values[3].value,  # Extract country
                "City": row.dimension_values[4].value,  # Extract city
                "Sessions": row.metric_values[0].value,  # Number of sessions
                "Engaged Sessions": row.metric_values[
                    1
                ].value,  # Number of engaged sessions
                "Engagement Rate (%)": float(row.metric_values[2].value)
                * 100,  # Convert engagement rate to percentage
                "Total Users": row.metric_values[3].value,  # Total number of users
                "Total Views": row.metric_values[4].value,  # Total views count
            }
        )

    # Convert processed data into a Pandas DataFrame
    df = pd.DataFrame(data)

    logger.info("✅ Data processed successfully.")  # Log success message

    # Print a preview of the extracted data (first 5 rows)
    print("📊 Extracted Data:")
    print(df.head())

    return df  # Return the DataFrame for further use
