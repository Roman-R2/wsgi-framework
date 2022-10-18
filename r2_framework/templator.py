from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: name of template
    :param folder: folder with template
    :param kwargs: keyword arguments for template
    :return:
    """
    env = Environment()
    # Specify folder for template finding
    env.loader = FileSystemLoader(folder)
    # Finding template
    template = env.get_template(template_name)
    return template.render(**kwargs)

    # --------------- Old code ------------
    # file_path = join(folder, template_name)
    # # Open template for name
    # with open(file_path, encoding='utf-8') as f:
    #     template = Template(f.read())
    # # Render template with parameters
    # return template.render(**kwargs)
    # -------------------------------------
