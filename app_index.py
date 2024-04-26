from flask import Flask, render_template, request

email_base = 'nik207b@gmail.com'
login_base = 'login admin'
password_base = '887293774799924773'



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')



@app.route('/form_in_user')
def form_in_user():
    return render_template("user/in_user.html")



@app.route('/in_user_processing', methods = ['POST'])
def in_user_processing():
    if request.method == 'POST':
        var_email = request.form['email']
        var_login = request.form['login']
        var_password = request.form['password']
        if var_email == email_base and var_login == login_base and var_password == password_base:
            return render_template('user/user_page.html')
        else:
            return render_template('error_page.html')
        

@app.route('/form_in_admin')
def form_in_admin():
    return render_template("admin/in_admin.html")


@app.route('/in_admin_processing', methods = ['POST'])
def in_admin_processing():
    if request.method == 'POST':
        var_login = request.form['login']
        var_password = request.form['password']
        if var_login == login_base and var_password == password_base:
            return render_template('admin/admin_page.html')
        else:
            return render_template('error_page.html')

    
    

if __name__ == '__main__':
    app.run(debug=True)

    
