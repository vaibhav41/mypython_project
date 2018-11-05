from flask import Flask,redirect, render_template
##from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
#    return render_template('test.html')
     return "congratulation you have successfully deploued Flask Web  App!"
 
@app.route("/hello/")
def hello():
    return render_template('index.html')
    #return render_template('test.html')
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
