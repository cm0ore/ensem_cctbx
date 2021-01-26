import sys
import os
from iotbx.data_manager import DataManager     # load in DataManager
dm = DataManager()                             # Get an initialized version as dm
dm.set_overwrite(True)
from iotbx.map_model_manager import map_model_manager      #   load in the map_model_manager
mmm=map_model_manager()         #   get an initialized instance of the map_model_manager
mm = mmm.map_manager()
pdb_file = sys.argv[1]
model = dm.get_model(pdb_file)

#make a map within 1A of all residues in model with given file_name
mmm.generate_map(file_name=pdb_file, box_cushion=1)

file_basename = os.path.basename(pdb_file).split('.pdb')[0]
mmm.write_map("%s.mrc" % file_basename)       #   write out a map in ccp4/mrc format
mmm.write_model("%s.pdb" % file_basename)    #   write out a model in PDB format

map_filename="%s.mrc" % file_basename
mm = dm.get_real_map(map_filename)
mm.shift_origin()
mm.show_summary()


mmm.create_mask_around_atoms(model=model)   #  create binary mask around atoms in the model

mmm.apply_mask_to_maps()
dm.write_real_map_file(mmm.map_manager()   ,filename="%s_masked.mrc" % file_basename) # masked


