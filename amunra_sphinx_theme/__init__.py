from os import path

from .version import __version__


def get_html_theme_path():
    return path.abspath(path.dirname(path.dirname(__file__)))


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme('amunra_sphinx_theme', path.abspath(path.dirname(__file__)))
    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
