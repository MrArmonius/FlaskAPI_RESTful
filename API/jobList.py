from . import jobs,jobFields
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

class JobList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "title", type=str, required=True, help="The title of the job must be provided", location="json")
        self.reqparse.add_argument(
            "author", type=str, required=True, help="The author of the job must be provided", location="json")
        self.reqparse.add_argument("length", type=int, required=True,
                                   help="The length of the job (in pages)", location="json")
        self.reqparse.add_argument(
            "rating", type=float, required=True, help="The rating must be provided", location="json")

    def get(self):
        return{"jobs": [marshal(job, jobFields) for job in jobs]}

    def post(self):
        args = self.reqparse.parse_args()
        job = {
            "id": jobs[-1]['id'] + 1 if len(jobs) > 0 else 1,
            "title": args["title"],
            "author": args["author"],
            "length": args["length"],
            "rating": args["rating"]
        }

        jobs.append(job)
        return{"job": marshal(job, jobFields)}, 201
