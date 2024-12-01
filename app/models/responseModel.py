from flask import jsonify

class APIResponse:
    def __init__(
            self,
            statusCode:int = None,
            status:bool = None,
            message:str = None,
            data = None,
            log:bool = True,
        ):
        self.statusCode = statusCode
        self.status = status
        self.message = message
        self.data = data
        self.log = log
        self._logs = []

    def update(self):
        if self.status != None:
            if self.statusCode == None:
                if self.status == True:
                    self.statusCode = 200
                else:
                    self.statusCode = 400
            if self.message == None:
                if self.status == True:
                    self.message = "API Call Sucessfull"
                else:
                    self.message = "something went wrong"
        else:
            raise ValueError("Status Not found")
        
    def addLog(self,message:str):
        self._logs.append(message)

    def getLog(self):
        if not self._logs:
            return None
        else:
            return_logs = ["=============== API LOGS ==============="]
            return_logs.extend(self._logs)
            return_logs.append("========================================")
            return "\n\t".join(str(log) for log in return_logs)

    def get_response(self):
        self.update()
        return jsonify(
            {
                "status" : self.status,
                "message" : self.message,
                "data" : self.data,
            }
        ), self.statusCode
