from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)

# Route to test connection
@app.route('/hello')
def hello():
    return "Hello, World!"

# Route to list users
@app.route('/users')
def list_users():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('users.html', users=users)

# Route to add a new user
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        mysql.connection.commit()
        return redirect(url_for('list_users'))
    return render_template('new_user.html')

# Route to get user details by id
@app.route('/users/<int:id>')
def user_detail(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    if user:
        return render_template('user_detail.html', user=user)
    else:
        return "User not found", 404

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return "Resource not found", 404

if __name__ == "__main__":
    app.run(debug=True)
