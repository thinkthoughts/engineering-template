"""
Reusable infrastructure for engineering-template notebooks.
"""

from .context import RepositoryContext
from .export import (
    create_outputs_archive,
    finalize_notebook,
)
from .figures import (
    generate_context_figures,
    plot_construction_sequence,
    plot_engineering_grammar,
    plot_repository_lane,
)
from .render import (
    render_engineering_context,
    render_specification_grammar,
    render_repository_lane,
    render_repository_sequence,
)
from .paths import (
    DATA,
    FIGURES,
    NOTEBOOKS,
    RESULTS,
    ROOT,
    initialize_directories,
)
from .validation import (
    ContextValidationError,
    validate_context,
)

__all__ = [
    "RepositoryContext",
    "ContextValidationError",
    "ROOT",
    "FIGURES",
    "RESULTS",
    "DATA",
    "NOTEBOOKS",
    "initialize_directories",
    "validate_context",
    "plot_engineering_grammar",
    "plot_repository_lane",
    "plot_construction_sequence",
    "generate_context_figures",
    "render_engineering_context",
    "render_specification_grammar",
    "render_repository_lane",
    "render_repository_sequence",
    "create_outputs_archive",
    "finalize_notebook",
]
