import json
from importlib import resources

from ._marker_based_annotation.model_selection import select_cluster_model


class MarkerAnnotator:
    def __init__(self, marker_dict=None):
        """
        Initializes the MarkerAnnotator with a dictionary of markers.
        If no marker_dict is provided, it loads a default set of marker genes from a JSON file.
        """
        if marker_dict is None:
            # Load default marker genes
            package_path = "clacell._marker_based_annotation" 
            source = resources.files(package_path).joinpath("human_pbmc_marker.json")
            with source.open("r", encoding="utf-8") as file:
                marker_genes = json.load(file)
            self.marker_dict = dict(marker_genes)
        else:
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