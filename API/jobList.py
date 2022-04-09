from . import jobs,jobFields,jobQueue
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

from datetime import datetime

class JobList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "path_file", type=str, required=True, help="The path to the file must be indicated", location="json")
        self.reqparse.add_argument(
            "job_id", type=str, required=True, help="The job_id must be indicated", location="json")
        

    def get(self): 
        return{"jobs": [marshal(job, jobFields) for _, job in jobs.items()]}

    def post(self):
        args = self.reqparse.parse_args()
        if jobQueue.full():
            abort(405)
        job = {
            "job_id": args["job_id"],
            "path_file": args["path_file"],
            "status": "In Queue",
            "last-seen": str(datetime.now()),
            "result": 0.0
        }

        jobs[job["job_id"]]= job
        jobQueue.put(job)
        return{"job": marshal(job, jobFields)}, 201
