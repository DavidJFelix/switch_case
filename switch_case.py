#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2011, Jerry Felix
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

class Switch():
    """
    """

    fall_through_flag = False
    test_set = set()
    
    def __init__(self, switch_data, fall_through = True):
        """ 
        """
        self.switch_data = switch_data
        self.fall_through = fall_through
        
    def __call__(self, *case_args):
        """       
        """
        if not self.fall_through:
            if not self.fall_through_flag:
                self.test_set = set()

            else:
                self.fall_through_flag = False

        self.test_set = self.test_set.union(set(case_args))
        for any in self.test_set:
            if any and isinstance(any, bool):
                return True

            try:
                if any == self.switch_data:
                    return True

            except(TypeError):
                pass

        return False

    def break(self):
        """
        """
        self.test_set = set()

    def continue(self):
        """
        """
        self.fall_through_flag = True