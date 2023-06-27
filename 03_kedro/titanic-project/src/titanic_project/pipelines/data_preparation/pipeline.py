"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.10
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import drop_features,preprocess


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=drop_features,
            inputs=["titanic_dataset", "params:list_drop"],
            outputs="titanic_dataset_cleaned",
            name="clean_data_node"
        ),
        node(
            func=preprocess,
            inputs=["titanic_dataset_cleaned"],
            outputs="titanic_dataset_preprocessed",
            name="preprocess_data_node"
        )
    ])
