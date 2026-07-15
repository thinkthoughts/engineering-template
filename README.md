# Engineering Template

This repository provides a reusable template for developing engineering repositories from leading specifications.

It generates a specification grammar, repository engineering-variable lane, repository notebook sequence, figures, and a machine-readable context manifest from one `RepositoryContext` object.

## Engineering Statement

> **A specified engineering variable connects observable states to admissible indicators.**

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

## Creating a New Repository

1. Create a repository from this template.
2. Rename the Python package and repository references.
3. Replace the `RepositoryContext` in Notebook 00.
4. Run `00_engineering_context.ipynb`.
5. Continue with `01_constraints.ipynb`.
