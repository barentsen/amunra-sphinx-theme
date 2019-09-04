Amunra-Sphinx-Theme
===================

.. image:: https://raw.githubusercontent.com/barentsen/amunra-sphinx-theme/master/docs/_static/images/amunra-preview.png
  :width: 400
  :alt: Amunra-Sphinx-Theme preview
  :target: https://barentsen.github.io/amunra-sphinx-theme/

Summary
-------

*Amunra* provides a lightweight, easy-to-use, responsive theme for Sphinx based on Bootstrap 4.
It features a minimalist top navigation bar which can be configured manually
or using Sphinx's standard ``toctree`` directive.


Demo
----

See the theme in action here:

* `<https://barentsen.github.io/amunra-sphinx-theme>`_ (`view source <https://github.com/barentsen/amunra-sphinx-theme/tree/master/docs>`__)
* `<https://docs.lightkurve.org>`_ (`view source <https://github.com/KeplerGO/lightkurve/tree/master/docs>`__)
* `<https://mirca.github.io/riskparity.py>_ (`view source <https://github.com/mirca/riskparity.py/tree/master/docs>`_)


Installation
------------

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
