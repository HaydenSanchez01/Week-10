from flask import Flask, render_template, request

app = Flask(__name__)


# make a homepage 
@app.route('/')
def hompage():
    return render_template("homepage1.html")

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "Hayden"]
    return render_template('name.html', Sname=name, nameList=listOfNames)

@app.route('/Form', methods = ['GET', 'POST'])
def formDemo(name = None):
    if request.method == 'POST':
        name = request.form['name']
    return render_template('Form.html', name = name)
# add the option to run this file directly 
if __name__ == "__main__":
    app.run(debug=True)