from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields


# A List of Dicts to store all of the books
jobs = [{
    "id": 1,
    "title": "Zero to One",
    "author": "Peter Thiel",
    "length": 195,
    "rating": 4.17
}
]


# Schema For the Book Request JSON
jobFields = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String,
    "length": fields.Integer,
    "rating": fields.Float
}

def create_app(test_config=None):
    # Initialize Flask
    app = Flask(__name__)
    api = Api(app)

    
    from .jobList import JobList
    api.add_resource(BookList, "/books")

    from .job import Job
    api.add_resource(Book, "/books/<int:id>")

    return app


#if __name__ == "__main__":
#    app.run(debug=True)


