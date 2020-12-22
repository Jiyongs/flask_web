from flask import Flask, render_template, request
from datetime import datetime
import connect_mongodb as mongo

# create flask instance
app = Flask(__name__)

# connect to mongodb
mongo_conn = mongo.connect_mongodb(db="jiyongs", collection="board")

# boards = {
#     '1' : {'user':'jiyoung', 'write_date' : '2020-12-19', 'title' : 'today', 'contents' : "Today is saturday.\nAnd I watched a series called 'Friends' all day long. It was so fun."},
#     '2' : {'user':'youngji', 'write_date' : '2020-12-20', 'title' : 'wannabe', 'contents' : "I just want to be a rich jobless."}
# }

# define route for pages
@app.route("/")
def template_boards():
    return render_template(
        'index.html',
        board_dict=mongo.find_boards(mongo_conn)
    )
@app.route("/boards/<string:post_id>")
def template_posts(post_id):
    board_dict = dict()
    boards = mongo.find_boards(mongo_conn)
    if post_id in boards:
        board_dict = boards[post_id]
    return render_template(
        'post.html',
        board_dict=board_dict,
        post_id=post_id
    )
@app.route("/new/", methods=['POST'])
def create_post():
    post = request.form
    post_dict = {'user': post['user'],
                       'write_date': get_current_date(),
                       'title': post['title'],
                       'contents': post['contents']
                }
    mongo.insert_one(mongo_conn, post_dict)
    return render_template(
        'index.html',
        board_dict=mongo.find_boards(mongo_conn)

    )
@app.route("/edit/", methods=['POST'])
def edit_post():
    post = request.form
    post_id = post['post_id']
    post_dict = {'user': post['user'],
                 'write_date': post['write_date'],
                 'title': post['title'],
                 'contents': post['contents']
                }
    mongo.update_boards(mongo_conn, post_id, post_dict)
    return render_template(
        'index.html',
        board_dict=mongo.find_boards(mongo_conn)
    )
@app.route("/delete/<string:post_id>")
def del_post(post_id):
    mongo.del_boards(mongo_conn, post_id)
    return render_template(
        'index.html',
        board_dict=mongo.find_boards(mongo_conn)
    )

# get current date
def get_current_date():
    return datetime.today().strftime("%Y-%m-%d")

# run web server
if __name__ == '__main__':
    app.run(debug=True)