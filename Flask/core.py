from flask import Flask, redirect, url_for, render_template
#from Logger import LoggerCalls

#lc = LoggerCalls()
app = Flask(__name__)

@app.route("/")
def home():
    #lc.debug_call('Landing page called')
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    #lc.debug_call('About us page called')
    return render_template("about-us.html")

if __name__ == "__main__":
    app.run()
