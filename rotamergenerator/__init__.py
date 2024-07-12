
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

import sys

sys.path.insert(1, './rotamergenerator')
sys.path.insert(1, './rotamergenerator/src')
sys.path.insert(1, './rotamergenerator/data')
sys.path.insert(1, './rotamergenerator/output')

from RotamerGenerator import RotamerGenerator
from src.addoptions import LoadArguments

import sys
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(_ROOT)
