import os
from time import time

from flask import Flask, g, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

# Prometheus metrics
REQUEST_COUNT = Counter(
    "flaskr_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "http_status"],
)
REQUEST_LATENCY = Histogram(
    "flaskr_request_latency_seconds",
    "Request latency in seconds",
    ["method", "endpoint"],
)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.before_request
    def _start_timer():
        g._start_time = time()

    @app.after_request
    def _record_metrics(response):
        try:
            request_latency = time() - g._start_time
        except Exception:
            request_latency = 0

        endpoint = request.endpoint or "unknown"
        REQUEST_LATENCY.labels(request.method, endpoint).observe(request_latency)
        REQUEST_COUNT.labels(request.method, endpoint, str(response.status_code)).inc()
        return response

    @app.route("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

    # register the database commands
    from . import db

    db.init_app(app)

    # apply the blueprints to the app
    from . import auth
    from . import blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app
