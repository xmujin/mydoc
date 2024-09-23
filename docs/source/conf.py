# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '《Unix网络编程》手册'
copyright = '2024, 向洵'
author = '向洵'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'breathe'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False # 默认展开所有父级目录

}

# -- Options for EPUB output
epub_show_urls = 'footnote'


breathe_projects = {"MyProject": "../../../../mylib/docs/xml"}
breathe_default_project = "MyProject"