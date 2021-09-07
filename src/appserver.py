__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
appserver.py
- creates an application instance and runs the dev server
"""

if __name__ == '__main__':
    from sweetrpg.library.api.application.main import create_app
    app = create_app()
    app.run('0.0.0.0', app.config['PORT'])