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
curl -X POST https://127.0.0.1:5000/books/2
   -H 'Content-Type: application/json'
   -d '{"title":"my_title","length":100}'
```

For simple Get Request:
```
curl https://127.0.0.1:5000/books
```