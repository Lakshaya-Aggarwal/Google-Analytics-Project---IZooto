import datetime
import time
from google.analytics.data import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest
from google.api_core.exceptions import GoogleAPIError, DeadlineExceeded
from auth import get_credentials
from logger import get_logger

# Initialize logger for tracking execution
logger = get_logger()

# Google Analytics 4 (GA4) Property ID
GA_PROPERTY_ID = "354503001"


def fetch_ga4_data():
    """
    Fetches Google Analytics 4 (GA4) data for the last 30 days.

    - Authenticates using service account credentials.
    - Retrieves key metrics such as sessions, engagement, and user behavior.
    - Implements error handling with retries for API rate limits and failures.
    """

    # Get credentials for authenticating with Google Analytics API
    credentials = get_credentials()
    client = BetaAnalyticsDataClient(credentials=credentials)

    # Define the date range for fetching data (last 30 days up to yesterday)
    end_date = datetime.datetime.now() - datetime.timedelta(days=1)
    start_date = end_date - datetime.timedelta(days=30)

    # Convert dates to the required format (YYYY-MM-DD)
    START_DATE = start_date.strftime("%Y-%m-%d")
    END_DATE = end_date.strftime("%Y-%m-%d")

    logger.info(f"📊 Fetching GA4 data from {START_DATE} to {END_DATE}")

    # Define the request payload for the GA4 API
    request = RunReportRequest(
        property=f"properties/{GA_PROPERTY_ID}",
        date_ranges=[{"start_date": START_DATE, "end_date": END_DATE}],
        dimensions=[
            {"name": "date"},  # Date of user activity
            {
                "name": "sessionSource"
            },  # Traffic source (e.g., direct, organic, referral)
            {"name": "sessionMedium"},  # Medium (e.g., search, email, social)
            {"name": "country"},  # Country of the users
            {"name": "city"},  # City of the users
        ],
        metrics=[
            {"name": "sessions"},  # Number of sessions
            {"name": "engagedSessions"},  # Sessions with engagement
            {"name": "engagementRate"},  # Percentage of engaged sessions
            {"name": "totalUsers"},  # Total unique users
            {"name": "screenPageViews"},  # Total page views
        ],
    )

    # Attempt to fetch data with retry logic for error handling
    for attempt in range(5):
        try:
            # Send API request and retrieve response
            response = client.run_report(request)

            # Check if any data was returned
            if not response.rows:
                logger.warning("⚠️ No data returned from GA4 API.")
                return None, None, None

            logger.info("✅ GA4 data fetched successfully.")
            return response, START_DATE, END_DATE

        except DeadlineExceeded:
            # Handle API rate limits by retrying with exponential backoff
            wait_time = 2**attempt
            logger.warning(
                f"⚠️ API rate limit exceeded. Retrying in {wait_time} seconds..."
            )
            time.sleep(wait_time)

        except GoogleAPIError as e:
            # Log API-related errors and stop execution
            logger.error(f"❌ GA4 API error: {e}")
            break

        except Exception as e:
            # Handle unexpected errors and log details for debugging
            logger.exception(f"❌ Unexpected error while fetching GA4 data: {e}")
            break

    # If all retry attempts fail, log an error and return failure response
    logger.error("❌ GA4 data fetch failed after multiple attempts.")
    return None, None, None
