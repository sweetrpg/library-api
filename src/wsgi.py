__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""WSGI entrypoint.
"""

from sweetrpg_library_api.application.main import create_app


app = create_app()
