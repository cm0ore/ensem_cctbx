# ensem_cctbx

##Author:

Camille Moore

##Summary:

ensem_cctbx_mapmask.py computes a map and mask within 1A of all residues for a given pdb_file. It also shifts the original pdb_file so that it will line up with the mask.

Note: you need two versions of the PDB, one with no solvent (for making the mask/map) and one original.

grep -v HETATM 7KQP.updated_refine_001.pdb | grep -v HOH > no_water_7KQP.pdb #removes waters from a pdb

##Outputs:
-shifted waterless pdb
-shifted orginial pdb
-map
-mask

##Example usage:

libtbx.python ensem_cctbx_map_making.py 'no_water_pdb_file' 'original_pdb_file'

##Conditions to run:

###Software requirements:

phenix==1.9-1692
CCTBX
python2.7

###Additional requirements:

A multi-MODEL PDB file
