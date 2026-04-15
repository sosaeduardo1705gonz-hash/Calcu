from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", resultado="")

@app.route("/aritmetica", methods=["POST"])
def aritmetica():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    op = request.form["op"]
    if op == "+": res = num1 + num2
    elif op == "-": res = num1 - num2
    elif op == "*": res = num1 * num2
    elif op == "/": res = num1 / num2
    return render_template("calcu.html", resultado=res)

@app.route("/binaria", methods=["POST"])
def binaria():
    b1 = int(request.form["bin1"], 2)
    b2 = int(request.form["bin2"], 2)
    op = request.form["op"]
    if op == "AND": res = b1 & b2
    elif op == "OR": res = b1 | b2
    elif op == "XOR": res = b1 ^ b2
    return render_template("calcu.html", resultado=bin(res)[2:])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

