import json
from importlib import resources

from ._marker_based_annotation.model_selection import select_cluster_model


class MarkerAnnotator:
    def __init__(self, marker_dict):
        """
        Initializes the MarkerAnnotator with a dictionary of markers.
        """
        self.marker_dict = marker_dict

    def annotate(self, adata):
        """
        Annotates the given AnnData object based on the provided marker genes.
        """
        print("Annotate data with marker-based annotation strategy")
        umi_df = adata.to_df()

        annotation_result = select_cluster_model(umi_df.T, self.marker_dict)
        adata.obs['scumi-annotation'] = annotation_result.label_final

        return adata