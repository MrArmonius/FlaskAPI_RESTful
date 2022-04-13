import subprocess
import sys
from threading import Thread
import time
import io

# Function where we create a consummer, an object which consumme queue items in async. We use CuraEngine as subprocess and pipe out the output on a file.
# Every seconds we check the new status and update it on the dict.
# The queue is the same for all consummers.

class Consumer(Thread):
    def __init__(self, queue, jobs):
        Thread.__init__(self)
        self.queue = queue
        self.jobs = jobs

    def run(self):
        while True:
            # get the job if the queue isn't empty, if the queue is empty wait a job comes.
            job = self.queue.get()
            
            # change the state of map "In Queue" to "In Process"
            self.jobs[job["job_id"]]["status"] = "Slicing"

            # launch subprocess CuraEngine with path_file, path_json, output
            # Maybe use Popen if we have very trouble about the execution time
            process = subprocess.Popen(['echo', 'lol1\n', 'lol2'], universal_newlines=True,stdout=subprocess.PIPE)

            #change status of our process
            self.jobs[job["job_id"]]["result"] = 80.0
            self.jobs[job["job_id"]]["status"] = "Saving meta-data"

            #test every line and find the ones which are important (i.e. length of filament, time of the print, weight of filament) and transform them in JSON to save it in DB
            lines = process.stdout.readlines()
            for line in lines:
                if "" in line:
                    #TODO
            
                
            # Change the status and go consume an other job and be sure to have 100.0% in result
            self.jobs[job["job_id"]]["result"] = 100.0
            self.jobs[job["job_id"]]["status"] = "Finish"
            self.queue.task_done()
