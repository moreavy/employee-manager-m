import database as DB
from os import path
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)
title = "Employee Manager M"


def format_dob(d, m, y):
    return d+"/"+m+"/"+y


def add_employee(name: str, post: str, day: int, month: int, year: int, salary: int):
    employees = DB.get("employees")
    to = {
        "name": name,
        "posting": post,
        "dob": {
            "day": day,
            "month": month,
            "year": year,
        },
        "salary": salary,
    }
    employees.append(to)
    DB.set("employees", employees)


@app.route("/")
def start():
    return redirect(url_for("workspace"))


@app.route("/workspace")
def workspace():
    return render_template("index.html.jinja", title=title, db=DB ,employees=DB.get("employees"), url_for=url_for, format_dob=format_dob)


@app.route("/add", methods=["POST"])
def add():
    if request.method.upper() == "POST":
        name = request.form.get("name")
        posting = request.form.get("posting")
        day = request.form.get("day")
        month = request.form.get("month")
        year = request.form.get("year")
        salary = request.form.get("salary")
        add_employee(name=name, post=posting, day=day,
                     month=month, year=year, salary=salary)
    return redirect(url_for("workspace"))


@app.route("/delete", methods=["POST"])
def delete():
    if request.method.upper() == "POST":
        id = request.form.get("id")
        employees = DB.get("employees")
        employees.pop(int(id))
        DB.set("employees", employees)
    return redirect(url_for("workspace"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html.jinja", error=error)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
