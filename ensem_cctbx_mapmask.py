#Generates a shifted waterless_model, map, and mask and also shifts the original model by the same amount 
#inputs are waterless_pdb_file and original_pdb_file

import sys
import os
from iotbx.data_manager import DataManager     # load in DataManager
dm = DataManager()                             # Get an initialized version as dm
dm.set_overwrite(True)
from iotbx.map_model_manager import map_model_manager      #   load in the map_model_manager
mmm=map_model_manager()         #   get an initialized instance of the map_model_manager

no_water_pdb = sys.argv[1]
model_filename = sys.argv[2] 

#create map from waterless model and write new files 
file_basename = os.path.basename(model_filename).split('.pdb')[0]
mmm.generate_map(file_name=no_water_pdb, map_id='new_map', box_cushion=1)
mmm.write_model("%s_shifted.pdb" % file_basename)
mmm.write_map("%s_shifted_map.mrc" % file_basename) 
mmm.create_mask_around_atoms()   #  create binary mask around atoms in the model
mmm.apply_mask_to_maps()
dm.write_real_map_file(mmm.map_manager()   ,filename="%s_shifted_masked.mrc" % file_basename) # masked


#shift coords of model_file with solvent
model = dm.get_model("%s_shifted.pdb" % file_basename) #shifted and waterless
with_water_model = dm.get_model(model_filename)
sites_cart = with_water_model.get_sites_cart()          #      get coordinates of atoms in Angstroms
from scitbx.matrix import col                # import a tool that handles vectors
shift = tuple(i - j for i,j in zip(model.get_sites_cart()[0], with_water_model.get_sites_cart()[0])) 
sites_cart += col(shift) 

with_water_model.set_sites_cart(sites_cart)
print(with_water_model.get_sites_cart()[0])            # print coordinate of first atom
dm.write_model_file(with_water_model, "shifted_with_water.pdb", overwrite=True)



