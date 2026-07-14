from .context import RepositoryContext


class ContextValidationError(ValueError):
    """Raised when repository context is incomplete or inconsistent."""


def validate_context(context: RepositoryContext) -> None:
    scalar_fields = {
        "repository": context.repository,
        "repository_description": context.repository_description,
        "engineering_statement": context.engineering_statement,
        "constraint": context.constraint,
        "connected_lane": context.connected_lane,
        "repository_variable_title": context.repository_variable_title,
        "lane_caption": context.lane_caption,
        "next_notebook": context.next_notebook,
    }

    for name, value in scalar_fields.items():
        if not value.strip():
            raise ContextValidationError(
                f"{name} must be non-empty"
            )

    sequence_fields = {
        "grammar": context.grammar,
        "engineering_objects": context.engineering_objects,
        "engineering_variables": context.engineering_variables,
        "observable_states": context.observable_states,
        "indicators": context.indicators,
        "lane_symbols": context.lane_symbols,
        "lane_labels": context.lane_labels,
        "construction_sequence": context.construction_sequence,
    }

    for name, values in sequence_fields.items():
        if not values:
            raise ContextValidationError(
                f"{name} must contain at least one item"
            )

        if any(not str(item).strip() for item in values):
            raise ContextValidationError(
                f"{name} contains an empty item"
            )

    if len(context.lane_symbols) != len(context.lane_labels):
        raise ContextValidationError(
            "lane_symbols and lane_labels must have equal length"
        )

    if len(context.construction_sequence) < 2:
        raise ContextValidationError(
            "construction_sequence must include Notebook 00 "
            "and at least one subsequent notebook"
        )

    next_number = context.construction_sequence[1].split(" ", 1)[0]

    if not context.next_notebook.startswith(next_number):
        raise ContextValidationError(
            "next_notebook must match the second item "
            "in construction_sequence"
        )
