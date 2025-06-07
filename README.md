# dg-experiment

### Local Development Setup
Prerequisites
- [git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/)
- [vscode](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/)

Setup the relevant dagster cli with `uv`
```bash
# Get a list of all installed uv tools
uv tool list
uv tool install dagster-dg
uv tool install create-dagster
```

Create a dg-project
```bash
uvx create-dagster project dg-experiment
```

Setup other configurations
- Setup git repository `git init`
- Setup `.gitignore`
- Setup `README.md`
- Update `pyproject.toml`

Optional: Create definitions.py

Add dependencies
```bash
uv add package --extra optional-dependency # dagster-cloud[serverless]
uv add package --optional optional-dependency-group # Add to [project.optional-dependencies] dev
```

Install dependencies
```bash
uv sync --all-extras # For all dependency groups
uv sync --all-extras --no-extra ci # For all dependency groups excluding specific group
uv sync --extra dependency-group # For a specific group
uv sync --extra ci # Install ci on CI/CD
```

Check dependencies
```bash
uv tree
```

Activate pre-commit hooks
```bash
uv run pre-commit install
```


### Notes
- `uvx create-dagster project dg-experiment` does not initialize a git repository unlike `uv init`
- Also does not generate a `.gitignore` or a `README.md`. Need to update the `pyproject.toml` and create the others
- The `create-dagster` and `dagster-dg` clis are distinct from each other
- The [guide](https://docs.dagster.io/guides/labs/dg/creating-a-project) and trying this out on a windows machine previously mention a `src/my_project/definitions.py` but seemingly did not create it. May be due to using the `create-dagster` directly without installation previously?
    - This may be due to the difference in dagster versions as well? The one the scaffolded `definitions.py` was `1.10.18` vs `1.10.19`
