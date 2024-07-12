"""Summary

Attributes:
    rg_root (TYPE): Description
"""
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

from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter

rg_root = str(Path(__file__).parent.parent)

def LoadArguments(
        input_pdb=rg_root+'/data/toy_pep_long.pdb',
        input_lib=rg_root+'/data/ALL.bbdep.rotamers.lib',
        threshold=1.0,
        num_models=10,
        output_dir=rg_root+'/output/'):
    """Summary
    
    Args:
        input_pdb (TYPE, optional): Description
        input_lib (TYPE, optional): Description
        threshold (float, optional): Description
        num_models (int, optional): Description
        output_dir (TYPE, optional): Description
    
    Returns:
        TYPE: Description
    """
    # -----------------------------------------
    # Command Line arguments Definitions
    # -----------------------------------------

    # Parse commandline Inputs
    parser_obj = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)

    parser_obj.add_argument("-i", "--input_pdb", default=input_pdb, help="Example input PDB file")

    parser_obj.add_argument("-l", "--input_lib", default=input_lib, help="Example input rotamer library file")

    parser_obj.add_argument("-t", "--threshold", default=threshold, help="Example probability threshold")

    parser_obj.add_argument("-k", "--num_models", default=num_models, help="Number of models to generate")

    parser_obj.add_argument("-o", "--output_dir", default=output_dir, help="Example output directory")

    args = parser_obj.parse_args()
    
    print("\nRunning with the following arguments!!\n")
    for v in vars(args):
        print(v,'\t' ,getattr(args, v))
    print()
    
    return args

if __name__ == '__main__':
    LoadArguments()

    