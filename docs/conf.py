import amunra_sphinx_theme


project = 'Amunra'
copyright = '2019, Geert Barentsen'
author = 'Geert Barentsen'

release = amunra_sphinx_theme.__version__
version = ".".join(release.split('.')[:2])  # shorter X.Y version

# .nojekyll prevents GitHub from hiding the `_static` dir
#sys.path += ['exts']
extensions = ['sphinxcontrib.rawfiles, sphinx.ext.mathjax']
rawfiles = ['.nojekyll']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_static_path = ['_static']

html_theme = 'amunra_sphinx_theme'

html_theme_options = {
    # Title shown in the top left. (Default: ``project`` value.)
    "navbar_title": "Amunra v{}".format(version),

    # Links to shown in the top bar. (Default: top-level ``toctree`` entries.)
    "navbar_links": [
        ("Quickstart", "quickstart")
    ],

    # If ``github_link`` is set, a GitHub icon will be shown in the top right.
    "github_link": "https://github.com/barentsen/amunra-sphinx-theme",

    # Text to show in the footer of every page.
    "footer_text": 'Created with ♥ by Geert Barentsen.',
}
