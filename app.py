from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash

import os

app = Flask(__name__)

comments = []

# Display all things
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/comment', methods=['POST'])
def comment():
    if request.method == "POST":
        comm = request.form['comment']
        comments.append(comm)

    return redirect(url_for("main"))

@app.route('/level1', methods=["POST","GET"])
def level1():
    if request.method == "POST":
        return render_template('level1.html',search=True,query=request.form['search'])
    else:
        return render_template('level1.html',search=False)

@app.route('/level2', methods=["POST","GET"])
def level2():
    if request.method == "POST":
        comments.append(request.form['comment'])
    return render_template('level2.html',list=comments)

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run()
