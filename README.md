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
git init
```

Setup other configurations
- Setup `.gitignore`
- Setup `README.md`
- Update `pyproject.toml`



### Notes
- `uvx create-dagster project dg-experiment` does not initialize a git repository unlike `uv init`
- Also does not generate a `.gitignore` or a `README.md`. Need to update the `pyproject.toml` and create the others
- The `create-dagster` and `dagster-dg` clis are distinct from each other
- The [guide](https://docs.dagster.io/guides/labs/dg/creating-a-project) and trying this out on a windows machine previously mention a `src/my_project/definitions.py` but seemingly did not create it. May be due to using the `create-dagster` directly without installation previously?
    - This may be due to the difference in dagster versions as well? The one the scaffolded `definitions.py` was `1.10.18` vs `1.10.19`