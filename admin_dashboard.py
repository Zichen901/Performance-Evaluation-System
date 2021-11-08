from flask import Flask, json, render_template, url_for, request, redirect, jsonify
from flask.helpers import make_response
from connection import Database
from __main__ import app, secure_site, db

nav_columns = {"Overview":"/admin/overview", "Staff":"/admin/staff", "Families":"/admin/families", "Business":"/admin/business"}

@app.route("/admin/staff", methods = ["POST", "GET", "PUT", "DELETE"])
@secure_site
def admin_staff(auth_data = None):
    staff_table = db.query('Select * FROM staff')

    if request.method == 'GET':
        return render_template('admin.html',auth_data=auth_data, staff_table=staff_table)
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    return render_template('admin.html', auth_data=auth_data)