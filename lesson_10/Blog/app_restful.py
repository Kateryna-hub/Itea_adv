from flask import Flask
from flask_restful import Api
from .resources import PostResource

app = Flask(__name__)
api = Api(app)


api.add_resource(PostResource, '/post', '/post/author/<string:author>', '/post/tag/<string:tag>', '/post/<string:id>')

