from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

from datetime import datetime
from queue import Queue


# A List of Dicts to store all of the books
jobs = [{
    "job_id": 1,
    "path_file": "/path/to/my/file",
    "status": "In Queue",
    "last-seen": datetime.now(),
    "result": 4.17
}
]


# Schema For the Book Request JSON
jobFields = {
    "job_id": fields.Integer,
    "path_file": fields.String,
    "status": fields.String,
    "last-seen": fields.String,
    "result": fields.Float
}

def create_app(test_config=None):
    # Initialize Flask
    app = Flask(__name__)
    api = Api(app)

    
    from .jobList import JobList
    api.add_resource(JobList, "/jobs")

    from .job import Job
    api.add_resource(Job, "/jobs/<int:id>")

    return app


#if __name__ == "__main__":
#    app.run(debug=True)


