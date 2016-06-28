from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='/static')

import mgmt

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route("/toggle")
def handle():
	conn = mgmt.Manager('/dev/cu.wchusbserial1410',9600)
	conn.toggle()
	return("0")

if __name__ == "__main__":
    app.run()
