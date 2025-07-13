"""LaTeX configuration for MarginBook theme."""

from __future__ import annotations

from typing import Any


def get_latex_elements() -> dict[str, Any]:
    """Get LaTeX elements configuration for margin notes.
    
    Returns:
        Dictionary of LaTeX configuration options.
    """
    return {
        # Document class options
        'papersize': 'a4paper',
        'pointsize': '10pt',
        
        # Preamble - packages and commands
        'preamble': r'''
% Page geometry for margin notes
\usepackage[
    a4paper,
    left=24.8mm,           % Inner margin
    textwidth=117mm,       % Main text width
    marginparsep=8.2mm,    % Gap between text and margin
    marginparwidth=39.4mm, % Margin width
    includemp,             % Include margin in page calculations
]{geometry}

% Font settings for XeLaTeX
\usepackage{fontspec}
\usepackage[korean]{kotex}

% Set main fonts - fallback if Noto not available
\IfFontExistsTF{Noto Serif CJK KR}{
    \setmainfont{Noto Serif CJK KR}
    \setsansfont{Noto Sans CJK KR}
}{
    \setmainfont{Times New Roman}
    \setsansfont{Arial}
}
\setmonofont{Consolas}

% Margin notes package
\usepackage{marginnote}
\renewcommand*{\marginnotevadjust}{-0.3cm}
\renewcommand*{\marginfont}{\footnotesize}

% Custom sidenote command (numbered)
\newcounter{sidenote}
\newcommand{\sidenote}[1]{%
    \stepcounter{sidenote}%
    \textsuperscript{\thesidenote}%
    \marginnote{\textsuperscript{\thesidenote}#1}%
}

% Margin figure environment
\newenvironment{marginfigure}{%
    \begin{marginnote}%
}{%
    \end{marginnote}%
}

% Better spacing
\usepackage{setspace}
\onehalfspacing

% Caption formatting
\usepackage[font=small,labelfont=bf]{caption}

% Hyperref settings
\hypersetup{
    colorlinks=true,
    linkcolor=black,
    citecolor=black,
    urlcolor=blue,
    pdfborder={0 0 0},
}
        ''',
        
        # Additional LaTeX packages
        'extrapackages': r'\usepackage{kotex}',
        
        # Figure alignment
        'figure_align': 'htbp',
        
        # Table of contents depth
        'tocdepth': 3,
        
        # Section numbering depth
        'secnumdepth': 3,
        
        # Footer
        'footer': '',
        
        # Fancy chapter headings
        'fncychap': '',
    }


def get_latex_documents(config) -> list[tuple[str, str, str, str, str]]:
    """Get LaTeX documents configuration.
    
    Args:
        config: Sphinx configuration object.
        
    Returns:
        List of document tuples for LaTeX builder.
    """
    return [
        (
            config.master_doc,  # Start file
            config.project.replace(' ', '') + '.tex',  # Target name
            config.project,  # Title
            config.author,  # Author
            'manual',  # Document class
        ),
    ]