from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250999446-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', ' UA-250999446-1');
</script>
 """
 return prefix_google + "Hello World"

@app.route('/logger', methods=['GET'])
def printMsg():
    loginfo = "This is my log"
    app.logger.warning(loginfo)
    app.logger.error(loginfo)
    app.logger.info(loginfo)

    return render_template('log.html', loginfo = "This is my log")

@app.route('/reqGoogle', methods=['GET'])
def reqGoogle():
    req = requests.get("https://www.google.com/")
    return req.cookies.get_dict()

@app.route('/reqGA', methods=['GET'])
def myreqGA():
    req = requests.get('https://analytics.google.com/analytics/web/#/p345032521/reports/intelligenthome')
    return req.text