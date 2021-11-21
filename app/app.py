# %%
from flask import Flask, render_template, request
import os
# %%

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Get port and debug mode from environment variables    
    port = os.environ.get('dash_port')
    debug = os.environ.get('dash_debug')=="True"
    app.run(debug=debug, host="0.0.0.0", port=port)