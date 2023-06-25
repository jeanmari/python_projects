#!/bin/python

from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
mysql = MySQL()

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "crud_flask"
mysql.init_app(app)

def fetch_all_tasks():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def fetch_task(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM tasks where id = %s"
    cursor.execute(query, id)
    result = cursor.fetchall()
    return result


@app.route("/")
def index():
    tasks = fetch_all_tasks()
    return render_template("home.html", tasks=tasks)

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/create/post', methods=["POST"])
def save_task():
    if request.method == "POST":
        short_description = request.form["short_desc"]
        description = request.form["desc"]
        cursor = mysql.connection.cursor()
        query = "INSERT INTO tasks (short_description, description) VALUES(%s, %s)"
        value = (short_description, description)
        exec = cursor.execute(query, value)
        mysql.connection.commit()
        cursor.close()
        if(exec):
            return redirect("/")
        else:
            return create()
    else: 
        return "Method not allowed!"
    
@app.route('/edit')
def edit():
    id = request.args.get("id")
    task = fetch_task(id)
    
    return render_template("edit.html", task=task)

@app.route('/update/', methods=['POST'])
def update():
    if request.form ["_method"] == "PATCH":
        id = request.form["id"]
        short_description = request.form["short_desc"]
        description = request.form["desc"]
        completed = request.form["completed"]
        cursor = mysql.connection.cursor()
        query = "UPDATE tasks set short_description=%s, description=%s, completed=%s WHERE id=%s"
        value = (short_description, description, completed, id)
        exec = cursor.execute(query, value)
        mysql.connection.commit()
        cursor.close()

        if(exec):
            return redirect('/')
        else:
            return redirect(f"/edit?id={id}")
    else:
        return "Method not allowed!"
    
@app.route('/delete', methods=['GET'])
def delete():
    id = request.args.get('id')
    cursor = mysql.connection.cursor()
    query = "DELETE FROM tasks WHERE id=%s"
    value = id
    exec = cursor.execute(query, value)
    mysql.connection.commit()
    cursor.close()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
