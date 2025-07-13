"""Sphinx MarginBook Theme - A Sphinx theme with margin notes for beautiful manuals."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from sphinx.application import Sphinx

from .directives import setup_directives
from .latex import get_latex_elements, setup_latex
from .nodes import setup_nodes
from .version import __version__, __version_tuple__

__all__ = [
    "__version__",
    "__version_tuple__",
    "get_html_theme_path",
    "get_latex_elements",
    "setup",
]


def get_html_theme_path() -> list[str]:
    """Return the path to the HTML theme directory.

    Returns:
        List containing the path to the theme directory.
    """
    return [str(Path(__file__).parent.resolve())]


def setup(app: Sphinx) -> dict[str, Any]:
    """Setup the Sphinx extension.

    Args:
        app: The Sphinx application object.

    Returns:
        Extension metadata.
    """
    # Register the HTML theme
    app.add_html_theme(
        "marginbook", str(Path(__file__).parent / "html" / "theme" / "marginbook")
    )

    # Register nodes and directives
    setup_nodes(app)
    setup_directives(app)

    # Setup LaTeX configuration
    setup_latex(app)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
