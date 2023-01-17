# FlaskAPI_RESTful
API RESTFUL based on Flask to queue jobs for CuraEngine

## Set-Up and Launch Flask
We need to export the environment variable `FLASK_APP=API` and `FLASK_ENV=development`.
To launch the application, just run in the repository root:
```
flask run
```

## Send JSON command for API_Example
To send JSON follows this command: 

```
curl -X POST http://127.0.0.1:5000/books/2
   -H 'Content-Type: application/json'
   -d '{"title":"my_title","length":100}'
```

For simple Get Request:
```
curl http://127.0.0.1:5000/books
```

## POST one JOB in the queue
To send one stl file with a JSON payload for the id;

```
curl -F 'file=@sample1.stl' -F data='{"job_id":"erwan"}' http://localhost:5000/jobs
```
**IMPORTANT**: the json syntax must be `'{"key": "value"}'` and not `"{'key': 'value'}"` else throw the error `"data": "Bad JSON encode"`

Later, we will add the configuration file of curaengine.

## The API use Queue library and Async function
The API have two main jobs, the one is to answer the request send from the user and the seconde is to consume these jobs. Indeed we can't afford to stop the server http and his answer while python do a job. So we have a synchronized queue, like this we can answer and our async function can consume.
For thesubprocess we use Popen. Like this we can read the avancement of the process in direct and update the list.