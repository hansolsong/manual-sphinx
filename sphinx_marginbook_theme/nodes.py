"""Custom docutils nodes for margin content."""

from __future__ import annotations

from docutils import nodes


class MarginNode(nodes.General, nodes.Element):
    """Node for margin content.
    
    This node represents content that should be placed in the margin.
    It can contain any block-level content like paragraphs, lists, figures, etc.
    """
    
    pass


class SidenoteNode(nodes.General, nodes.Element):
    """Node for numbered sidenotes.
    
    This node represents a numbered sidenote that appears in the margin.
    Similar to footnotes but displayed in the margin instead of at the bottom.
    
    Attributes:
        number: The sidenote number
    """
    
    def __init__(self, *args, number: int | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        if number is not None:
            self['number'] = number


class MarginFigureNode(nodes.General, nodes.Element):
    """Node for figures placed in the margin.
    
    This node represents a figure (image with optional caption) that should
    be placed in the margin area.
    """
    
    pass


def setup_nodes(app):
    """Register the custom nodes with Sphinx.
    
    Args:
        app: The Sphinx application object.
    """
    app.add_node(
        MarginNode,
        html=(visit_margin_html, depart_margin_html),
        latex=(visit_margin_latex, depart_margin_latex),
    )
    app.add_node(
        SidenoteNode,
        html=(visit_sidenote_html, depart_sidenote_html),
        latex=(visit_sidenote_latex, depart_sidenote_latex),
    )
    app.add_node(
        MarginFigureNode,
        html=(visit_marginfigure_html, depart_marginfigure_html),
        latex=(visit_marginfigure_latex, depart_marginfigure_latex),
    )


# HTML visitor functions
def visit_margin_html(self, node):
    """Visit margin node for HTML output."""
    self.body.append(self.starttag(node, 'aside', CLASS='margin-note'))


def depart_margin_html(self, node):
    """Depart margin node for HTML output."""
    self.body.append('</aside>\n')


def visit_sidenote_html(self, node):
    """Visit sidenote node for HTML output."""
    number = node.get('number', '')
    self.body.append(
        f'<span class="sidenote-number">{number}</span>'
        f'<aside class="sidenote" data-sidenote-number="{number}">'
    )


def depart_sidenote_html(self, node):
    """Depart sidenote node for HTML output."""
    self.body.append('</aside>')


def visit_marginfigure_html(self, node):
    """Visit margin figure node for HTML output."""
    self.body.append(self.starttag(node, 'figure', CLASS='margin-figure'))


def depart_marginfigure_html(self, node):
    """Depart margin figure node for HTML output."""
    self.body.append('</figure>\n')


# LaTeX visitor functions
def visit_margin_latex(self, node):
    """Visit margin node for LaTeX output."""
    self.body.append(r'\marginnote{')


def depart_margin_latex(self, node):
    """Depart margin node for LaTeX output."""
    self.body.append('}')


def visit_sidenote_latex(self, node):
    """Visit sidenote node for LaTeX output."""
    # In LaTeX, we'll use a custom \sidenote command
    self.body.append(r'\sidenote{')


def depart_sidenote_latex(self, node):
    """Depart sidenote node for LaTeX output."""
    self.body.append('}')


def visit_marginfigure_latex(self, node):
    """Visit margin figure node for LaTeX output."""
    self.body.append(r'\begin{marginfigure}')


def depart_marginfigure_latex(self, node):
    """Depart margin figure node for LaTeX output."""
    self.body.append(r'\end{marginfigure}')