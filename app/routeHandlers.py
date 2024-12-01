from uuid import uuid4
from app import config
from functools import wraps
from flask import Flask, request
from app.utils.loggerUtils import logger
from app.models.responseModel import APIResponse

def staticProtect(f):
    @wraps(f)
    def func(*args,**kwargs):
        apiToken = request.headers.get('apiToken')
        if not apiToken or apiToken != config.ACCESS_TOKEN:
            return APIResponse(
                status=False,
                statusCode=401,
                message="Unauthorized Access",
            )
        else: return f(*args,**kwargs)
    return func

def loginProtect(f):
    @wraps(f)
    def func(*args,**kwargs):
        return f(*args,**kwargs)
    return func

def errorHandler(f):
    @wraps(f)
    def func(*args,**kwargs):
        requestId = uuid4()
        request.id = requestId
        requestLog = {
            "RequestId" : requestId,
            "Origin" : request.origin,
            "Endpoint" : request.path,
            "Method" : request.method,
        }
        if request.files:
            requestLog["Files"] = [ file.filename for file in request.files.values()]
        else:
            requestLog["Data"] = request.get_data(as_text=True)
        logger.info(f"Request : \n\t{_dict_to_log_string(requestLog)}")
        try:
            response = f(*args,**kwargs)
            if isinstance(response,APIResponse):
                response.update()
                responseLog = {
                    "RequestId" : requestId,
                    "StatusCode" : response.statusCode,
                    "Status" : response.status,
                    "Message" : response.message,
                }
                if response.log:
                    responseLog["data"] = response.data
                api_log = response.getLog()
                if api_log: responseLog["API Log"] = api_log
                logger.info(f"Response : \n\t{_dict_to_log_string(responseLog)}")
                return response.get_response()
            else:
                print(response,type(response),sep="\n\n")
                raise TypeError("Invalid Response Type")
        except Exception as e:
            logger.exception(f"Response : \n\tRequestId : {requestId}\n{e}\n")
            return APIResponse(
                statusCode=500,
                status=False,
                message="Something went wrong"
            ).get_response()
    return func

def addErrorHandler(app:Flask):
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            view_func = app.view_functions[rule.endpoint]
            app.view_functions[rule.endpoint] = errorHandler(view_func)

def _dict_to_log_string(data:dict):
    return "\n\t".join(f"{key} : {data[key]}" for key in data.keys())
