import os
import sys
from google.oauth2 import service_account
from google.auth.exceptions import GoogleAuthError
from logger import get_logger

# Initialize logger to track script execution and errors
logger = get_logger()

# Define the service account JSON file path
SERVICE_ACCOUNT_FILE = "service_account.json"


def get_credentials():
    """Authenticate using service account and return credentials."""

    # First, check if the service account file actually exists
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        logger.error("❌ service_account.json file not found! Please upload it.")
        sys.exit("service_account.json file missing. Upload before running the script.")

    try:
        # Attempt to load credentials from the service account file
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE
        )
        # If we reach here, authentication was successful
        logger.info("✅ Authentication successful.")
        return credentials

    except GoogleAuthError as e:
        # Handles authentication failures due to incorrect or invalid service account file
        logger.error(f"❌ Authentication failed: {e}")
        sys.exit("Authentication failed. Please check your service account file.")

    except Exception as e:
        # Catch any other unexpected errors (e.g., file corruption, permission issues, etc.)
        logger.exception(f"❌ Unexpected authentication error: {e}")
        sys.exit("Unexpected authentication error. Check logs for details.")
