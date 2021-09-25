from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

contacts = [{
    "Contact": 939949994,
    "Name": 'Python',
    "done": False,
    "id": 1
}, {
    "Contact": 8774739555,
    "Name": 'pip',
    "done": False,
    "id": 2
}]


@app.route('/')
def main():
    return render_template("index.html")


@app.route("/getData")
def getData():
    return jsonify({"data": contacts})


@app.route("/postData", methods=["POST"])
def postData():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please post the data",
            "code": "404"
        })
    contact = {
        "Contact": request.json["Contact"],
        "Name": request.json["Name"],
        "done": False,
        "id": contacts[-1]["id"] + 1
    }

    contacts.append(contact)

    return jsonify({
        "status": "success",
        "message": "contact added successfully",
        "code": "200"
    })


if __name__ == '__main__':
    app.run(debug=True)
