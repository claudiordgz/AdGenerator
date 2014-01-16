__author__ = 'Claudio'

import YamlHandler

class HTMLBuilder(YamlHandler.YamlHandler):
    """ The HTML Builder handles the skeleton
    """
    def __init__(self, path, file):
        YamlHandler.YamlHandler.__init__(self, path, file)
        self.__store_skeleton()
        self.init = False
        if self.skeleton:
            self.init = True

    def __store_skeleton(self):
        self.skeleton = self.get()
        self.init = True

    def refresh(self):
        if not self.init:
            self.__store_skeleton()

"""
skeleton = get_skeleton(config['skeleton_path'], config['skeleton_file'])
    html_complete = ''.join(skeleton['default'])
    for css_object in skeleton['cssObjects']:
        html_complete = ''.join([html_complete, css_object])
    html_complete = append_politics(html_complete, skeleton['politics'])
    html_complete = assemble_description(html_complete, skeleton['description'],
                                         description, banner_list, header_complete)
    html_complete = gallery(html_complete, skeleton['gallery'], image_gallery, skeleton['remover'])
    if photo_gallery:
        html_complete = gallery(html_complete, skeleton['photos'], photo_gallery, skeleton['remover'])
    html_complete = ''.join([html_complete, skeleton['ending']])

"""

def main():
    obj = HTMLBuilder('../../../ads_yaml', 'main.yml')
    object = obj.get()
    print object

if __name__ == '__main__':
    main()