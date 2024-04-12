from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/user_reg')
def user_reg():
    return render_template("user/registr_user.html")

if __name__ == '__main__':
    app.run(debug=True)