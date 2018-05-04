from flask_restful import Api, Resource, fields, marshal_with

from App.ext import db
from App.models import HomeBaner
from utills.dbutills import add_baner

api = Api()


def init_api(app):
    api.init_app(app)


baner_fields = {
    'id': fields.Integer,
    'image': fields.String,
    'name': fields.String,
    'trackId': fields.String
}

result_fields = {
    'msg': fields.String,
    'baner': fields.List(fields.Nested(baner_fields))
}


class HomeResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        homebaners = HomeBaner.query.all()
        return {'msg': 'hello test', 'baner': homebaners}

    def put(self):
        add_baner(db)
        return {'msg': 'ok'}


api.add_resource(HomeResource, '/home/')
