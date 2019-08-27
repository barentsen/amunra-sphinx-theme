Quickstart
==========

1. Install the theme::

    pip install amunra-sphinx-theme

2. Configure it in your Sphinx's ``conf.py`` configuration file
   as follows::

    html_theme = "amunra_sphinx_theme"

3. Configure the theme options by adding the following snippet
   in your `conf.py` file::

    html_theme_options = {
        # Title shown in the top left. (Default: ``project`` value.)
        "navbar_title": "Amunra",

        # Links to shown in the top bar. (Default: top-level ``toctree`` entries.)
        "navbar_links": [
            ("Quickstart", "quickstart"),
            ("Tutorials", "tutorials/index"),
            ("API", "api/index"),
            ("About", "about/index"),
        ],

        # If ``github_link`` is set, a GitHub icon will be shown in the top right.
        "github_link": "https://github.com/barentsen/amunra-sphinx-theme",

        # Text to show in the footer of every page.
        "footer_text": "Created with ♥ by Geert Barentsen.",

        # Google Analytics ID. (Optional.)
        "analytics_id": "UA-XXXXX-X"
    }

4. Optional: create a nice splash page for your project by including the
   following code in your `index.rst` file::

    .. title:: Your-Project-Title

    .. container:: lead

        Your-Project-Title

        A short description of your project.

        .. raw:: html

            <a href="quickstart.html" class="btn btn-primary">Quickstart →</a>
