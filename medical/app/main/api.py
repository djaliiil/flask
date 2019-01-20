from app.models.event import Event
from flask_restful import Resource, reqparse, inputs
 
from app import db
from sqlalchemy.orm import joinedload

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ProductList(Resource):

  
  
    def get(self):
        data = [product.to_dict() for product in Event.all_items()]
        return data, 200

