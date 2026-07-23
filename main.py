from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.post("/")
def file_event_handler():
    # Get the CloudEvent JSON payload
    event = request.get_json(silent=True)

    logging.info("Cloud Run Function started")

    if event:
        # Extract metadata
        bucket = event.get("bucket")
        filename = event.get("name")
        content_type = event.get("contentType")
        size = event.get("size")

        # Log metadata
        logging.info("Cloud Storage Event Metadata")
        logging.info(f"Bucket: {bucket}")
        logging.info(f"Filename: {filename}")
        logging.info(f"Content Type: {content_type}")
        logging.info(f"File Size: {size} bytes")

    else:
        logging.warning("No JSON payload received.")

    return {
        "status": "success"
    }, 200