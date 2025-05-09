
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'agents-for-all'
author = 'Sailesh Dhungana'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.graphviz',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'

pygments_style = 'sphinx'
pygments_dark_style = 'monokai'

html_static_path = ['_static']
autoclass_content = 'both'
add_module_names = False

graphviz_dot = "dot"
