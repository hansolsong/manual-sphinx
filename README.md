# sphinx-marginbook-theme

A Sphinx theme with margin notes for beautiful manuals, inspired by Tufte CSS and kaobook.

## Features

- 📝 **Margin Notes**: Place supplementary content in the margins using MyST directives
- 🎨 **Beautiful Typography**: Clean, readable design inspired by Quarto's Cosmo theme for HTML
- 📖 **PDF Support**: Professional PDF output with Tufte-style layout
- 🌏 **Korean Language Support**: Full support for Korean documentation
- 📱 **Responsive Design**: Margin notes adapt gracefully on mobile devices

## Installation

```bash
pip install sphinx-marginbook-theme
```

## Quick Start

1. Add the theme to your Sphinx configuration:

```python
# conf.py
extensions = [
    'myst_parser',
    'sphinx_marginbook_theme',
]

html_theme = 'marginbook'
```

2. Use margin notes in your MyST documents:

```markdown
# My Document

This is main content with a margin note{margin}`This appears in the margin!`.

:::{margin}
You can also use block-level margin notes for longer content.

- Item 1
- Item 2
:::
```

## Documentation

Full documentation is available at [https://sphinx-marginbook-theme.readthedocs.io](https://sphinx-marginbook-theme.readthedocs.io).

## Development

This project uses `uv` for package management:

```bash
# Clone the repository
git clone https://github.com/yourusername/sphinx-marginbook-theme.git
cd sphinx-marginbook-theme

# Install development dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Build documentation
cd docs
make html
make latexpdf
```

## Acknowledgments

- Inspired by [Tufte CSS](https://edwardtufte.github.io/tufte-css/)
- LaTeX layout inspired by [kaobook](https://github.com/fmarotta/kaobook)
- Built on top of [Sphinx](https://www.sphinx-doc.org/) and [MyST Parser](https://myst-parser.readthedocs.io/)
