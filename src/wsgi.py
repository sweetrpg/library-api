__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
wsgi.py
- WSGI entrypoint.
"""

from sweetrpg_shelf_api.application.main import create_app


app = create_app()
