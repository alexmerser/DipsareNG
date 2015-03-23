# -*- coding: utf-8 -*-
"""
	Stack core WSGI module
"""
from werkzeug.contrib.fixers import ProxyFix
from init import app

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
	app.run(host='localhost', port=5000)