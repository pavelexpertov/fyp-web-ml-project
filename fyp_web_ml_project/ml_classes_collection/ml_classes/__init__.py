def _import_package_files():
    """ Dynamically import all the public attributes of the python modules in this
        file's directory (the package directory) and return a list of their names.
    """
    import os
    exports = []
    globals_, locals_ = globals(), locals()
    package_path = os.path.dirname(__file__)
    package_name = os.path.basename(package_path)
    package_name = 'fyp_web_ml_project.ml_classes_collection.' + package_name

    for filename in os.listdir(package_path):
        modulename, ext = os.path.splitext(filename)
        if modulename[0] != '_' and ext in ('.py', '.pyw'):
            subpackage = '{}.{}'.format(package_name, modulename) # pkg relative
            module = __import__(subpackage, globals_, locals_, [modulename])
            modict = module.__dict__
            names = (modict['__all__'] if '__all__' in modict else
                     [name for name in modict if name[0] != '_'])  # all public
            exports.extend(names)
            globals_.update((name, modict[name]) for name in names)

    return exports


if __name__ != '__main__':
    __all__ = ['__all__'] + _import_package_files()  # '__all__' in __all__
