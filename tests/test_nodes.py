"""Tests for custom docutils nodes."""

from __future__ import annotations

import pytest
from docutils import nodes

from sphinx_marginbook_theme.nodes import (
    MarginFigureNode,
    MarginNode,
    SidenoteNode,
    depart_margin_html,
    depart_margin_latex,
    visit_margin_html,
    visit_margin_latex,
)


class TestNodes:
    """Test custom node classes."""
    
    def test_margin_node_inheritance(self):
        """Test MarginNode inheritance."""
        node = MarginNode()
        assert isinstance(node, nodes.General)
        assert isinstance(node, nodes.Element)
        
    def test_sidenote_node_with_number(self):
        """Test SidenoteNode with number attribute."""
        node = SidenoteNode(number=42)
        assert node['number'] == 42
        
        # Test without number
        node2 = SidenoteNode()
        assert 'number' not in node2
        
    def test_margin_figure_node(self):
        """Test MarginFigureNode."""
        node = MarginFigureNode()
        assert isinstance(node, nodes.General)
        assert isinstance(node, nodes.Element)


class TestHTMLVisitors:
    """Test HTML visitor functions."""
    
    def test_visit_margin_html(self, mocker):
        """Test visit_margin_html function."""
        self_mock = mocker.Mock()
        self_mock.body = []
        self_mock.starttag.return_value = '<aside class="margin-note">'
        
        node = MarginNode()
        visit_margin_html(self_mock, node)
        
        self_mock.starttag.assert_called_once_with(node, 'aside', CLASS='margin-note')
        assert '<aside class="margin-note">' in self_mock.body
        
    def test_depart_margin_html(self, mocker):
        """Test depart_margin_html function."""
        self_mock = mocker.Mock()
        self_mock.body = []
        
        node = MarginNode()
        depart_margin_html(self_mock, node)
        
        assert '</aside>\n' in self_mock.body


class TestLaTeXVisitors:
    """Test LaTeX visitor functions."""
    
    def test_visit_margin_latex(self, mocker):
        """Test visit_margin_latex function."""
        self_mock = mocker.Mock()
        self_mock.body = []
        
        node = MarginNode()
        visit_margin_latex(self_mock, node)
        
        assert r'\marginnote{' in self_mock.body
        
    def test_depart_margin_latex(self, mocker):
        """Test depart_margin_latex function."""
        self_mock = mocker.Mock()
        self_mock.body = []
        
        node = MarginNode()
        depart_margin_latex(self_mock, node)
        
        assert '}' in self_mock.body