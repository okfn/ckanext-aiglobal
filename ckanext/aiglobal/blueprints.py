from flask import Blueprint

from ckan.plugins import toolkit


aiglobal = Blueprint('aiglobal', __name__)


def home_redirect():
    return toolkit.redirect_to(controller='package', action='search')


aiglobal.add_url_rule('/', view_func=home_redirect)
