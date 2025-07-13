"""Tests for theme setup and configuration."""

from __future__ import annotations

from pathlib import Path

import pytest

import sphinx_marginbook_theme
from sphinx_marginbook_theme import get_html_theme_path, get_latex_elements


class TestThemeSetup:
    """Test theme setup and configuration."""

    def test_version(self):
        """Test version is properly set."""
        assert hasattr(sphinx_marginbook_theme, "__version__")
        assert hasattr(sphinx_marginbook_theme, "__version_tuple__")
        assert isinstance(sphinx_marginbook_theme.__version__, str)
        assert isinstance(sphinx_marginbook_theme.__version_tuple__, tuple)

    def test_get_html_theme_path(self):
        """Test get_html_theme_path returns correct path."""
        paths = get_html_theme_path()
        assert isinstance(paths, list)
        assert len(paths) == 1

        theme_path = Path(paths[0])
        assert theme_path.exists()
        assert theme_path.is_dir()

    def test_get_latex_elements(self):
        """Test get_latex_elements returns proper configuration."""
        elements = get_latex_elements()
        assert isinstance(elements, dict)

        # Check required keys
        assert "preamble" in elements
        assert "papersize" in elements
        assert "pointsize" in elements

        # Check content
        assert "marginnote" in elements["preamble"]
        assert "sidenote" in elements["preamble"]
        assert "geometry" in elements["preamble"]

    def test_theme_files_exist(self):
        """Test that theme files are in place."""
        theme_path = Path(sphinx_marginbook_theme.__file__).parent

        # Check HTML theme files
        html_theme = theme_path / "html" / "theme" / "marginbook"
        assert html_theme.exists()
        assert (html_theme / "theme.conf").exists()
        assert (html_theme / "layout.html").exists()
        assert (html_theme / "static" / "marginbook.css").exists()
        assert (html_theme / "static" / "marginbook.js").exists()

        # Check LaTeX files
        latex_path = theme_path / "latex"
        assert latex_path.exists()
        assert (latex_path / "config.py").exists()


class TestSphinxIntegration:
    """Test Sphinx integration."""

    @pytest.mark.sphinx("html", testroot="basic")
    def test_html_build(self, app, status, warning):
        """Test that HTML build works."""
        app.build()
        assert app.builder.name == "html"

        # Check that theme was applied
        assert app.config.html_theme == "marginbook"

    @pytest.mark.sphinx("latex", testroot="basic")
    def test_latex_build(self, app, status, warning):
        """Test that LaTeX build works."""
        app.build()
        assert app.builder.name == "latex"

        # Check that LaTeX configuration was applied
        assert app.config.latex_engine == "xelatex"
        assert "marginnote" in app.config.latex_elements.get("preamble", "")
