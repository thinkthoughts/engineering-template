# Engineering Template

This repository provides a reusable template for developing engineering repositories from leading specifications.

It generates a connected engineering context, reusable figures, machine-readable specifications, and notebook workflows by specializing a single `RepositoryContext` object.

## Engineering Statement

> **Engineering variables specify measurable repository contexts.**

*Replace this statement with the engineering statement for your repository.*

<img src="figures/repository-template.png" />

## Specification Grammar

```text
Constraint
↓
Connected lane
↓
Engineering object
↓
Engineering variable
↓
Observable state
↓
Indicator
```

**Admissible generalizations trail leading specifications.**

## Repository Notebook Sequence

```text
00  Engineering Context
01  Constraints
07  Connected Lanes
11  Engineering Objects
13  Engineering Variables
17  Observable State
19  Distribution
23  Dynamics
29  Optimization
37  Controllers
43  Benchmarks
```

Each notebook develops an engineering concept.

## Repository Outputs

- reusable engineering notebooks
- repository context figures
- machine-readable engineering specifications
- reusable Python package
- engineering benchmarks and examples

## Repository Structure

```text
RepositoryContext
        ↓
validation.py
        ↓
figures.py
        ↓
Notebook 00
        ↓
engineering_context.json
```

A new engineering repository is created by specializing the `RepositoryContext` while reusing the notebook structure, specification grammar, figure generation, validation, and repository workflow.

## Creating a New Repository

1. Clone this repository.
2. Rename the Python package and repository.
3. Update the `RepositoryContext`.
4. Run `00_engineering_context.ipynb`.
5. Begin Notebook 01 for the new engineering domain.
