from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_api():
    return "successful api request."

@app.route('/<string:name>')
def get_name(name):
    return f"hello {name}, How are you?"
    # return 'hello there'

@app.route('/blog/<int:blog_id>')
def get_blog(blog_id):
    return f"This is the blog no: {blog_id}"

@app.route('/revision/<float:rev_no>')
def get_revision_number(rev_no):
    return f"Version: {rev_no}"

if __name__ == '__main__':
    app.run(port=5050)

