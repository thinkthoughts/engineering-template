from __future__ import annotations

from IPython.display import Markdown, display

from .context import RepositoryContext


def render_engineering_context(context: RepositoryContext) -> None:
    """Render the Notebook 00 title and engineering statement."""

    display(
        Markdown(
            f"""# Engineering Context

**Repository:** `{context.repository}`  
**Repository description:** *{context.repository_description}*

## {context.engineering_statement_title}

> **{context.engineering_statement}**

Notebook 00 specifies the repository vocabulary, engineering variable,
notebook sequence, and generated context artifacts used by every later notebook.
"""
        )
    )


def render_specification_grammar(context: RepositoryContext) -> None:
    """Render the canonical specification grammar and design principle."""

    grammar_chain = " → ".join(context.grammar)

    display(
        Markdown(
            f"""## {context.grammar_title}

**{grammar_chain}**

**{context.design_principle}**
"""
        )
    )
