import logging
import azure.functions as func

def main(documents: func.DocumentList) -> func.DocumentList:

    logging.info(f"CosmosDB trigger executed!")

    for doc in documents:
        logging.info(f"Document: {doc.to_json()}")

    returnDocs = []
    for x in range(0, 3):
        newDoc = func.Document.from_dict({"text": str(x), "foo": "bar"})
        returnDocs.append(newDoc)

    return func.DocumentList(returnDocs)
