from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-library-model",
    install_requires=[
        "Authlib",
        "blinker",
        "dnspython<2.0.0",
        "Flask-Caching",
        "Flask-Cors",
        "Flask-DotEnv",
        "Flask-REST-JSONAPI",
        "Flask-Session",
        "Flask>=2.0",
        "Flask-Migrate",
        "Flask-MongoEngine",
        "gunicorn",
        "kanka",
        "python-dateutil",
        "python-dotenv",
        "python-editor",
        "PyYAML",
        "redis",
        "requests",
        "sentry-sdk",
        "analytics-python<2.0",
        "sweetrpg-db @ git+https://github.com/sweetrpg/db.git@develop",
        "sweetrpg-model-core @ git+https://github.com/sweetrpg/model-core.git@develop",
        "sweetrpg-api-core @ git+https://github.com/sweetrpg/api-core.git@develop",
        "sweetrpg-library-model @ git+https://github.com/sweetrpg/library-model.git@develop",
    ],
    extras_require={},
)
