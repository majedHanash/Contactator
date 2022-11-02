from pickletools import read_unicodestring1
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_ckeditor import CKEditor
from post_request import handle_post_request

load_dotenv()
app = Flask(__name__)
ckeditor = CKEditor(app)
# print(ml_back.generate_email2())


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        result, data = handle_post_request(request)
        result = result.replace('\n', '</br>')
        # return redirect(url_for("index", result=result))
        return render_template("index.html", result=result, data=data)

    return render_template("index.html")
