#
# ignore.py
#
# darch - Difference Archiver
# Copyright (c) 2015-2017 Ammon Smith
#
# darch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# darch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with darch.  If not, see <http://www.gnu.org/licenses/>.
#

__all__ = [
    'Ignore',
]

from fnmatch import fnmatch
import os

class Ignore(object):
    def __init__(self):
        self.antipatterns = []
        self.patterns = []

    def add(self, path, _open=open):
        path_dir = os.path.dirname(path)
        with _open(path, 'r') as fh:
            for line in fh.readlines():
                line = line.strip()
                if not line.startswith('#'):
                    if line.startswith('!'):
                        line = line[1:]
                        l = self.antipatterns
                    else:
                        l = self.patterns
                    l.append(os.path.join(path_dir, line))

    # Returns True if the file should be ignored
    def check(self, path):
        for pattern in self.antipatterns:
            if fnmatch(path, pattern):
                return False
        for pattern in self.patterns:
            if fnmatch(path, pattern):
                return True
        return False

