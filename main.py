from flask import Flask, render_template
import requests
from pytrends.request import TrendReq
import datetime

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
     gtag('config', 'UA-250999446-1');
    </script>
    """
    return prefix_google + "Hello World"

@app.route('/logger', methods=['GET'])
def print_msg():
    loginfo = "This is my log"
    app.logger.warning(loginfo)
    app.logger.error(loginfo)
    app.logger.info(loginfo)

    return render_template('log.html', loginfo="This is my log")

@app.route('/reqGoogle', methods=['GET'])
def req_google():
    req = requests.get("https://www.google.com/")
    return req.cookies.get_dict()

@app.route('/reqGA', methods=['GET'])
def req_ga():
    req = requests.get('https://analytics.google.com/analytics/web/#/p345032521/reports/intelligenthome')
    return req.text

@app.route('/pytrends')
def googletrendchart():
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=["Ryan Air", "Transavia"], timeframe='today 90-d', geo='FR')
    df = pytrends.interest_over_time()
    data_ryan_air = df['Ryan Air'].tolist()
    data_transavia = df['Transavia'].tolist()
    data_date = df.index.values.tolist()
    timestamp_in_seconds = [element/1e9 for element in data_date]
    date = [datetime.fromtimestamp(element)for element in timestamp_in_seconds]
    days = [element.date() for element in date]
    months = [element.isoformat() for element in days]
    params = {
        "type": 'line',
        "data": {
            "labels": months,
            "datasets": [{
                "label": 'Ryan Air',
                "data": data_ryan_air,
                "borderColor": '#3e95cd',
                "fill": 'false',
            },
                {
                "label": 'Transavia',
                "data": data_transavia,
                "borderColor": '#ffce56',
                "fill": 'false',
            }
            ]
        },
        "options": {
            "title": {
                # + str(topic_1) + " et " + str(topic_2)
                "text": 'Comparaison entre'
            },
            "scales": {
                "yAxes": [{
                    "ticks": {
                        "beginAtZero": 'true'
                    }
                }]
            }
        }
    }

    prefix_chartjs = """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
         <canvas id="myChart" width="1200px" height="700px"></canvas>""" + f"""
        <script>
        var ctx = document.getElementById('myChart');
        var myChart = new Chart(ctx, {params});
        </script>
        """

    return prefix_chartjs
