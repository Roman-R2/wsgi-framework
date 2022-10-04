from jinja2 import Template
from os.path import join


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: name of template
    :param folder: folder with template
    :param kwargs: keyword arguments for template
    :return:
    """
    file_path = join(folder, template_name)
    # Open template for name
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    # Render template with parameters
    return template.render(**kwargs)
