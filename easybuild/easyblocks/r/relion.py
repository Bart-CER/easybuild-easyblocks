##
# Copyright 2009-2013 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for BiSearch, implemented as an easyblock

@author: Stijn De Weirdt (Ghent University)
@author: Dries Verdegem (Ghent University)
@author: Kenneth Hoste (Ghent University)
@author: Pieter De Baets (Ghent University)
@author: Jens Timmerman (Ghent University
@author: Bart Verleye (Auckland))
"""
import os

from easybuild.framework.easyblock import EasyBlock
from easybuild.tools.filetools import run_cmd


class EB_Relion(EasyBlock):
    """
    Support for building BiSearch.
    Basically just run the installation script install.sh.
    """

    def configure_step(self):
        """(no configure)"""
        pass

    def build_step(self):
        """(empty, building is performed in make_install step)"""
        pass

    def install_step(self):
        os.chdir("relion-1.2")
        
        cmd="sed -i.b 's/PREFIX=$RELION_HOME/PREFIX=%s/' INSTALL.sh " % self.installdir.replace("/","\/")
        run_cmd(cmd, log_all=True, simple=True)

        cmd = "./INSTALL.sh"
        run_cmd(cmd, log_all=True, simple=True)

    def sanity_check_step(self):
        """Custom sanity check."""

        custom_paths = {
                        'files':[],
                        'dirs':['bin','lib','include']
                       }

        super(EB_Relion, self).sanity_check_step(custom_paths=custom_paths)
