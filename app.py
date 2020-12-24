from flask import Flask, jsonify, send_file, request
import db
app = Flask(__name__)

@app.route('/init')
def flask_mongodb_atlas():
    data = []
    data.append(1)
    data.append(2)
    data.append("flask mongodb atlas!")
    return jsonify(data)


#test to insert data to the data base
@app.route("/test")
def test():
    db.db.collection.insert_one({"name": "John"})
    return "Connected to the data base!"

@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'sample.png'
    else:
       filename = 'sample.png'
    return send_file(filename, mimetype='image/gif')

if __name__ == '__main__':
    app.run(port=8000)