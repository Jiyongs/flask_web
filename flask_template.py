from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template(
        'index.html',
        my_str="플라스크 웹 만들자",
        my_list=[x+1 for x in range(10)]
    )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)