import logging
import json
import azure.functions as func

def main(inMessage: func.QueueMessage, outMessage: func.Out[func.QueueMessage]):

    logging.info(f"Queue trigger executed!")
    logging.info(f"Message Id: {inMessage.id}")
    logging.info(f"Message Body: {inMessage.get_body()}")
    logging.info(f"Message Body as JSON: {inMessage.get_json()}")
    logging.info(f"Dequeue Count: {inMessage.dequeue_count}")
    logging.info(f"Insertion Time: {inMessage.insertion_time}")
    logging.info(f"Expiration Time: {inMessage.expiration_time}")
    logging.info(f"Time Next Visible: {inMessage.time_next_visible}")

    output = {'text': 'abc'}
    outMessage.set(json.dumps(output))
