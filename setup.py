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
        "gunicorn",
        "kanka",
        "pylint",
        "python-dateutil",
        "python-dotenv",
        "python-editor",
        "PyYAML",
        "redis",
        "requests",
        "sentry-sdk",
        "sweetrpg-db @ git+https://github.com/sweetrpg/db.git@develop",
        "sweetrpg-api-core @ git+https://github.com/sweetrpg/api-core.git@develop",
        "sweetrpg-library-model @ git+https://github.com/sweetrpg/library-model.git@develop",
    ],
    extras_require={},
)
