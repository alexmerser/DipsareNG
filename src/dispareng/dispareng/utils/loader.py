import os
import imp


def load_blueprints(app):
    """
        This method looks for any modules or packages in the given directory, loads them
        and then registers a blueprint - blueprints must be created with the name 'module'

    :param app: application instance
    """
    mod_path = app.config['MODULES']
    dir_list = os.listdir(mod_path)
    mods = {}

    for module in dir_list:
        if os.path.isdir(os.path.join(mod_path, module)) and os.path.exists(
                os.path.join(mod_path, module, '__init__.py')):
            f, filename, description = imp.find_module(module, [mod_path])
            mods[module] = imp.load_module(module, f, filename, description)
            blueprint = getattr(mods[module], 'module')
            if blueprint.name not in app.blueprints:
                app.register_blueprint(blueprint)
            else:
                app.logger.error("CONFLICT:{0} already registered.".format(
                    filename))

        # This part of code load blueprint from python module (for more flexibility to extend base system)
        elif os.path.isfile(os.path.join(mod_path, module)):
            name, ext = os.path.splitext(module)
            if ext == '.py' and not name == '__init__':
                f, filename, description = imp.find_module(name, [mod_path])
                mods[module] = imp.load_module(name, f, filename, description)
                blueprint = getattr(mods[module], 'module')
                if blueprint.name not in app.blueprints:
                    app.register_blueprint(blueprint)
                else:
                    app.logger.error("CONFLICT:{0} already registered.".format(
                        filename))