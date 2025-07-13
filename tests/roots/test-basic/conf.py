"""Test configuration."""

extensions = [
    "myst_parser",
    "sphinx_marginbook_theme",
]

html_theme = "marginbook"
master_doc = "index"
exclude_patterns = ["_build"]

# LaTeX configuration
latex_engine = "xelatex"
