from flask import Blueprint
from app.services.testServices.controller import testController
from app import routeHandlers

router = Blueprint('test',__name__)
apiPrefix = "/test"

@router.get("/test")
def testing():
    return testController.testing()