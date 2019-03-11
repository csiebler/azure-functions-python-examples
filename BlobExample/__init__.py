import logging
import azure.functions as func

def main(inputBlob: func.InputStream, outputBlob: func.Out[str]):
  
    logging.info(f"Blob trigger executed!")
    logging.info(f"Blob Name: {inputBlob.name} ({inputBlob.length}) bytes")
    logging.info(f"Full Blob URI: {inputBlob.uri}")

    output = "Hello World!"
    outputBlob.set(output)
