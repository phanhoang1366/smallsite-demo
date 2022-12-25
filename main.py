from flask import Flask, request, session, url_for, redirect, render_template, Response
import secrets

app = Flask(__name__, template_folder=".")
app.secret_key = secrets.token_bytes()

css_file = open("output.css", "r")
css_contents = css_file.read()
css_file.close()

@app.after_request
def after_request_callback(response: Response):
  print(response.__dict__)
  if response.headers["Content-Type"].startswith("text/html"):
    updated = render_template("template.html", status=response.status_code, message=response.response[0].decode())
    response.set_data(updated)
  return response

@app.errorhandler(404)
def not_found(e):
    return "Not Implemented (I'm lazy)", 501
    return render_template("template.html", status=501, message="Not Implemented (I'm lazy)"), 501

@app.route("/")
def home():
    return "OK", 200
    return render_template("template.html", status=200, message="OK")

@app.route("/output.css")
def robots():
    return css_contents, 200, {'Content-Type': 'text/css'}
