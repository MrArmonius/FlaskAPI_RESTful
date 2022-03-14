from . import books,bookFields
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

# Resource: Individual Book Routes
class Book(Resource):
    def __init__(self):
        # Initialize The Flsak Request Parser and add arguments as in an expected request
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", type=str, location="json")
        self.reqparse.add_argument("author", type=str, location="json")
        self.reqparse.add_argument("length", type=int, location="json")
        self.reqparse.add_argument("rating", type=float, location="json")

        super(Book, self).__init__()

    # GET - Returns a single book object given a matching id
    def get(self, id):
        book = [book for book in books if book['id'] == id]

        if(len(book) == 0):
            abort(404)

        return{"book": marshal(book[0], bookFields)}

    # PUT - Given an id
    def put(self, id):
        book = [book for book in books if book['id'] == id]

        if len(book) == 0:
            abort(404)

        book = book[0]

        # Loop Through all the passed agruments
        args = self.reqparse.parse_args()
        for k, v in args.items():
            # Check if the passed value is not null
            if v is not None:
                # if not, set the element in the books dict with the 'k' object to the value provided in the request.
                book[k] = v

        return{"book": marshal(book, bookFields)}

        # Delete - Given an id
    def delete(self, id):
        book = [book for book in books if book['id'] == id]

        if(len(book) == 0):
            abort(404)

        books.remove(book[0])

        return 201
