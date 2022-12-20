from flask import Flask, render_template

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

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/logger/')
# def logger():
#     return render_template('about.html')

# import logging

# @app.route('/logger', methods=["GET"])
# def printMsg():
#     app.logger.warning('testing warning log')
#     app.logger.error('testing error log')
#     app.logger.info('testing info log')
#     return "Check your console"

@app.route('/logger', methods=['GET'])
def printMsg():
    loginfo = "This is my log"
    app.logger.warning(loginfo)
    app.logger.error(loginfo)
    app.logger.info(loginfo)

    return render_template('log.html', loginfo = "This is my log")

# import sys

# print('This is error output', file=sys.stderr)
# print('This is standard output', file=sys.stdout)