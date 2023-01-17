from flask import current_app

import subprocess
import sys
from threading import Thread
import time
import io

# Function where we create a consummer, an object which consumme queue items in async. We use CuraEngine as subprocess and pipe out the output on a file.
# Every seconds we check the new status and update it on the dict.
# The queue is the same for all consummers.

class Consumer(Thread):
    def __init__(self, queue, jobs, ):
        Thread.__init__(self)
        self.queue = queue
        self.jobs = jobs
        self.app = current_app._get_current_object()

    def run(self):
        with self.app.app_context():
            while True:
                # get the job if the queue isn't empty, if the queue is empty wait a job comes.
                job = self.queue.get()
                
                # change the state of map "In Queue" to "In Process"
                self.jobs[job["job_id"]]["status"] = "Slicing"

                # launch subprocess CuraEngine with path_file, path_json, output
                # Maybe use Popen if we have very trouble about the execution time
                INPUT = self.app.config['PATH_STL'] + job["path_file"] + ".stl"
                OUTPUT = self.app.config['PATH_GCODE'] + job["path_file"] + ".gcode"
                process = subprocess.run([self.app.config['CURAENGINE'], 'slice', '-v', '-p', '-j', self.app.config['FDMPRINTER_DEF'], '-j', self.app.config['DEFAULT_PRINTERDEF'], '-l', INPUT, '-o', OUTPUT], universal_newlines=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


                print("Return code curaengine: ", process.returncode)
                lines = process.stdout.split("\n")
                for line in lines[-20:]:
                        print(line)
                
                if process.returncode == 0:
                    #change status of our process
                    self.jobs[job["job_id"]]["result"] = 80.0
                    self.jobs[job["job_id"]]["status"] = "Saving meta-data"

                    #test every line and find the ones which are important (i.e. length of filament, time of the print, weight of filament) and transform them in JSON to save it in DB
                    lines = process.stdout.split("\n")
                    for line in lines[-20:]:
                        print(line)
                    
                        
                    # Change the status and go consume an other job and be sure to have 100.0% in result
                    self.jobs[job["job_id"]]["result"] = 100.0
                    self.jobs[job["job_id"]]["status"] = "Finish"
                
                 
                self.queue.task_done()
