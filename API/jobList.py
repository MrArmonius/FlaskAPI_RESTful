from . import jobs,jobFields,jobQueue
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import werkzeug
from werkzeug.utils import secure_filename

from datetime import datetime
import json

from flask import current_app as app

class JobList(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "file", type=werkzeug.datastructures.FileStorage, location='files', required=True, help="Provide a file please")
        self.reqparse.add_argument(
            "data", location='form', required=True, help="Provide metadata")


        self.PATH_FOLDER_GCODE = "stl/"
        #self.reqparseData = reqparse.RequestParser()
        #self.reqparseData.add_argument(
        #    "job_id", type=str, required=True, help="The job_id must be indicated", location="json")
        

    def get(self): 
        print(app.config['CURAENGINE'])
        return{"jobs": [marshal(job, jobFields) for _, job in jobs.items()]}

    def post(self):
        args = self.reqparse.parse_args()
        try:
            data = json.loads(args["data"])
            job_id = secure_filename(data["job_id"])
        except ValueError:
            return{"data": "Bad JSON encode"}, 401
        except KeyError:
            return{"data": "Don't find job_id"}, 402
        if jobQueue.full():
            abort(405)
        
        path_file = self.PATH_FOLDER_GCODE + job_id + ".stl"
        job = {
            "job_id": job_id,
            "path_file": path_file,
            "status": "In Queue",
            "last-seen": str(datetime.now()),
            "result": 0.0
        }
        stl_file = args["file"]
        stl_file.save(path_file)

        #jobs[job["job_id"]]= job
        #jobQueue.put(job)
        return{"job": marshal(job, jobFields)}, 201
