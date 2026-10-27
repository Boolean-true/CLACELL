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
