from flask import Flask, Response, request
from flask_restful import Api, Resource, abort
from mongoengine.errors import NotUniqueError, ValidationError

from database.db import initialize_db
from database.models import User


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "host": "mongodb://localhost/test_user_db"
}
api = Api(app)
initialize_db(app)


def get_user_or_404(user_id: int):
    try:
        return User.objects.get(id=user_id)
    except ValidationError:
        abort(404, message=f"User {user_id} doesn't exist")


class UserListView(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        try:
            user = User(**body).save()
        except NotUniqueError:
            abort(400, message=f"User {body['username']} already exist")
        except ValidationError:
            abort(400, message="ValidationError")
        response = {user.username: user.id}
        return Response(response, mimetype="application/json", status=201)


class UserView(Resource):
    def get(self, user_id: int):
        return Response(
            get_user_or_404(user_id).to_json(),
            mimetype="application/json",
            status=200
        )

    def delete(self, user_id: int):
        get_user_or_404(user_id).delete()
        return Response(
            "",
            status=204
        )

    def put(self, user_id: int):
        body = request.get_json()
        try:
            get_user_or_404(user_id).update(**body)
        except NotUniqueError:
            abort(400, message=f"User {body['username']} already exist")
        except ValidationError:
            abort(400, message="ValidationError")
        return Response(
            get_user_or_404(user_id).to_json(),
            mimetype="application/json",
            status=201
        )


api.add_resource(UserListView, "/users")
api.add_resource(UserView, "/users/<user_id>")


if __name__ == "__main__":
    app.run(debug=True)
