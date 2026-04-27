import anndata as ad
import pandas as pd
from scipy import sparse
from pathlib import Path

h5ad_path = Path("../blood/10x-rep1-kallisto-cellbender/10x-rep1-kallisto-cellbender.h5ad")
out_csv = Path("../blood/10x-rep1-kallisto-cellbender/10x-rep1-kallisto-cellbender_gene_by_cell.csv")
adata = ad.read_h5ad(h5ad_path)
X = adata.X
if sparse.issparse(X):
    X = X.toarray()

df = pd.DataFrame(X, index=adata.obs_names, columns=adata.var_names).T
df.to_csv(out_csv)

print(f"Wrote: {out_csv}")
print(f"Shape (genes x cells): {df.shape}")