from flask import *

app=Flask(__name__)

# attractions route setting


# Pages
@app.route("/")
def index():
	return render_template("index.html")

# app.run(host="0.0.0.0", port=3000)
app.run(host="54.224.206.32", port=3000)
# app.run(port=3000)