"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from titanic_project.pipelines import data_preparation as data_prep
from titanic_project.pipelines import data_modelling as data_mod


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    data_preparation_pipeline = data_prep.create_pipeline()
    data_modelling_pipeline = data_mod.create_pipeline()
    return {
        "__default__":sum(pipelines.values()),
        "data_prep":data_preparation_pipeline,
        "data_mod":data_modelling_pipeline
    }
