__author__ = 'Claudio'

import yaml

class YamlHandler(object):
    """ I/O For Yaml
    """
    def __init__(self, path=None, filename=None):
        if path:
            self.path = path
        if filename:
            self.filename = filename

    def get(self):
        if self.path and self.filename:
            config = self.get_yaml(self.path, self.filename)
        else:
            config = None
        return config

    def get_yaml(self, path, filename):
        yaml_file = '{path}/{ad_skeleton}'.format(path=path, ad_skeleton=filename)
        with open(yaml_file, 'r') as f:
            yaml_file = yaml.load(f)
        return yaml_file
