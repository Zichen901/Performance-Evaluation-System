from flask import Flask, json, render_template, url_for, request, redirect, jsonify
from flask.helpers import make_response
from connection import Database
from __main__ import app, secure_site, db

nav_columns = {"Home":"/coach/home", "Personal Information":"/coach/info"}

@app.route("/coach/home", methods = ["POST", "GET", "PUT", "DELETE"])
@secure_site
def coach_home(auth_data = None):
    return render_template("coach_home.html", auth_data = auth_data, nav_columns = nav_columns)

@app.route("/coach/info", methods = ["POST", "GET", "PUT", "DELETE"])
@secure_site
def coach_info(auth_data = None):
    return "/coach/info"