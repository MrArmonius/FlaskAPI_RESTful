from flask import Flask, current_app
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import werkzeug

from datetime import datetime
from queue import Queue





# A queue for jobs where client is producer and cura engine is consummer
jobQueue = Queue(maxsize=3)

# A List of Dicts to store all of the books
jobs = {}

# "xUi7aze":{
#     "job_id": "xUi7aze",
#     "path_file": "eFgr",
#     "status": "In Queue",
#     "last-seen": datetime.now(),
#     "result": 4.17
# },
# "xUi8aze":{
#     "job_id": "xUi8aze",
#     "path_file": "eFgr",
#     "status": "In Queue",
#     "last-seen": datetime.now(),
#     "result": 4.17
# }

# jobQueue.put(jobs["xUi7aze"])
# jobQueue.put(jobs["xUi8aze"])
# Schema For the Book Request JSON
jobFields = {
    "job_id": fields.String,
    "path_file": fields.String,
    "status": fields.String,
    "last-seen": fields.String,
    "result": fields.Float,
    "time": fields.Integer,
    "filament_used": fields.Float,
    "layer_height": fields.Float,
    "minx": fields.Float,
    "miny": fields.Float,
    "minz": fields.Float,
    "maxx": fields.Float,
    "maxy": fields.Float,
    "maxz": fields.Float,
    "filament_volume": fields.Integer
}



def create_app(test_config=None):
    # Initialize Flask
    app = Flask(__name__)
    api = Api(app)
    
    from .config import DevelopmentConfig
    app.config.from_object(DevelopmentConfig()) 

    from .jobList import JobList
    api.add_resource(JobList, "/jobs")

    from .job import Job
    api.add_resource(Job, "/jobs/<id>")

    @app.before_first_request
    def _run_thread():
        # Launch thread consummer
        from .consumer import Consumer
        #Number of workers
        for _ in range(1):
            cons = Consumer(jobQueue, jobs)
            cons.daemon = True
            cons.start()
    

    return app


