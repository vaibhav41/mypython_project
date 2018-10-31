from flask import Flask, redirect, render_template
 
app = Flask(__name__)
 
@app.route("/")
def index():
#    return render_template('test.html')
     return "Congrtatulation you have successfully deployed Flask App!"
 
@app.route("/hello/")
def hello():
    return render_template('test.html')
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
