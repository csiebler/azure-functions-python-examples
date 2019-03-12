import logging
import azure.functions as func

def main(documents: func.DocumentList) -> func.Document:

    logging.info(f"CosmosDB trigger executed!")

    for doc in documents:
        logging.info(f"Document: {doc.to_json()}")

    returnDoc = func.Document.from_dict({"text": "Hello World", "foo": "bar"})
    return returnDoc
