from flask_restful import Api, Resource

from App.models import HomeBaner

api = Api()


def init_api(app):
    api.init_app(app)


class HomeResource(Resource):
    def get(self):
        homebaners = HomeBaner.query.all()
        return {'msg': 'hello test'}


api.add_resource(HomeResource, '/home/')
