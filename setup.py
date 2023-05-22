from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-library-api",
    install_requires=[
        "analytics-python~=1.0",
        "blinker~=1.6",
        "dnspython~=2.0",
        "Flask-Caching~=2.0",
        "Flask-CORS~=3.0",
        "Flask-DotEnv~=0.1",
        "Flask-Migrate",
        "Flask-MongoEngine",
        "Flask-OAuthlib",
        "Flask-REST-JSONAPI",
        "Flask-Session~=0.5",
        "Flask-Swagger~=0.2",
        "Flask~=2.0",
        "hiredis~=2.2",
        "kanka",
        "prometheus-flask-exporter~=0.22",
        "PyMongo[srv]==4.0.2",
        "python-dateutil~=2.8",
        "python-dotenv~=0.21",
        "python-editor~=1.0",
        "python-logstash-async~=2.5",
        "PyYAML~=6.0",
        "redis~=4.5",
        "requests~=2.31",
        "sentry-sdk[flask]~=1.23.0",
        "sweetrpg-api-core",
        "sweetrpg-db",
        "sweetrpg-library-objects",
        "sweetrpg-model-core",
        "sweetrpg-web-core",
        "urllib3~=1.26",
    ],
    extras_require={},
)
