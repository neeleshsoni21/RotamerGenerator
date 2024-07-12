"""Summary
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

from __future__ import print_function
import IMP
import IMP.core
import IMP.atom
import IMP.algebra
import IMP.rotamer

from collections import OrderedDict
import numpy as np
import os
import sys

class RotamerGenerator():

    """Summary
    
    Attributes:
        args (TYPE): Description
        h_residues (TYPE): Description
        hier (TYPE): Description
        m (TYPE): Description
        output_pdb (TYPE): Description
        rc (TYPE): Description
        residue_rotamers (TYPE): Description
    """
    
    def __init__(self, args):
        """Summary
        
        Args:
            args (TYPE): Description
        
        Returns:
            TYPE: Description
        """
        self.validate_arguments(args)

        self.m = IMP.Model()
        
        output_pdb_basename = os.path.splitext(os.path.basename(self.args.input_pdb))[0]
        
        
        self.output_pdb = os.path.join(self.args.output_dir,output_pdb_basename)

        self.read_pdb()
        self.get_all_rotamers()
        self.generate_rotamer_probability_distribution()
        self.Select_K_Rotamers_from_Distribution()
        self.Generate_K_pdb_models()

        return

    def validate_arguments(self, args):
        """
        Validates the command line arguments.
        
        Args:
            args (TYPE): Description
            Exits the program if any required arguments are missing.
        
        Returns:
            TYPE: Description
        """

        if not args.input_pdb:
            print('--input_pdb is required')
            sys.exit(1)

        if not args.output_dir:
            print('--output_dir is required')
            sys.exit(1)
        elif not os.path.isdir(args.output_dir):
            print('--output_dir directory not found!!')
            sys.exit(1)

        if not args.threshold:
            print('--threshold is required')
            sys.exit(1)
        elif (float(args.threshold) < 0) or (float(args.threshold) > 1):
            print('--threshold should be between 0 & 1')
            sys.exit(1)
        else:
            try:
                args.threshold = float(args.threshold)
            except:
                print('--num_models should be integer')
                sys.exit(1)

        if not args.num_models:
            print('--num_models is required')
            sys.exit(1)
        else:
            try:
                args.num_models = int(args.num_models)
            except:
                print('--num_models should be integer')
                sys.exit(1)
        
        if not args.input_lib:
            print('--input_lib is required')
            sys.exit(1)

        #if args.verbose:
        #    IMP.set_log_level(IMP.VERBOSE)

        self.args = args

        return

    def read_pdb(self):
        """
        Reads the input PDB file and extracts residues.
        
        Returns:
            TYPE: Description
        """
        self.hier = IMP.atom.read_pdb(self.args.input_pdb, self.m)
        
        self.h_residues = IMP.atom.get_by_type(self.hier, IMP.atom.RESIDUE_TYPE)

        return

    def get_all_rotamers(self):
        """
        Retrieves all possible rotamers for each residue in the structure.
        
        Returns:
            TYPE: Description
        """
        
        rl = IMP.rotamer.RotamerLibrary()
        rl.read_library_file(self.args.input_lib)
        
        self.rc = IMP.rotamer.RotamerCalculator(rl)
        self.residue_rotamers = OrderedDict()

        for h in self.h_residues:
            rd = IMP.atom.Residue(h)
            rr = self.rc.get_rotamer(rd, self.args.threshold)
            self.residue_rotamers[h] = [rd, rr]

        return

    def generate_rotamer_probability_distribution(self):
        """
        Generates a probability distribution for the rotamers of each residue.
        
        Returns:
            TYPE: Description
        """

        for h, (rd, rr) in self.residue_rotamers.items():
            
            rotamer_probabilities = OrderedDict()
            # Use CA as representative atom for the residue to identify the number of rotamers
            
            for numid in range(rr.get_number_of_cases(IMP.atom.AT_CA)):
                rotamer_probabilities[numid] = rr.get_probability(numid)
            
            rotamer_probabilities = self.normalize_dict_values(rotamer_probabilities)
            
            self.residue_rotamers[h].append(rotamer_probabilities)

        return

    def normalize_dict_values(self, prob_dict):
        """
        Normalizes the values in a dictionary to make their sum equal to 1.
        
        Args:
            prob_dict: Dictionary with probabilities.
        
        Returns:
            A dictionary with normalized values.
        """

        total = sum(prob_dict.values())
        
        if total == 0:
            normalized_dict = {key: value for key, value in prob_dict.items()}
        else:
            normalized_dict = {key: value / total for key, value in prob_dict.items()}
        
        return normalized_dict

    def Select_K_Rotamers_from_Distribution(self):
        """
        Selects K rotamers from the probability distribution for each residue.
        
        Returns:
            TYPE: Description
        """
        
        for h, (rd, rr, rot_probs) in self.residue_rotamers.items():
            
            if sum(rot_probs.values()) == 0:
                selected_rotamers = [0]
            
            else:
                selected_rotamers = list(np.random.choice(list(rot_probs.keys()), size=self.args.num_models, p=list(rot_probs.values())))
            
            self.residue_rotamers[h].append(selected_rotamers)

        return

    def Generate_K_pdb_models(self):
        """
        Generates K PDB models with the selected rotamers for each residue.
        
        Returns:
            TYPE: Description
        """
        
        for i in range(self.args.num_models):
        
            for h, (rd, rr, rot_probs, sel_idxs) in self.residue_rotamers.items():
        
                # For cases where there are no rotamers, like Ala, Gly
                idx = sel_idxs[0] if len(sel_idxs) == 1 else sel_idxs[i]
        
                for ha in IMP.atom.get_by_type(rd, IMP.atom.ATOM_TYPE):
                    at = IMP.atom.Atom(ha)
                    at_t = at.get_atom_type()
        
                    if rr.get_atom_exists(at_t):
                        res_coords = rr.get_coordinates(idx, at_t)
                        xyz = IMP.core.XYZ(at)
                        xyz.set_coordinates(res_coords)
            
            try:
                IMP.atom.write_pdb(self.hier, self.output_pdb + '_' + str(i) + '.pdb')
            except Exception as e:
                print("Error:",e)

        return
