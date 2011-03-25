#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Copyright (c) 2011, Jerry Felix
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import operator

class _CaseFunctionWithArgs():
    """ Storage for the CaseFunction and the args used within the case  """
    
    def __init__(self, CaseFunction, args):
        self.CaseFunction = CaseFunction
        self.args = args

class CaseFunction():
    """ Creates and handles CaseFunctions that are used within case 

    By instantiating CaseFunction, you create a holder of the CaseFunction
    that will be later executed.  This enables us to pass around the 
    CaseFunction and its args, without necessarily executing it.

    For example:
        from switch_case import switch, case
        x = raw_input()
        switch(x)    
        if case(1, 2, some_CaseFunction_with_side_effects(3)):   # <-- Line 4
            do_something

    In this example, we want to be able to pass the values 1, 2, and
    (some_CaseFunction_with_side_effects, 3) to our Switch()__call__()
    function in Line 4, without executing some_CaseFunction_with_side_effects
    unless necessary to determine Truth.  (The side effects might be that it
    changes some value, or perhaps it takes a long time to run.)

    If the raw_input is 1 or 2, then some_CaseFunction_with_side_effects is
    never called (because this case is determined to be True without calling
    the function, thanks to the first two values passed).

    So, instantiating CaseFunction allows you to set up a CaseFunction.
    Calling CaseFunction, through the use of case(CaseFunction(args)), will
    grab the CaseFunction and args and pass them along without execution.
    The CaseFunction will be executed later if necessary to determine
    boolean Truth of the case.
    
    """
    
    def __init__(self, case_function):
        self.case_function = case_function
    def __call__(self, *args):
        return _CaseFunctionWithArgs(self.case_function, args)

class Switch():
    """ Stores the switch arg, and compares against case args 

    Typical use is:

        from switch_case import switch, case, lt
        #
        # ... later in the program...
        #
        switch(x):   
        if case(1):
            process_1
        elif case(2,3):
            process_2_3

        if case(lt(10)):
            process_less_than_10_including_1_2_3

        if case():
            process_any_not_already_processed


    Calling case() with no args will return True if all previously checked
    cases were False (since the last call to switch).  Typical use is to
    check it last, to handle all previously unhandled cases.  

    Note in the above example that switch (i.e. lowercase) is used.  It is
    typically equated to Switch (the class name).  It's possible to use either,
    depending on what's imported.
    
    Instantiating Switch(arg) will evaluate the initial arg (once), and store it
    in switch_arg.  Also, self.true_count is defaulted to 0, signifying
    that no case has been True yet.  And last_switch keeps track in a class
    variable the identity of the last instance of Switch created.

    Calling the switch instance (typically using the case(args) function) will
    use the case args to compare against the switch arg.  If found to be
    True, self.true_count is incremented.  A Boolean is returned.

    So, in our typical example, above, the statement
        switch(x)
    creates an instance of the Switch object, storing x as a switch
    to be compared against, and storing the identity of this instance in
    last_switch.  This means that any future calls to case(arg) will
    use arg and x to return a boolean.

    An alternate, more explicit method of usage is to store the result of
    the call to switch().  For example:
        case_check_x = switch(x)
        if case_check_x(a,b,c):    
    This is good idea if you have multiple switch() statements in your program
    segment (i.e. function, module, whatever), because "case" is defined to
    use the last switch that was called, regardless of how the program is
    structured.  (I'm imagining that some wicked bugs could be introduced by
    nesting switch statements within case statements, since case is defined to
    check the previously executed switch, and not the one that might
    structurally appear to be checked.)

    """

    last_switch = None
    
    def __init__(self, switch_arg=None, limit=None, prev=None):
        """ Store the switch_arg and initialize the ever_true flag

        __init__ is called with the Switch(switch_arg) instantiation, typically
        case = Switch(x)

        limit can be used to help prevent "fall through" bugs of C's switch/
        case statement.  The case function will only return True a limited
        number of times, defined by limit.  Default is that there is no limit.
        
        """
        if prev:
            self.switch_arg = Switch.last_switch.switch_arg
            self.limit = Switch.last_switch.limit
            self.true_count = Switch.last_switch.true_count
        else:
            self.switch_arg = switch_arg
            self.limit = limit
            self.true_count = 0
            Switch.last_switch = self
        
    def __call__(self, *case_args):
        """ Use args to compare against switch_arg; if no args, return True if it hasn't yet 

        __call__ is called with the Switch(switch_arg)(arg) function, typically
        using the instance previously created.  Typically like this:
            if case(a, b, c):
                do_something

        If there are no args passed to case(), then simply return True if 
        self.true_count == 0.  This is helpful for the "case else" or "default"
        condition.

        If there are args, then for each arg, compute the value, and compare it
        to switch_arg either comparing equality, or by executing a
        CaseFunction provided as an arg to case).

        The results for each arg of case are checked, left-to-right, until a
        True case is found.  This means that some cases may not be checked
        (which is good for efficiency, and some side effects may be avoided).
                
        """

        t = False
        if self.limit == None or self.true_count < self.limit:
            if case_args:
                for arg in case_args:
                    if isinstance(arg, _CaseFunctionWithArgs):
                        t = arg.CaseFunction(self.switch_arg, *arg.args)
                    else:
                        t = self.switch_arg==arg
                    if t:
                        break
            else:
                t = not self.true_count
        self.true_count += int(t)
        return t


    @staticmethod
    def _case(*args):
        """ Calls the __call__ function of the last switch.
            
        This function gets called anytime you call case, without specifying
        which instance of Switch you are trying to call.  It will use the
        last created instance of Switch.
        
        """
        
        if Switch.last_switch == None:
            raise TypeError ("case has no pre-defined switch for comparison")
        
        return Switch.last_switch(*args)
        


# "CaseFunctions" allow for more complicated cases.  Instead of simply
# allowing cases of equality (e.g. case(1, 2, 3)), we can also consider cases
# of greater than, less than, contains, or any CaseFunction that the user
# wishes to write.
#
# CaseFunctions provide more power, flexibility, and unfortunately,
# a little bit of namespace polution.  Be careful that you don't import
# these short-named objects (like le), and then accidentally use the name for
# some other purpose, prior to their use with "case".  Longer versions (like
# less_than) are provided for your safety and code readability.
#
# These allow you to do things like checking the case of less-than-10
#     if case(lt(10)):
#         do_something
#
# You can intermix CaseFunctions and values in your case statement:
#     if case(2, 5, 7, gt(15)):      # cases 2, 5, 7, or greater than 15
#         do_something
#
lt = CaseFunction(operator.lt)
le = CaseFunction(operator.le)
eq = CaseFunction(operator.eq)
ne = CaseFunction(operator.ne)
gt = CaseFunction(operator.gt)
ge = CaseFunction(operator.ge)
contains = CaseFunction(operator.contains)

@CaseFunction
def contained_in(switch_arg, case_arg):
    """ Returns boolean value, reporting switch_arg is "in" case_arg.

    Think of this as the "in" function.  The name "in" was already taken!
    Use "contains" to see the inverse (i.e. if the case_arg is in switch_arg).
    """
    return switch_arg in case_arg

@CaseFunction
def between(switch_arg, case_arg_lower, case_arg_upper):
    """ Compares switch_arg with interval ( case_arg_lower case_arg_upper ]

    Note that this is inclusive on the lower bound, and exclusive on the
    upper bound, in typical Python style.
    """
    return case_arg_lower <= switch_arg < case_arg_upper

less_than = lt
less_than_or_equal = le
equal = eq
not_equal = ne
greater_than = gt
greater_than_or_equal = ge


# Users can create their own CaseFunctions in the same way that
# "between" and "contained_in" are created, above.
#
# For example, to create a "starts_with_a" CaseFunction, which will
# compare the switch value (perhaps user's input) with various cases, checking
# to see if the switch value starts with a certain character pattern
# regardless of upper-case vs. lower-case:
#
#    from switch_case import CaseFunction, switch, case 
#    
#    @CaseFunction
#    def starts_with_a(switch_arg, case_arg):
#        return switch_arg.lower().startswith(case_arg.lower())
#    
#    # ... later in the program...
#
#    switch(raw_input("What's your answer?"))
#    if case(starts_with_a("y"), starts_with_a("ok")):
#        print "I assume that's a Yes"



# Regarding the name switch vs. Switch:
# lowercase looks better for syntax; LeadingCaps for class name matches PEP8.
#
# You can either import like this:
#     from switch_case import Switch as switch
#     from switch_case import le, gt  #(or whatever CaseFunctions you need)
# This method has the benefit of making it obvious to later readers that
# Switch is a class.
#
# or like this:
#     from switch_case import *   # more namespace polution!
# This has the benefit of getting everything, at the cost of adding a lot of
# stuff that you might not need into your name space, and being less explicit
# for readers later.
#
# or like this:
#     from switch_case import switch, case, le, ge, CaseFunction
#
# The latter is recommended, importing switch and case, plus any CaseFunctions
# needed, plus CaseFunction, if you are creating your own CaseFunctions.
#
# Here's a complete list of stuff you might want:
#    from switch_case import switch, case, CaseFunction
#    from switch_case import le, lt, eq, ne, ge, gt
#    from switch_case import between, contained_in, contains
#    from switch_case import less_than, less_than_or_equal, equal, not_equal
#    from switch_case import greater_than, greater_than_or_equal
#
switch = Switch            # makes it look like a Python statement
case = Switch._case        # now case will call the last Switch created

