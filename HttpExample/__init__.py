import logging
import azure.functions as func

def main(request: func.HttpRequest) -> func.HttpResponse:

    logging.info(f"HTTP trigger executed!")

    logging.info(f"Headers: {request.headers}")
    logging.info(f"Params: {request.params}")
    logging.info(f"Route Params: {request.route_params}")
    logging.info(f"Body: {request.get_body()}")

    try:
        logging.info(f"Body JSON: {request.get_json()}")
    except ValueError:
        pass
    

    return func.HttpResponse(f"Hello World!", status_code=200)
