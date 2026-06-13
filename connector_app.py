from flask import Flask, render_template, request, jsonify
from detector import detect_sqli   # ✅ use your fixed file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontpage.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    query = data.get("query", "")

    result = detect_sqli(query)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)