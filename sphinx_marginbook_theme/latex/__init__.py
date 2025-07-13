"""LaTeX/PDF support for MarginBook theme."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .config import get_latex_documents, get_latex_elements

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__all__ = ["setup_latex", "get_latex_elements", "get_latex_documents"]


def setup_latex(app: Sphinx) -> None:
    """Setup LaTeX configuration for the theme.
    
    Args:
        app: The Sphinx application object.
    """
    # Check if building LaTeX
    if app.builder.format != 'latex':
        return
    
    # Update latex_elements with our configuration
    latex_elements = app.config.latex_elements or {}
    latex_elements.update(get_latex_elements())
    app.config.latex_elements = latex_elements
    
    # Set latex_engine to xelatex for better Unicode support
    app.config.latex_engine = 'xelatex'
    
    # Connect to config-inited event to ensure our settings are applied
    app.connect('config-inited', on_config_inited)


def on_config_inited(app: Sphinx, config: Any) -> None:
    """Update configuration after it's been initialized.
    
    Args:
        app: The Sphinx application object.
        config: The Sphinx configuration object.
    """
    # Ensure our LaTeX elements are applied
    if not hasattr(config, 'latex_elements'):
        config.latex_elements = {}
    
    config.latex_elements.update(get_latex_elements())