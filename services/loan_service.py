
import os
import json
import requests
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def create_loan():

    api_url = os.getenv("API_URL")
    offer_code_id = os.getenv("OFFER_CODE_ID")
    user_id = os.getenv("USER_ID")
    api_type = os.getenv("API_TYPE")
    authorization = os.getenv("AUTHORIZATION")

    required_values = {
        "API_URL": api_url,
        "OFFER_CODE_ID": offer_code_id,
        "USER_ID": user_id,
        "API_TYPE": api_type,
        "AUTHORIZATION": authorization
    }

    missing = [
        key for key, value in required_values.items() if not value
    ]

    if missing:
        raise ValueError(
            f"Missing environment variables: {', '.join(missing)}"
        )

    payload_path = BASE_DIR / "loan_payload.json"

    with open(payload_path, "r", encoding="utf-8") as file:
        payload = json.load(file)

    headers = {
        "UserId": user_id,
        "Type": api_type,
        "Content-Type": "application/json",
        "Authorization": authorization
    }

    params = {
        "offerCodeId": offer_code_id
    }

    response = requests.post(
        api_url,
        params=params,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    return response.json()
