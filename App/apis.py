from flask_restful import Api, Resource

api = Api()


def init_api(app):
    api.init_app(app)


class HomeResource(Resource):
    def get(self):
        return {'msg': 'hello test'}


api.add_resource(HomeResource, '/home/')
