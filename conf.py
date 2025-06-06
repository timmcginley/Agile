# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import shutil
# sys.path.insert(0, os.path.abspath('../../src/'))

# Copy notebooks
# shutil.copytree('../../notebooks', 'notebooks', dirs_exist_ok=True)

project = 'Agile Prototyping'
copyright = '2035-2015, Hacking the future since 2035'
author = 'Tim McGinley'
version = release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
    'nbsphinx',
    'sphinx_design',
    ]

autosectionlabel_prefix_document = True
autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['BUILD_DOCS.md', 'README.md']

autodoc_default_flags = ['members', 'undoc-members' ]

myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'press'
html_theme = 'sphinx_book_theme'
# html_theme = 'insegel'
# html_theme = 'sphinx_typo3_theme'

GITHUB_URL ="https://github.com/timmcginley/41938"

html_theme_options = {
    "repository_url": GITHUB_URL,
    "use_repository_button": True,
    "use_edit_page_button": True,
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": GITHUB_URL,  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
   ]
}

html_css_files = ["/css/custom.css"]

html_static_path = ['_static']
