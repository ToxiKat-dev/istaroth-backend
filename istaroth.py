from flask import Flask
from flask_cors import CORS
from app import config
from app.services import routes
from app import routeHandlers

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
routes.addRoutes(app)

if __name__ == "__main__":
    routeHandlers.addErrorHandler(app)
    app.run(host=config.HOST,port=config.PORT,)