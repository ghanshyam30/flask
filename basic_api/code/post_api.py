from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def user_info(name):
    return f"Congratulations {name}, we have registered you successfully. This is your workspace feel free to customize it...!"


@app.route('/user', methods = ['POST','GET'])
def register_user():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('user_info', name = user))
    else:
        user = request.args.get('name')
        # user = "default"
        return redirect(url_for('user_info', name = user))


if __name__ == '__main__':
    app.run(port=5050)
