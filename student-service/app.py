from flask import Flask, jsonify, request

app = Flask(__name__)
students = {"id":502,"studentName":"sampath", "totalMarks":30}          # id -> {"id": int, "studentName": str, "totalMarks": int}

@app.route("/students", methods=["GET"])
def get_all():
    return jsonify(list(students.values())), 200

@app.route("/students/<int:sid>", methods=["GET"])
def get_one(sid):
    if sid not in students:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(students[sid]), 200

@app.route("/students", methods=["POST"])
def create():
    data = request.get_json()
    sid = data.get("id")
    if sid is None or sid in students:
        return jsonify({"error": "id missing or already exists"}), 400
    students[sid] = {
        "id": sid,
        "studentName": data["studentName"],
        "totalMarks": data["totalMarks"],
    }
    return jsonify(students[sid]), 201

@app.route("/students/<int:sid>", methods=["PUT"])
def update(sid):
    if sid not in students:
        return jsonify({"error": "Student not found"}), 404
    data = request.get_json()
    students[sid]["studentName"] = data["studentName"]
    students[sid]["totalMarks"] = data["totalMarks"]
    return jsonify(students[sid]), 200

@app.route("/students/<int:sid>", methods=["DELETE"])
def delete(sid):
    if sid not in students:
        return jsonify({"error": "Student not found"}), 404
    del students[sid]
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)