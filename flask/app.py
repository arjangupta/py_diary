# Arjan's first Flask program

from flask import Flask, render_template

app = Flask(__name__)

num_tacos = 0

@app.route('/')
def index(): #this function can be named anything. It defines the route of the landing page, i.e. '/'
    return render_template("index.html")

@app.route('/tacos', methods=['POST', 'GET'])
def tacos():
    global num_tacos
    print("You have hit the tacos endpoint")
    num_tacos += 1
    return render_template("tacos.html", tacos_requested=num_tacos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #0.0.0.0 means that this web app is accessible to any device on the current network