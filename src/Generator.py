__author__ = 'Claudio'

import yaml

def readHtmlAsString(filename):
    """ Open the html file and put it in a string """
    with open(filename, "r") as in_file:
        html_text = in_file.read()
    return html_text

def html_path():
    """ The Path to the HMI Workspace """
    html_add_path = "C:/Users/Claudio/PycharmProjects/MLAdGenerator/res"
    return html_add_path

def input_html():
    """ Get the filename for the input objects """
    input_filename = "index.html"
    return input_filename

def static_img(img_name, img_href, img_id, img_src, img_class=None):
    """
    push an image object with its css object
    """
    if img_class is None:
        html_img = '<div name="{img_name}" class="float-container">\
         <a href="{img_href}">\
          <img id="{img_id}" class="smaller" src="{img_src}" />\
         </a>\
        </div>'.format(img_name=img_name, img_href=img_href, img_id=img_id, img_src=img_src)
    else:
        html_img = '<div name="{img_name}" class="{img_class}">\
         <a href="{img_href}">\
          <img id="{img_id}" class="smaller" src="{img_src}" />\
         </a>\
        </div>'.format(img_name=img_name, img_href=img_href, img_id=img_id, img_src=img_src, img_class=img_class)
    return html_img

def image_str_definer(gallery_name, idx, img, img_class):
    name = gallery_name+str(idx)
    image = static_img(name, img, gallery_name, img, img_class)
    return image

def gallery_generator(gallery_name, gallery, img_class=None):
    html_gallery = [image_str_definer(gallery_name, idx, img, img_class) for idx, img in enumerate(gallery)]
    return html_gallery

def list_of_images_strings(ad_home, ad_gallery, ad_format):
    if len(ad_format) == 1:
        images = [''.join([ad_home, image, '.', ad_format[0]]) for image in ad_gallery]
    else:
        images = [''.join([ad_home, image, '.', filetype]) for image, filetype in zip(ad_gallery, ad_format)]
    return images

def write_to_disk(file_name, html_complete):
    file_ = "{filename}".format(filename=file_name)
    text_file = open("../ads_output/{name}.html".format(name=file_), "w")
    text_file.write(html_complete)
    text_file.close()

def ad_and_photo():
    ad_name = 'galaxysII.yml'
    photo_size = 'float-half-page'
    return ad_name, photo_size

def fractal_home_url():
    fractal_home = 'http://www.claudiordgz.com/Fractal/images/'
    return fractal_home

def append_politics(html_complete, politics):
    html_complete = ''.join([html_complete, politics])
    return html_complete

def gallery(html_code, skeleton_gallery_type, gallery_list, skeleton_remover):
    html_complete = ''.join([html_code, skeleton_gallery_type['begin']])
    for idx, image in enumerate(gallery_list):
        lidx = idx + 1
        html_complete = ''.join([html_complete, image])
        if lidx is 3:
            html_complete = ''.join([html_complete, skeleton_remover])
    html_complete = ''.join([html_complete, skeleton_gallery_type['end']])
    return html_complete

def assemble_description(html_code, skeleton_description, ad_description, banner_complete, header_complete):
    html_complete = ''.join([html_code, skeleton_description['begin']])
    html_complete = ''.join([html_complete, header_complete])
    html_complete = ''.join([html_complete, skeleton_description['text']])
    if banner_complete is not None:
        for banner in banner_complete:
            html_complete = ''.join([html_complete, banner])
    html_complete = ''.join([html_complete, ad_description])
    html_complete = ''.join([html_complete, skeleton_description['end']])
    return html_complete

def get_images_from_configuration(home, gallery_name, image_list, image_format):
    image_gallery = list_of_images_strings(home, image_list, image_format)
    if image_gallery:
        image_gallery = gallery_generator(gallery_name, image_gallery)
    return image_gallery

def generate_banner(home, banner_gallery):
    banner_list = [''.join([home, banner[0], '.', banner[1]]) for banner in banner_gallery]
    banner_complete = ['<img name="BannerImage" class="smaller" \
        src="{bannerImg}" />'.format(bannerImg=banner) for banner in banner_list]
    return banner_complete

def generate_header(home, header_image):
    header_complete = ''.join([home, header_image[0], '.', header_image[1]])
    header_complete = static_img('HeaderImageMain', header_complete, 'HeaderImage', header_complete, 'float-half-page')
    return header_complete

def get_yaml(path, filename):
    yaml_file = '{path}/{ad_skeleton}'.format(path=path, ad_skeleton=filename)
    with open(yaml_file, 'r') as f:
        yaml_file = yaml.load(f)
    return yaml_file

def ad_configuration(path_to_ad, ad_name):
    return get_yaml(path_to_ad, ad_name)

def get_skeleton(path, filename):
    return get_yaml(path, filename)

def get_configuration(path, filename):
    return get_yaml(path, filename)

def main():
    """ DOCSTRING """
    config = get_configuration('', 'main_configuration.yml')
    ad_name, photo_size = ad_and_photo()
    ad = ad_configuration(config['ad_path'], ad_name)
    html_url = config['user_server_url']

    ad_home = ''.join([html_url, ad['path']])
    if ad['headerimg']:
        header_complete = generate_header(ad_home, ad['headerimg'])
    if ad['banner']:
        banner_list = generate_banner(ad_home, ad['banner'])

    description = ad['header']['description']
    if 'extra' in ad.keys():
        extra_desc = ad['extra']['description']
        extra_img = ad['extra']['img']

    image_gallery = get_images_from_configuration(ad_home, 'ImageGallery', ad['images_gallery'], ad['format'])
    photo_gallery = get_images_from_configuration(ad_home, 'PhotoGallery', ad['photo_gallery'], ad['format'])

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

    write_to_disk(ad['header']['name'], html_complete)


if __name__ == '__main__':
    main()