"""Sphinx MarginBook Theme - A Sphinx theme with margin notes for beautiful manuals."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx

from .directives import setup_directives
from .nodes import setup_nodes
from .version import __version__, __version_tuple__

__all__ = ["__version__", "__version_tuple__", "setup", "get_html_theme_path"]


def get_html_theme_path() -> list[str]:
    """Return the path to the HTML theme directory.
    
    Returns:
        List containing the path to the theme directory.
    """
    return [str(Path(__file__).parent.resolve())]


def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup the Sphinx extension.
    
    Args:
        app: The Sphinx application object.
        
    Returns:
        Extension metadata.
    """
    # Register the HTML theme
    app.add_html_theme("marginbook", str(Path(__file__).parent / "html" / "theme" / "marginbook"))
    
    # Register nodes and directives
    setup_nodes(app)
    setup_directives(app)
    
    # TODO: Register transforms and visitors in Phase 3/4
    
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }