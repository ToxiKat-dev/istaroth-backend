from flask import Flask
from app.services.testServices import testRoutes

def addRoutes(app:Flask):
     app.register_blueprint(testRoutes.router,url_prefix=testRoutes.apiPrefix)