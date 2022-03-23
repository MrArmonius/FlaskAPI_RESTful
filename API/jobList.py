from . import jobs,jobFields
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

from datetime import datetime

class JobList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "path_file", type=str, required=True, help="The path to the file must be indicated", location="json")
        

    def get(self):
        return{"jobs": [marshal(job, jobFields) for job in jobs]}

    def post(self):
        args = self.reqparse.parse_args()
        job = {
            "job_id": jobs[-1]['job_id'] + 1 if len(jobs) > 0 else 1,
            "path_file": args["path_file"],
            "status": "In Queue",
            "last-seen": str(datetime.now()),
            "result": 0.0
        }

        jobs.append(job)
        return{"job": marshal(job, jobFields)}, 201
