from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from datetime import datetime

# create flask instance
app = Flask(__name__)
api = Api(app)

# define board list
boards = {
    '1' : {'user':'jiyoung', 'write_date' : '2020-12-19', 'title' : 'today', 'contents' : "Today is saturday.\nAnd I watched a series called 'Friends' all day long. It was so fun."},
    '2' : {'user':'youngji', 'write_date' : '2020-12-20', 'title' : 'wannabe', 'contents' : "I just want to be a rich jobless."}
}

parser = reqparse.RequestParser()
parser.add_argument('user', 'write_date', 'title', 'contents')

# define route for pages
@app.route("/")
def template_boards():
    return render_template(
        'index.html',
        board_dict=boards
    )
@app.route("/boards/<string:post_id>")
def template_posts(post_id):
    board_dict = dict()
    if post_id in boards:
        board_dict = boards[post_id]
    return render_template(
        'post.html',
        board_dict=board_dict
    )

# api for boards page
class Board(Resource):
    def get(self):
        return boards

# api for posting page
class Post(Resource):
    def get(self, post_id):
        post_not_exist(post_id)
        return boards[post_id]

    def delete(self, post_id):
        post_not_exist(post_id)
        del boards[post_id]
        return '', 204

    def post(self):
        args = parser.parse_args()
        post_id = str(len(boards) + 1)
        boards[post_id] = {'user':args['user'],
                           'write_date':get_current_date(),
                           'title':args['title'],
                           'contents':args['contents']
                           }
        return boards[post_id], 201

    def put(self, post_id):
        args = parser.parse_args()
        post = {'user':args['user'],
                'write_date':args['write_date'],
                'title': args['title'],
                'contents':args['contents']}
        boards[post_id] = post
        return post, 201

# exception
def post_not_exist(post_id):
    if post_id not in boards:
        abort(404, message="post {} doesn't exist.".format(post_id))

# get date
def get_current_date():
    return datetime.today().strftime("%Y-%m-%d")

# url mapping
api.add_resource(Board, '/boards/')
api.add_resource(Post, '/boards/<string:post_id>')

# run web server
if __name__ == '__main__':
    app.run(debug=True)