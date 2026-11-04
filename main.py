
import os
from dotenv import load_dotenv
from services.loan_service import create_loan


def main():

    load_dotenv()

    dry_run = os.getenv("DRY_RUN", "true").lower() == "true"

    if dry_run:
        print("DRY RUN MODE")
        print("Configuration loaded successfully.")
        print("No loan creation request was sent.")
        print("Set DRY_RUN=false after authorization to submit.")
        return

    try:
        response = create_loan()

        print("Loan created successfully!")
        print("Loan ID:", response.get("loanId"))
        print("Loan URL:", response.get("loan_url"))

    except Exception as error:
        print("Loan creation failed:", error)


if __name__ == "__main__":
    main()
