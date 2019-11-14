import ckan.plugins as p
import ckan.plugins.toolkit as toolkit

from ckanext.aiglobal import blueprints


class AiglobalPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IBlueprint)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'aiglobal')

    # IBlueprint

    def get_blueprint(self):
        return [blueprints.aiglobal]
