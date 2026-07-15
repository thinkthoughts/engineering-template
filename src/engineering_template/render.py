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


def render_repository_lane(context: RepositoryContext) -> None:
    """Render the repository lane from context labels and relationships."""

    chain_parts = [context.lane_labels[0]]

    for relationship, next_label in zip(
        context.lane_relationships,
        context.lane_labels[1:],
    ):
        chain_parts.append(f"{relationship} {next_label}")

    lane_chain = " ".join(chain_parts)

    display(
        Markdown(
            f"""## {context.repository_variable_title}

**{context.connected_lane}**

{lane_chain}

**{context.design_principle}**
"""
        )
    )


def render_repository_sequence(context: RepositoryContext) -> None:
    """Render the repository notebook sequence."""

    sequence_lines = "\n".join(
        f"- {item}" for item in context.construction_sequence
    )

    display(
        Markdown(
            f"""## {context.repository_sequence_title}

{context.repository_sequence_caption}

{sequence_lines}
"""
        )
    )
