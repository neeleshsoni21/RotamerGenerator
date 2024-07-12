################################################################################
#   Copyright (C) 2024 Neelesh Soni <neeleshsoni03@gmail.com>,
#   <neelesh@salilab.org>
#
#   This library is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this library.  If not, see <http://www.gnu.org/licenses/>.
################################################################################


#---------------------------
# Run with default arguments.
# USAGE: python rg_test.py
# rg_test.py should contain the following lines 
#---------------------------
import rotamergenerator as rg
args = rg.LoadArguments()
rg_obj = rg.RotamerGenerator(args)

'''
#---------------------------
# Run with command line arguments
# USAGE: python rg_test.py -i ./rotamergenerator/data/toy_pep_long.pdb -l ./rotamergenerator/data/ALL.bbdep.rotamers.lib -k 50 -t 1.0 -o ./rotamergenerator/output/
# rg_test.py should contain the following lines
#---------------------------
import rotamergenerator as rg
args = rg.LoadArguments()
rg_obj = rg.RotamerGenerator(args)


#---------------------------
# Run with input arguments
# USAGE: python rg_test.py 
# rg_test.py should contain the following lines
#---------------------------
input_pdb='./rotamergenerator/data/toy_pep_long.pdb'
input_lib='./rotamergenerator/data/ALL.bbdep.rotamers.lib'
threshold=1.0
num_models=10
output_dir='./rotamergenerator/output/'

import rotamergenerator as rg
args = rg.LoadArguments(input_pdb, input_lib, threshold, num_models, output_dir)
rg_obj = rg.RotamerGenerator(args)
'''


