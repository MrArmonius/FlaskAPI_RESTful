from . import jobs,jobFields
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

# Resource: Individual Job Routes
class Job(Resource):
    def __init__(self):
        # Initialize The Flsak Request Parser and add arguments as in an expected request
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("path_file", type=str, help="The path to the file must be indicated", location="json")

        super(Job, self).__init__()

    # GET - Returns a single job object given a matching id
    def get(self, id):
        job = [job for job in jobs if job['job_id'] == id]

        if(len(job) == 0):
            abort(404)

        return{"job": marshal(job[0], jobFields)}

    # PUT - Given an id
    def put(self, id):
        job = [job for job in jobs if job['job_id'] == id]

        if len(job) == 0:
            abort(404)

        job = job[0]

        # Loop Through all the passed agruments
        args = self.reqparse.parse_args()
        for k, v in args.items():
            # Check if the passed value is not null
            if v is not None:
                # if not, set the element in the jobs dict with the 'k' object to the value provided in the request.
                job[k] = v

        return{"job": marshal(job, jobFields)}

        # Delete - Given an id
    def delete(self, id):
        job = [job for job in jobs if job['job_id'] == id]

        if(len(job) == 0):
            abort(404)

        jobs.remove(job[0])

        return 201