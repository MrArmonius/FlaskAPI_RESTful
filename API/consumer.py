import subprocess
import sys
from threading import Thread
import time

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
            self.jobs[job["job_id"]]["status"] = "In Process"

            # launch subprocess CuraEngine with path_file, path_json, output
            process = subprocess.Popen(['CuraEngine', '"Hello stdout"'], stdout=subprocess.PIPE)

            # While curaengine isn't finished, update the status
            while process.poll() is None:
                # read only one line
                output = process.stdout.readline()
                print(output, file=sys.stderr)
                # Time refresh status in seconds
                time.sleep(0.5)

            self.queue.task_done()
                
            # Change the status and go consume an other job and be sure to have 100.0% in result
            self.jobs[job["job_id"]]["result"] = 100.0
            self.jobs[job["job_id"]]["status"] = "Finish"