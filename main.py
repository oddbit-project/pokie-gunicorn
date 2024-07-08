from rick.resource.config import EnvironmentConfig
from pokie.config.template import BaseConfigTemplate
from pokie.core import FlaskApplication

from pokie_gunicorn.config import GunicornConfigTemplate


# base configuration
class Config(EnvironmentConfig, BaseConfigTemplate, GunicornConfigTemplate):
    pass


def build_pokie():
    # load configuration from ENV
    cfg = Config().build()

    # modules to load & initialize
    modules = [
        'pokie_gunicorn'
    ]

    # factories to run
    factories = []

    # build app
    pokie_app = FlaskApplication(cfg)
    flask_app = pokie_app.build(modules, factories)
    return pokie_app, flask_app


main, app = build_pokie()

# =============================================================================

if __name__ == '__main__':
    main.cli()
