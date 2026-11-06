import anndata as ad
import pandas as pd
import numpy as np


adata = ad.io.read_h5ad('/home/woody/iwbn/iwbn133h/data/10x-gex/breast/0fbf6fa3-8463-46ab-bda8-9703848b58db.h5ad')
#adata = ad.io.read_h5ad('0fbf6fa3-8463-46ab-bda8-9703848b58db_spatial.h5ad')

print(adata)


def compute_target_sum(adata: ad.AnnData) -> float:
    if hasattr(adata.X, "sum"):
        per_cell_totals = np.asarray(adata.X.sum(axis=1)).ravel()
    else:
        per_cell_totals = np.sum(adata.X, axis=1)

    print("min:", np.min(per_cell_totals))
    print("median:", np.median(per_cell_totals))
    print("mean:", np.mean(per_cell_totals))
    print("max:", np.max(per_cell_totals))

    return float(np.median(per_cell_totals))


# Use raw counts for the dense dataset
adata = adata.raw.to_adata()

# Use gene names instead of ensemble ids
symbol_col = 'feature_name'

# Alt-Namen als Backup in var speichern
adata.var['ensembl_id'] = adata.var_names
print('saved backup of ensembl ids')
# Gen-Namen auf Symbole umstellen
adata.var_names = adata.var[symbol_col]
print('use gene names')
# Namenskonflikt verhindern (Index-Namen entfernen)
adata.var.index.name = None
# Duplikate behandeln (z.B. Gene_1, Gene_2 anhängen)
adata.var_names_make_unique()
print('make gene names unique')


def map_breast_cancer_hierarchy(adata):
    # Vollständiges Mapping-Dictionary: author_cell_type -> (Coarse, Fine)
    mapping = {
        # Maligne / Epitheliale Zellen (Coarse & Fine gleich wegen hoher Donor-Spezifität)
        **{epi: ('Epithelial cell', 'Epithelial cell') for epi in [
            'epi_0', 'epi_1', 'epi_2', 'epi_3', 'epi_4', 'epi_5', 'epi_6', 
            'epi_8', 'epi_13', 'epi_14', 'epi_15', 'epi_16', 'epi_17', 
            'epi_18', 'epi_20', 'epi_22', 'epi_low_ent'
        ]},
        
        # T-Zellen
        'CD8_Tem': ('T cell', 'CD8_Tem'),
        'CD4_Tem': ('T cell', 'CD4_Tem'),
        'CD4_Treg': ('T cell', 'CD4_Treg'),
        'CD4_Naive': ('T cell', 'CD4_Naive'),
        'CD8_Tex': ('T cell', 'CD8_Tex'),
        'CD8_Isg': ('T cell', 'CD8_Isg'),
        'T_Prolif.': ('T cell', 'T_Prolif.'),
        'CD4_Tfh': ('T cell', 'CD4_Tfh'),
        'CD4_Th': ('T cell', 'CD4_Th'),
        
        # NK-Zellen
        'NK': ('Natural killer cell', 'NK'),
        'NK_rNK': ('Natural killer cell', 'NK_rNK'),
        'NK_Cyto.': ('Natural killer cell', 'NK_Cyto.'),
        
        # B-Zellen & Plasma-Zellen
        'Plasma_IgG': ('Plasma cell', 'Plasma_IgG'),
        'B_ACB': ('B cell', 'B_ACB'),
        'B_Naive': ('B cell', 'B_Naive'),
        'B_Cell': ('B cell', 'B_Cell'),
        'B_IFIT': ('B cell', 'B_IFIT'),
        'B_GCB': ('B cell', 'B_GCB'),
        
        # Myeloische Zellen
        'Mac/Mono': ('Myeloid cell', 'Mac/Mono'),
        'cDC2': ('Myeloid cell', 'cDC2'),
        'Mac_RTM_LA': ('Myeloid cell', 'Mac_RTM_LA'),
        'Mac_RTM_IFN': ('Myeloid cell', 'Mac_RTM_IFN'),
        'Mac_LA': ('Myeloid cell', 'Mac_LA'),
        'Mac_RTM_MT': ('Myeloid cell', 'Mac_RTM_MT'),
        'Mac_IFN': ('Myeloid cell', 'Mac_IFN'),
        'Mac_Anti.': ('Myeloid cell', 'Mac_Anti.'),
        'Mac_ES': ('Myeloid cell', 'Mac_ES'),
        'pDC': ('Myeloid cell', 'pDC'),
        'mDC': ('Myeloid cell', 'mDC'),
        'cDC1': ('Myeloid cell', 'cDC1'),
        'Mast': ('Myeloid cell', 'Mast'),
        
        # Stromale Zellen / CAFs
        'CAFs (COL11A1+)': ('Stromal cell', 'CAFs (COL11A1+)'),
        'CAFs (LAMP5)': ('Stromal cell', 'CAFs (LAMP5)'),
        'CAFs (PI16+)': ('Stromal cell', 'CAFs (PI16+)'),
        'CAFs (DPT+)': ('Stromal cell', 'CAFs (DPT+)'),
        'CAFs (CA12+)': ('Stromal cell', 'CAFs (CA12+)'),
        'PCs (ECM)': ('Stromal cell', 'PCs (ECM)'),
        'VSMC': ('Stromal cell', 'VSMC'),
        'Myofibroblast': ('Stromal cell', 'Myofibroblast'),
        'Prolif Stromal': ('Stromal cell', 'Prolif Stromal'),
        
        # Endothelzellen
        'Endo Imm.': ('Endothelial cell', 'Endo Imm.'),
        'Endo Ven.': ('Endothelial cell', 'Endo Ven.'),
        'Endo Capil.': ('Endothelial cell', 'Endo Capil.'),
        'Endo Arter.': ('Endothelial cell', 'Endo Arter.'),
        'Endo Lymph.': ('Endothelial cell', 'Endo Lymph.')
    }
    
    # Mapping auf obs anwenden
    coarse_list = []
    fine_list = []
    
    for val in adata.obs['author_cell_type']:
        if val in mapping:
            coarse_list.append(mapping[val][0])
            fine_list.append(mapping[val][1])
        else:
            # Fallback für ungemappte Zellen (z.B. Rejection Class)
            coarse_list.append('Unknown')
            fine_list.append('Unknown')
            
    adata.obs['scumi_clean_coarse'] = coarse_list
    adata.obs['scumi_clean_fine_grained'] = fine_list
    
    return adata

adata_mapped = map_breast_cancer_hierarchy(adata)
print(adata_mapped)

print("Final AnnData object:")
print(adata_mapped)

print("Gene counts:")
compute_target_sum(adata_mapped)

print("Coarse cell type counts:")
print(len(adata_mapped.obs['scumi_clean_coarse'].value_counts()))
print(adata_mapped.obs['scumi_clean_coarse'].value_counts())

print("Fine-grained cell type counts:")
print(len(adata_mapped.obs['scumi_clean_fine_grained'].value_counts()))
print(adata_mapped.obs['scumi_clean_fine_grained'].value_counts())


# Save Dataset
ad.settings.allow_write_nullable_strings = True

output_path = '/home/woody/iwbn/iwbn133h/data/10x-gex/breast/0fbf6fa3-8463-46ab-bda8-9703848b58db_fine_and_coarse_annotated.h5ad'
adata_mapped.write_h5ad(output_path)