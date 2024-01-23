from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse

# from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

app = Flask(
    __name__,
    static_url_path="",
    static_folder="frontend/dist",
    template_folder="frontend/dist",
)


# CORS(app) #comment this on deployment
api = Api(app)


@app.route("/", defaults={"path": ""})
def serve(path):
    return send_from_directory(app.static_folder, "index.html")


api.add_resource(HelloApiHandler, "/api/hello")


if __name__ == "__main__":
    app.run(debug=True)

else:
    # In a production environment, it is recommended to serve static files using a dedicated web server
    # such as Nginx or Apache with WSGI. Adjust the configuration of the web server to efficiently handle
    # static content and proxy requests to the Flask application. This approach enhances performance
    # and provides better security compared to using Flask's built-in development server.
    print("Running in production mode")
