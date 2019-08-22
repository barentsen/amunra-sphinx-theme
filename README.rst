Amunra-Sphinx-Theme
===================

**A beautiful, responsive, minimalist theme for your Sphinx projects.**
 
Demo
----

See it in action at `docs.lightkurve.org <https://docs.lightkurve.org>`_.


Installation
------------

1. Install the theme::

    pip install amunra-sphinx-theme

2. Configure it in your Sphinx's `conf.py` configuration file
   as follows::

    html_theme = "amunra_sphinx_theme"

3. Configure the theme options by adding the following snippet
   in your `conf.py` file::

    html_theme_options = {
        "navbar_links": [
            ("Quickstart", "quickstart"),
            ("Tutorials", "tutorials/index"),
            ("API", "api/index"),
            ("About", "about/index"),
        ],
        "github_link": "https://github.com/barentsen/amunra-sphinx-theme",
        "footer_text": "Created with ♥ by Geert Barentsen.",
        "analytics_id": "UA-XXXXX-X"
    }
