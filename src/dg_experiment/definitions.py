from dagster import definitions, load_defs

import dg_experiment.defs


@definitions
def defs():
    return load_defs(defs_root=dg_experiment.defs)
