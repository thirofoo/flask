from flask import Flask, jsonify,request,render_template
import flask

app = Flask(__name__, static_folder='', static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return render_template('index.html',info=str(request.form['name']))
    else:
        return render_template('index.html',info='nothing')

@app.route("/image",methods=['GET'])
def image():
    return jsonify({
        "id": 1,
        "image": "./static/images/bg.jpg",
        "name": "through",
        "pwd": "hirohiro0724"
        })

if __name__ == "__main__":
    app.run(port=8000, debug=True)