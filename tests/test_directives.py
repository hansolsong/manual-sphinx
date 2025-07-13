"""Tests for MyST directives."""

from __future__ import annotations

import pytest
from docutils import nodes

from sphinx_marginbook_theme.directives import (
    MarginDirective,
    MarginFigureDirective,
    SidenoteRole,
)
from sphinx_marginbook_theme.nodes import MarginFigureNode, MarginNode, SidenoteNode


class TestMarginDirective:
    """Test the margin directive."""
    
    def test_margin_directive_basic(self, app):
        """Test basic margin directive functionality."""
        directive = MarginDirective(
            'margin',
            arguments=[],
            options={},
            content=['This is margin content'],
            lineno=1,
            content_offset=0,
            block_text='',
            state=None,
            state_machine=None,
        )
        # Set up minimal state
        directive.state = app.env.get_doctree('index').settings.env.docname
        
        # The directive should return a MarginNode
        # Note: Full testing requires a proper state machine setup
        assert directive.name == 'margin'
        assert directive.has_content is True
    
    def test_margin_node_creation(self):
        """Test MarginNode creation."""
        node = MarginNode()
        assert isinstance(node, nodes.General)
        assert isinstance(node, nodes.Element)


class TestSidenoteRole:
    """Test the sidenote role."""
    
    def test_sidenote_role_numbering(self):
        """Test that sidenotes are numbered correctly."""
        role = SidenoteRole()
        
        # First sidenote
        nodes1, messages1 = role(
            'sidenote',
            'raw',
            'First note',
            1,
            None,
        )
        assert len(nodes1) == 2  # ref + sidenote
        assert isinstance(nodes1[0], nodes.superscript)
        assert isinstance(nodes1[1], SidenoteNode)
        assert nodes1[1]['number'] == 1
        
        # Second sidenote
        nodes2, messages2 = role(
            'sidenote',
            'raw',
            'Second note',
            1,
            None,
        )
        assert nodes2[1]['number'] == 2
    
    def test_sidenote_node_attributes(self):
        """Test SidenoteNode attributes."""
        node = SidenoteNode(number=5)
        assert node['number'] == 5


class TestMarginFigureDirective:
    """Test the margin figure directive."""
    
    def test_margin_figure_directive_options(self):
        """Test margin figure directive options."""
        directive = MarginFigureDirective(
            'margin-figure',
            arguments=['image.png'],
            options={
                'alt': 'Test image',
                'width': '300px',
            },
            content=['Figure caption'],
            lineno=1,
            content_offset=0,
            block_text='',
            state=None,
            state_machine=None,
        )
        
        assert directive.required_arguments == 1
        assert 'alt' in directive.option_spec
        assert 'width' in directive.option_spec
        assert 'scale' in directive.option_spec
    
    def test_margin_figure_node_creation(self):
        """Test MarginFigureNode creation."""
        node = MarginFigureNode()
        assert isinstance(node, nodes.General)
        assert isinstance(node, nodes.Element)