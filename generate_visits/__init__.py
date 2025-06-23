import datetime
import logging
import random
import requests

import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    stores = ["Store1", "Store2", "Store3"]
    sections = ["Men", "Women", "Kids"]

    store_id = random.choice(stores)
    section = random.choice(sections)
    current_timestamp = datetime.datetime.utcnow().isoformat()
    random_count = random.randint(1, 10)

    request_body = {
        "storeId": store_id,
        "section": section,
        "timestamp": current_timestamp,
        "count": random_count
    }

    url = "https://shoptrafficfunc.azurewebsites.net/api/log_visit?code=TWÓJ_CODE_TUTAJ"

    try:
        response = requests.post(url, json=request_body)
        if response.status_code == 200:
            logging.info(f'Wysłano dane: {request_body}')
        else:
            logging.error(f'Błąd: {response.status_code} {response.text}')
    except Exception as e:
        logging.error(f'Wyjątek: {e}')
