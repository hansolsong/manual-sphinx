"""MyST directives for margin content."""

from __future__ import annotations

from typing import Any

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

from .nodes import MarginFigureNode, MarginNode, SidenoteNode


class MarginDirective(SphinxDirective):
    """Directive for margin content blocks.

    Usage in MyST:
        :::{margin}
        This content appears in the margin.
        :::
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self) -> list[nodes.Node]:
        """Process the margin directive."""
        node = MarginNode()
        node.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class SidenoteRole:
    """Role for inline sidenotes.

    Usage in MyST:
        Some text {sidenote}`This is a numbered sidenote`
    """

    def __init__(self):
        self._counter = 0

    def __call__(
        self,
        name: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner,
        options: dict[str, Any] | None = None,
        content: list[str] | None = None,
    ) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Process the sidenote role."""
        options = options or {}

        # Increment counter for numbering
        self._counter += 1

        # Create the sidenote reference in the main text
        ref_node = nodes.superscript("", str(self._counter))
        ref_node["classes"] = ["sidenote-ref"]

        # Create the sidenote content
        sidenote = SidenoteNode(number=self._counter)

        # Parse the content
        content_node = nodes.paragraph("", text)
        sidenote += content_node

        return [ref_node, sidenote], []


class MarginFigureDirective(SphinxDirective):
    """Directive for figures in the margin.

    Usage in MyST:
        :::{margin-figure} image.png
        :alt: Alternative text

        Optional caption
        :::
    """

    has_content = True
    required_arguments = 1  # image path
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "alt": directives.unchanged,
        "height": directives.length_or_unitless,
        "width": directives.length_or_percentage_or_unitless,
        "scale": directives.percentage,
        "align": lambda arg: directives.choice(arg, ("left", "center", "right")),
        "name": directives.unchanged,
        "class": directives.class_option,
    }

    def run(self) -> list[nodes.Node]:
        """Process the margin figure directive."""
        node = MarginFigureNode()
        node.document = self.state.document

        # Create the image node
        image_node = nodes.image(uri=self.arguments[0])

        # Apply options to image
        if "alt" in self.options:
            image_node["alt"] = self.options["alt"]
        if "height" in self.options:
            image_node["height"] = self.options["height"]
        if "width" in self.options:
            image_node["width"] = self.options["width"]
        if "scale" in self.options:
            image_node["scale"] = self.options["scale"]

        node += image_node

        # Add caption if content is provided
        if self.content:
            caption_node = nodes.caption()
            self.state.nested_parse(self.content, self.content_offset, caption_node)
            node += caption_node

        return [node]


def setup_directives(app):
    """Register the directives with Sphinx.

    Args:
        app: The Sphinx application object.
    """
    app.add_directive("margin", MarginDirective)
    app.add_directive("margin-figure", MarginFigureDirective)

    # Create a single sidenote role instance to maintain counter
    sidenote_role = SidenoteRole()
    app.add_role("sidenote", sidenote_role)

    # Also register for MyST parser
    if hasattr(app, "myst_config"):
        # This will be called by MyST parser
        pass
