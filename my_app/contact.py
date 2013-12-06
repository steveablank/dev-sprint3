import flask, flask.views
import os
import utils

class Contact(flask.views.MethodView):
	@utils.login_required
	def get(self):
		return flask.render_template('contact.html')