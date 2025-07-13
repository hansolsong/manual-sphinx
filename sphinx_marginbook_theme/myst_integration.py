"""Integration with MyST Parser for custom directives and roles."""

from __future__ import annotations

from typing import Any

from sphinx.application import Sphinx


def setup_myst_directives(app: Sphinx) -> None:
    """Setup MyST-specific directive plugins.

    This ensures our custom directives work seamlessly with MyST parser.

    Args:
        app: The Sphinx application object.
    """
    # Check if MyST parser is installed
    try:
        import myst_parser

        del myst_parser  # Imported only to check if available
    except ImportError:
        # MyST parser not installed, skip setup
        return

    # Register directives with MyST parser
    if hasattr(app, "myst_config"):
        # This is handled by MyST parser automatically when directives
        # are registered through Sphinx's add_directive
        pass


def create_myst_config() -> dict[str, Any]:
    """Create MyST configuration for margin notes.

    Returns:
        Dictionary of MyST parser configuration options.
    """
    return {
        "enable_extensions": [
            "colon_fence",  # For ::: directives
            "deflist",  # For definition lists
            "attrs_inline",  # For {margin}`text` syntax
        ],
    }
