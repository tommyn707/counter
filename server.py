from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "aaaaa"

@app.route('/')
def index():
    # IT'S THE FIRST TIME THE USER IS VISITING
    if 'num_visits' not in session:
        session['num_visits'] = 1
    # IT'S NOT THE FIRST TIME
    else:
        session['num_visits'] += 1
    return render_template("index.html")

@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")


app.run(debug=True)