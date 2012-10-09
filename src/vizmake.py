#!/usr/bin/env python
#
# Copyright (c) 2012, Wenbin Fang
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#    This product includes software developed by the <organization>.
# 4. Neither the name of the <organization> nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY WENBIN FANG ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL WENBIN FANG BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__appname__ = 'vizmake'
__version__ = "2.0.0"
__author__ = "Wenbin Fang <fang@wenbin.org>"
__licence__ = "BSD"

#
# Libraries
#==========

import re

class VizMake:
    """
    Description:
      The central manager to visualize make
    """
    def __init__(self):
        pass

    def _parse(self, data):
        """
        Description:
          Parse the output of `make -p`
          1. For each line, regular expression match 'target: files'
          2. For matched lines, build dependency graph

        Arguments:
          data: output of `make -p`
        """
        lines = data.split('\n') 

        # TODO(wenbin): should handle the case that a target file has '%%'
        # Currently we assume the left side of ':' contains non-% and non-space
        prog = re.compile('^[^%\s]+:[^%]+$')
        for line in lines:
            result = prog.match(line)
            if result != None:
                # Split left side of first ':' and right side of first ':'
                # Left side is target, left side is dependent things
                print line
            
    def run(self):
        self._parse('')

def main():
    viz = VizMake()
    viz.run()

#
# Main
#======
if __name__ == '__main__':
    main()

# The end
