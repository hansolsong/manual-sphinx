"""Pytest configuration and fixtures for sphinx-marginbook-theme tests."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from sphinx.testing.path import path

if TYPE_CHECKING:
    from sphinx.application import Sphinx

pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture(scope='function')
def rootdir():
    """Root directory for test files."""
    return path(__file__).parent.abspath() / 'roots'


@pytest.fixture(scope='function')
def content(app: Sphinx):
    """Build the application and return the content directory."""
    app.build()
    return app.outdir


@pytest.fixture(scope='function')
def example_dir(tmp_path):
    """Create a temporary copy of the example project."""
    example_src = Path(__file__).parent.parent / 'examples' / 'basic'
    example_dst = tmp_path / 'example'
    shutil.copytree(example_src, example_dst)
    return example_dst