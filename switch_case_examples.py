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




# switch_case examples


# This file demonstrates the switch_case module.


# switch_case is designed to provide Python with a switch and case syntax
# somewhat similar to what is found in the C language.  I developed this as
# an exercise to learn more about Python, and am not suggesting that it has
# any practical use.  Mostly, I wanted to see how elegantly it could be done.
# Still, if you can make use of it, please do so!


# I've tested switch_case on Python 2.7 and 3.2

# First, a bit of housekeeping, which will hopefully make these examples
# easier to read, while still executable.  Just ignore the next ten lines...

from __future__ import print_function
import sys
if sys.version[0]=="3":
    def raw_input(*args):
        return input(*args)
def _____________________________________________________________________(e=''):
                                    if type(e)==int:
                                     print("_"*80+"\n"+" "*30+"Example "+str(e))



_____________________________________________________________________            



# OK, now, back to our examples...


_____________________________________________________________________        (1)




# In it's simplest form, switch_case works like this:



from switch_case import switch, case             # note the import style
x = 42
switch(x)                                        # note the switch statement
if case(1):                                      # note the case statement
    print(1)
if case(2):
    print(2)
if case():                                       # note the case with no args
    print("Some number besides 1 or 2")


# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
Some number besides 1 or 2
                                                                             """
                                                                               )

_____________________________________________________________________            

# The final case() in the above example is a default value.  You use case()
# (with no parameters) to signify the default case -- if no previous case
# has been True since the switch statement was executed, then this block of code
# gets executed.

# In this simple form, it has the C-like fall-through behavior.  So we have
# the flexibility to execute multiple code blocks, if multiple cases are True.
# Of course, if this is undesirable, then elif and else can be used.  (Note
# that the "break" statement is *not* used, as it would be in C.  Instead, you
# use elif and else, to avoid fall-through.

_____________________________________________________________________        (2)



# Here's a second example that demonstrates the fall-through capability.
# Note that multiple blocks can be executed; in the case of "man", the first
# two blocks are executed.

from switch_case import switch, case

for person_type in ["man","boy","woman","doll"]:
    print ("The person is a "+ person_type + ".")

    implications = []
    switch(person_type)
    if case("man","boy"):                   # note that "man" appears here
        implications.append("he's male")
    if case("man","woman"):                 # note that "man" also appears here...             
        implications.append("the person is an adult")# and note "if", not "elif"
    if case("boy","girl"):
        implications.append("the person is a child")
    if case():
        implications.append("the person is not a male, adult or child")
    print ("  This implies " + ", and ".join(implications) + ".")


# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
The person is a man.
  This implies he's male, and the person is an adult.
The person is a boy.
  This implies he's male, and the person is a child.
The person is a woman.
  This implies the person is an adult.
The person is a doll.
  This implies the person is not a male, adult or child.
                                                                             """
                                                                               )

_____________________________________________________________________            


# In the above example, notice that when person_type == "man", the first
# two code blocks get executed.

# If you are a cautious programmer, you may want to limit the number of
# code blocks that get executed.  As mentioned earlier, you can limit it
# through the use of elif and else.  Or you can pass an argument called "limit"
# to your switch statement, which will also set a limit.

# The limit parameter limits how many times True will be returned by the case
# statement.  You can reset the counter and limit with a subsequent call to
# switch.

# Here's an example to demonstrate this concept.  In this example, I also
# introduce another feature: Case Functions.

_____________________________________________________________________        (3)

from switch_case import switch, case, lt

x = 5
switch(x, limit=1)                      # note the limit parameter
if case(lt(3)):                         # "lt" meaning "less than"
    print("x is less than 3")
if case(lt(6)):                         # x=5 satisfies this case
    print("x is less than 6")
if case(lt(9)):                         # note the "if", not "elif"
    print("x is less than 9")           # x=5 also satisfies this case
if case():
    print("x is greater than or equal to 9")


# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
x is less than 6                                                                             """
                                                                               )

_____________________________________________________________________            


# Note that in this example, the first case is checked, and is False.  The
# second case is checked, and is True.  Because the next statement is another
# if statement (as opposed to an elif or an else), the third case is checked,
# but because the limit has been reached (as specified in the switch statement),
# False is returned.  The fourth case is also checked, and returns False.

# This functions only slightly differently than if the last three if's were
# changed to elif's.  The difference is that in the elif case, the third and
# fourth case functions would never even be executed.  This is probably only
# significant if the parameters passed to case(...) have side effects (such as
# changing a value or if it is CPU-intensive).

# In the above example, the Case Function named "lt" is used.  This is a
# powerful feature.  I don't believe this is available in C. lt stands for
# less_than.  So case(lt(3)) is checking to see if the switch variable (x, in
# this case) is less than 3.

# Here's a list of the Case Functions that are available.

_____________________________________________________________________          (

                                                                             """
le, lt, eq, ne, ge, gt
between, contained_in, contains
less_than, less_than_or_equal, equal, not_equal
greater_than, greater_than_or_equal
                                                                             """
                                                                               )
_____________________________________________________________________            



# You can also write your own Case Functions, which is shown later.  First,
# let's look at some examples using other Case Functions.

_____________________________________________________________________        (4)

from switch_case import switch, case, contained_in

def compute_intensive_function():
    print ("a zillion CPU seconds pass...")
    return 6


switch(compute_intensive_function()) 
if case(1, contained_in(range(10,20)),21,31,41):  # mix constants with functions
    print ("That answer has a '1' in it.")
elif case(*range(42)):                            # unpack a list of integers
    print ("It's too small to be the answer we're looking for")
elif case(42):
    print ("we've found the answer!")
elif case():
    print ("Unexpected answer")


# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
a zillion CPU seconds pass...
It's too small to be the answer we're looking for
                                                                             """
                                                                               )
_____________________________________________________________________            


# There are a few significant things to note, in the above example.  First,
# constants can be intermixed with Case Functions, as is shown in the "if"
# statement.

# Note also that the compute-intensive function is only executed once, which is
# at the time it's passed to switch().

# In the if statement, above, the switch argument is compared in the following
# order:

# Is switch_arg equal to 1?
# or is switch_arg in [10,11,12,13,14,15,16,17,18,19]?
# or is switch_arg equal to 21?
# or is switch_arg equal to 31?
# or is switch_arg equal to 41?

# Note that if any one of these conditions is True, the other cases are not
# even tested; one True means that the entire case is True (since the
# conditions are or'd together).

# Note, too, the line that says
# elif case(*range(42)):

# The "*" in that line signifies the unpacking of the list that is returned
# from the range function or generator.  Without the "*", we would be comparing
# switch_arg to see if it is literally equal to the list (as opposed to
# checking each individual item contained within the list).

# case(*range(42)) and case(contained_in(range(42))) are roughly equivalent,
# although the former is implemented by unpacking the list, and comparing each
# item for equality, while the latter is implemented using the "in" keyword
# (which, internal to Python, probably does the same thing in the case of a
# list - it checks each item, left-to-right, comparing for equality).  There's
# a subtle difference, but generally the results will be the same (for lists),
# performing similarly as fast.

# However, if you are comparing against a set or a dictionary, then the
# preferred method is absolutely to use "contained_in", as opposed to unpacking
# the set or dictionary.  This is the difference between a hash and a search -
# the former is faster.

# Bad:
# if case(*some_set):
#     or
# if case(*some dictionary):
#
# Better:
# if case(contained_in(some_set)):
#     or
# if case(contained_in(some dictionary)):

# This is because sets and dicts contain performance enhancing hash values for
# quick retrieval.  And by unpacking them (using the "*" operator), you are
# essentially converting the item to a list, discarding the hash values!

# Another minor thing to notice in the above example is that certain values
# for switch_arg, such as 21, would meet both of the first two case conditions.
# Since logic is controlled by the elif, the second one is never executed (as
# you would expect).

# Here's another example

_____________________________________________________________________        (5)





from switch_case import switch, case, between

x=12
switch(x, limit=1)             # only execute the FIRST True case
if case(between(10,100)):
    print ("%d has two digits."%x)
if case(*range(0,100,2)):      # note that this is an if, not an elif!
    print ("%d is even."%x)    # doesn't get executed for 2 digit numbers,
                               # because limit is 1; previous case was True.
if case():
    print ("Nothing interesting to say about %d"%x)



# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
12 has two digits.
                                                                             """
                                                                               )
_____________________________________________________________________            


# In the above example, we use the "between" Case Function.  As you can guess,
# this does a comparison to see if the switch_arg is greater than or equal to
# the lower bound, and less than the upper bound.  This is consistent with
# Python's typical intervals (such as slices and ranges).  In other words, the
# example, above, case(between(10,100)) includes the number 10, but does not
# include the number 100, in the comparison.

# Can you guess what the difference between the following two cases are?
_____________________________________________________________________          (

                                                                             """
switch(x)
if case(between(10,100)):
    do_something
if case(*range(10,100)):
    do_something_else
                                                                             """                                                                               )
_____________________________________________________________________            

# What's the difference between these two cases?  Think about it.
# I'll tell you the answer in a minute.

# Let me describe what's going on behind the scenes with the switch and case
# statements.  When you call switch, the switch_arg is evaluated and stored.
# Also, a few other items are stored:  The limit (if any; defaults to None),
# a variable called true_count (which counts how many cases have evaluated
# to True), and an instance id for this instance of Switch.

# The true_count is initialized to zero, as you'd expect.  The instance id is an
# object that gives us access to all three of these values later, when we
# invoke the case function.

# So we keep a reference to all this information, for the *most recent* call
# to switch.   This makes our "simple implementation" work pretty well. You call
# switch.  Then when you call case, it knows what the last switch was, so we're
# all set.  Pretty simple.

# Unfortunately, things get a little tricky if you try to use switch multiple
# times in your program.  If they are totally independent uses, then there's no
# problem.  But if you try to nest them, then you are asking for trouble.
# So I'll show you how to work around that problem, but it's time for me to
# give you the answer of my question from four paragraphs ago.

# There's are a few subtle differences between "between" and "*range".
# Remember, range is simply calling the Python range function directly -
# switch_case has nothing to do with that.  And "range" will return a list of
# integers between 10 and 100.  Whereas "between" will compare switch_arg
# with 10 and 100.  There are a whole lot of non-integers that are between
# 10 and 100, that won't appear in the range!

# Another difference is that range will get expanded.  Imagine if the range was
# range(10,1000000).  A bunch of memory (and time) is going to get used in
# expanding that range, to create a list.  And even though range is a generator
# in more recent versions of Python, when you call case(range(10,1000000)),
# Python is going to generate that whole list of numbers immediately, before
# calling case.  "between", however, simply looks at those two end points, and
# compares switch_arg to them.

# So, "between" might help you with performance, especially with larger ranges.

# "between" is a Case Function that is included in the switch_case.py file.
# It's really very simple.  Here's what it looks like:

_____________________________________________________________________          (

                                                                             """
@CaseFunction
def between(switch_arg, case_arg_lower, case_arg_upper):
    return case_arg_lower <= switch_arg < case_arg_upper
                                                                             """
                                                                               )
_____________________________________________________________________            


# Disregarding the @CaseFunction decorator, it means that when someone calls
# "between", it return the boolean value of whether switch_arg is between the 
# lower and upper arguments (inclusive of the lower one).

# The CaseFunction decorator bundles the between function and it's arguments
# so that they can be called later, not immediately.  I'll try to explain this
# better a little later, but for now, simply accept that this is the general 
# format of the Case Functions, so that if you want to write your own, it's that
# simple.

# This next example shows you how you might write your own Case Function.

# Say you want to prompt the user to type something in.  And then you want to
# check their input with a series of case statements.  In my example, I only
# use one case statement, but you'll get the idea.

_____________________________________________________________________        (6)

from switch_case import  switch, case, CaseFunction      #remember to import
                                                         #CaseFunction

@CaseFunction
def starts_with_a(switch_arg, case_arg):
    return switch_arg.lower().startswith(case_arg.lower())


switch(raw_input("What's your answer? "))
if case(starts_with_a("y"), starts_with_a("ok")):
    print ("I assume that's a Yes")
    
_____________________________________________________________________            

# In this example, we have written our own Case Function that compares the
# switch_arg to see if it "starts with a" certain string of characters that
# are in case_arg.  It compares the strings regardless of upper-case and
# lower-case.

# The output will vary depending on the input, of course, but the response
# "I assume that's a Yes" will be displayed if "Y" or "yes" or "y" or "yeah" or
# "OK" or "ok" or "Ok" are entered, as examples.

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
What's your answer? OK
I assume that's a Yes
                                                                             """
                                                                               )
_____________________________________________________________________            

# Your custom Case Functions can be as simple or as complicated as you want.

# Remember earlier, I said that the @CaseFunction decorator bundles the function
# and its arguments for later execution.  Now I'll explain why I implemented
# it that way.

# I tried to design this switch/case implementation to run as few comparisons
# as possible, and to avoid duplicating comparisons.  That's why the switch
# argument is only calculated once and stored.

# Imagine the following poor logic.  Assume that "largest_factor" is a time
# consuming function.

_____________________________________________________________________          (

                                                                             """
# bad way to write code:
if  largest_factor(x) < 1000:
    do_something
elif largest_factor(x) < 5000:
    do_something_else

                                                                             """
                                                                               )
_____________________________________________________________________            


# Obviously, you'd want to calculate largest_factor(x) one time, rather than
# the way this is written.  With switch, you calculate largest_factor once:


_____________________________________________________________________          (

                                                                             """
# better:
switch(largest_factor(x))
if  case(lt(1000)):
    do_something
elif case(lt(5000)):
    do_something_else
                                                                             """
                                                                               )
_____________________________________________________________________            


# I know that's an obvious improvement (and I also realize that the same
# improvement could be done without switch / case).  Stick with me here.

# Imagine that you have a complex function, or a function with side effects
# in your case statement, and it's not the left-most condition in the case
# statement.  You would want to execute the comparisons from left to right,
# and stop when a True condition is found.

# Here's an example:

_____________________________________________________________________        (7)

import math
from switch_case import  switch, case, CaseFunction

@CaseFunction
def function_with_side_effect(x, y):
    print ("Processing %d"%y)
    return y >= x  #This is the same as: if y>=x: return True else: return False


switch(0)
if case(function_with_side_effect(1), function_with_side_effect(math.sqrt(4))):
    print ("Found at least one True case")
    
_____________________________________________________________________

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
Processing 1
Found at least one True case
                                                                             """
                                                                               )
_____________________________________________________________________            

# The thing to notice is that the output did NOT contain "Processing 2", because
# a True condition was found with the first condition, so the second condition
# never had to be executed.  In this case, function_with_side_effect only ran
# as few times as necessary, until True was established.

# However, Python will automatically try to reduce all of the parameters at the
# time the call to case is executed.  For example, the math.sqrt(4) function
# was executed, and  then the integer 2 was passed to
# function_with_side_effects.  But because function_with_side_effects is
# decorated with CaseFunction, the function and its parameters are grabbed
# and not executed unless necessary.

# It's hard to explain, but trust me, it's a good thing.


_____________________________________________________________________            


# I mentioned after example 5 that the simple form of switch / case that we
# have been using in all of these examples might be too simple for more
# complicated programs.  This is because case (as defined in switch_case.py)
# always refers to the most recently executed switch statement.  But if you
# nest switch statements, then you could cause yourself headaches.

# Here's an example program that demonstrates that gotcha:



_____________________________________________________________________        (8)

# Bad example - code has a bug in it, introduced by nesting

from switch_case import switch, case, lt, gt
my_money = 1000
your_money = 2000000


switch(my_money)
if case(lt(5000)):
    print ("I'm poor; I have less that $5000")
    switch(your_money - my_money)   # bug introduced: case gets changed here
    if case(gt(100000)):
        print ("You have A LOT more money than me!")
    elif case(gt(0)):
        print ("you have more money than me.")
    else:
        print ("you don't have any more money than I do.")
if case(gt(1000000)):     # bug effects this comparison
    print ("I'm rich!")   # bug displayed here
        
_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
I'm poor; I have less that $5000
You have A LOT more money than me!
I'm rich!
                                                                             """
                                                                               )
_____________________________________________________________________            

# The issue with this program is that the indent structure seems to imply
# that the "if case(gt(1000000)): is talking about the same switch as the
# first if statement.

# As you can see from the program output, the program concluded that I am
# both "poor" and "rich", because of the bug.

# There's a simple solution to this.  If there's a possibility that the
# switch_arg is going to change before all of the cases are evaluated, then
# we'll use a more complicated form of the switch/case syntax.

# In fact, it's probably good practice to use the more complicated form in
# all cases, but it's not quite as pretty as the simple form.  I thought the
# simple form looked eligant, and is completely suitable for simple
# applications.

# The complicated form is more Pythonic in the sense that it is more explicit.
# It looks like this:

_____________________________________________________________________          (

                                                                             """
from switch_case import switch     # we don't need to import case

case_casename = switch(x)          # note that we assign the switch to a case
if case_casename(value_1):         # then we refer to that case by name
    do_something
if case_casename(value_2):
    do_something_else
if case_casename():
    do_default
    
                                                                             """
                                                                               )
_____________________________________________________________________            

# Here's a corrected version of the previous example, that uses this complex
# format, in a nesting situation.

_____________________________________________________________________        (9)

# Better example

from switch_case import switch
my_money = 1000
your_money = 2000000


case_my_money = switch(my_money)      # Note how we bind the switch to something
if case_my_money(lt(5000)):           # And then we use the binding here.
    print ("I'm poor; I have less that $5000")
    case_money_diff = switch(your_money - my_money) # different binding
    if case_money_diff(gt(100000)):                 # different use
        print ("You have A LOT more money than me!")
    elif case_money_diff(gt(0)):
        print ("you have more money than me.")
    else:
        print ("you don't have any more money than I do.")
if case_my_money(gt(1000000)):       # back to using the first binding
    print ("I'm rich!")
        
_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
I'm poor; I have less that $5000
You have A LOT more money than me!
                                                                             """
                                                                               )
_____________________________________________________________________            

# Note in the example above, how the case_names make it very clear as to which
# case is being checked.

# Here's another example, demonstrating using sets in the case statements.
# These case statements should exectute very quickly, even with much larger
# sets than I have defined below, because sets are hashed data structures.

_____________________________________________________________________       (10)

 
from switch_case import switch, case, contained_in

nouns = set(["cat", "dog", "zebra", "fly", "horse", "bird"])
verbs = set(["sit", "can", "sing", "drive", "fly", "walk"])
articles = set(["a", "the"])

sentences = [
    "walk the dog",
    "can the horse sing",
    "can a bird fly",
    ]


for sentence in sentences:
    words = sentence.split()
    for word in words:
        part_of_speech = []
        switch(word)
        if case(contained_in(nouns)):
            part_of_speech.append("noun")
        if case(contained_in(verbs)):
            part_of_speech.append("verb")
        if case(contained_in(articles)):
            part_of_speech.append("article")
        if case():
            part_of_speech.append("unknown part of speech")
        print (word, "(" + ", ".join(part_of_speech) + ") ",end='')
    print()

_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
walk (verb) the (article) dog (noun) 
can (verb) the (article) horse (noun) sing (verb) 
can (verb) a (article) bird (noun) fly (noun, verb) 
                                                                             """
                                                                               )
_____________________________________________________________________            

# Note that word "fly" is determined to be possibly either a noun or a verb.

# Here are just a few more examples, to show you some possibilities.
_____________________________________________________________________       (11)


from switch_case import switch, case

switch(10, limit=1)
print ("switch_arg = %d" % switch(prev=True).switch_arg)   # Note syntax
print (" 1:          %s" % case(1))
print ("10:          %s" % case(10))   # This is True
print ("10:          %s" % case(10))   # limit is 1, so this will be False
print ("limit:       %s" % switch(prev=True).limit)
print ("true_count:  %s" % switch(prev=True).true_count)
print()

_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
switch_arg = 10
 1:          False
10:          True
10:          False
limit:       1
true_count:  1
                                                                             """
                                                                               )
_____________________________________________________________________            

# Note above that you have access to the most recent switch_arg, limit, and
# true_count, even using the simple format.  prev=True is telling switch that
# you are not building a new switch, but instead referring to the previous one.

# The limit has constrained the number of times that case will return True.
_____________________________________________________________________       (12)


from switch_case import switch, case

switch(15)
print ("switch_arg = %d" % switch(prev=True).switch_arg)
print (" 1:          %s" % case(1))
print ("10:          %s" % case(10))
print ("():          %s" % case())  # This is True, because nothing previous was
print ("():          %s" % case())  # But now it's False
print ("limit:       %s" % switch(prev=True).limit)
print ("true_count:  %s" % switch(prev=True).true_count)
print ()

_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
switch_arg = 15
 1:          False
10:          False
():          True
():          False
limit:       None
true_count:  1
                                                                             """
                                                                               )
_____________________________________________________________________            

# In the above case, there is no limit, but case() will still only return True
# one time.

_____________________________________________________________________       (13)


from switch_case import switch, case

case_1=switch(20)                           # Complex form of switch statement
print ("switch_arg = %d" % case_1.switch_arg)  # Note the syntax
print (" 1:          %s" % case_1(1))
print ("():          %s" % case_1())
print ("20:          %s" % case_1(20))
print ("20:          %s" % case_1(20))      # This can be True multiple times
print ("20:          %s" % case_1(20))
print ("():          %s" % case_1())        # This cannot be True multiple times
print ("limit:       %s" % case_1.limit)
print ("true_count:  %s" % case_1.true_count)
print ()

_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
switch_arg = 20
 1:          False
():          True
20:          True
20:          True
20:          True
():          False
limit:       None
true_count:  4
                                                                             """
                                                                               )
_____________________________________________________________________            

# Using the more complex format allows for simpler access to switch_arg, limit,
# and true_count.

# Note that in the above example, with no limit, true_count keeps incrementing.
# Still, though, case() will only be True at most once.  And even after case()
# is True, other True cases will return True (as long as the limit hasn't been
# exceeded).

_____________________________________________________________________       (14)


from switch_case import switch, case

switch(25)            #simple form complicates things later!
print ("switch_arg = %d" % switch(prev=True).switch_arg)
print ("limit:       %s" % switch(prev=True).limit)
print ("true_count:  %s" % switch(prev=True).true_count)
switch(prev=True).limit = 4              # Doesn't really do anything
switch(prev=True).true_count = 5         # Doesn't really do anything
print ("limit:       %s" % switch(prev=True).limit)
print ("true_count:  %s" % switch(prev=True).true_count)
switch(prev=True).last_switch.limit = 6        # This works
switch(prev=True).last_switch.true_count = 7   # This works
print ("limit:       %s" % switch(prev=True).limit)
print ("true_count:  %s" % switch(prev=True).true_count)


_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
switch_arg = 25
limit:       None
true_count:  0
limit:       None
true_count:  0
limit:       6
true_count:  7
                                                                             """
                                                                               )
_____________________________________________________________________            

# You can access limit and true_count from the most recent switch, but it's
# a little more difficult to change those values.  Note how attempting to
# change them to 4 and 5 has no effect.  (This is actually changing them on
# the current switch, which is created and immediately a candidate for
# garbage collection, since it's not assigned a name.)

# Setting limit and true_count can be done by accessing the last_switch
# property.  It's ugly, but it can be done, and it's demonstrated above,
# setting them to 6 and 7, respectively.

_____________________________________________________________________       (15)


from switch_case import switch, case

case_2 = switch(30)     # complex form simplifies things later
print ("switch_arg = %d" % case_2.switch_arg)   # Note the syntax
print ("limit:       %s" % case_2.limit)
print ("true_count:  %s" % case_2.true_count)
case_2.limit = 8                               
case_2.true_count = 9
print ("limit:       %s" % case_2.limit)
print ("true_count:  %s" % case_2.true_count)




_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
switch_arg = 30
limit:       None
true_count:  0
limit:       8
true_count:  9
                                                                             """
                                                                               )
_____________________________________________________________________            

# Notice above, how much easier it is to access the limit and the true_count, 
# when using the more complex "case_casename = switch(x)" format.  You can 
# easily reach in and change the limit and true_count.

_____________________________________________________________________       (16)


from switch_case import switch, case

case_3 = switch(35)
case_4 = switch(40)
print ("switch_arg:  %s" % case_3.switch_arg)
print ("switch_arg:  %s" % case_4.switch_arg)    # This accesses the same thing
print ("switch_arg:  %s" % switch(prev=True).switch_arg)  #... as this ...
print ("switch_arg:  %s" % case_3.last_switch.switch_arg) #... and this.

_____________________________________________________________________            

# Running this program produces this output:
_____________________________________________________________________          (

                                                                             """
switch_arg:  35
switch_arg:  40
switch_arg:  40
switch_arg:  40
                                                                             """
                                                                              )
_____________________________________________________________________            

# Note that the latest switch information can be accessed by using its name
# (case_4 in this case), or through switch(prev=True), or through any other
# switch that has been defined.   Not sure why you'd want to do that, but it's
# a side effect of the way I implemented this.


# Here's the complete documentation:

# You can import any or all of the following:
#
#    from switch_case import switch, case, CaseFunction
#    from switch_case import le, lt, eq, ne, ge, gt
#    from switch_case import between, contained_in, contains
#    from switch_case import less_than, less_than_or_equal, equal, not_equal
#    from switch_case import greater_than, greater_than_or_equal



# [case_name = ] switch(switch_arg=None ,limit=None, prev=None)
#
# This creates a new instance of a Switch, which stores switch_arg and limit.
# It also creates a new instance variable called true_count, which counts how
# many times True is returned from subsequent calls using case or case_name.
# And it also stores the instance id into a Class variable called last_switch.
# This means that every Switch has access to the id of the most recent Switch.
#
# "case" is a special instance of "case_name", and is defined to point to the
# most recent Switch.  And the optional case_name will provide later access to
# this particular Switch.
#
# "limit" sets the upper limit of how many times True can be returned when
# calling "case_name".
#
# Setting "prev" to some True value (for example, True, 1, "anything") will
# provide "read only" access to the switch_ arg, limit and the true_count of
# the most recently created Switch (and NOT count this one as the most recently
# created Switch).

# Every Switch has access to the most recently created Switch, through
# Switch.last_switch.  This provides read/write access to switch_arg, limit,
# and true_count, via Switch.last_switch.switch_arg and similar.
#
# So you can instantiate a new Switch, with Switch(prev=True), and have access
# to the most recently created Switch (prior to this one), through
# Switch(prev=True).last_switch.switch_arg (and similar for limit and
# true_count).


# case_name([args])
#
# First, this checks to see if we've reached our limit on the number of Trues
# that are permitted.  If so, we return False.
#
# This returns a boolean, comparing each arg with case_name.switch_arg, in a
# left-to-right order.  If any comparison comes back True, then the function
# itself is returned as True.  
#
# If one of the args is a Case Function with args, then the Case Function is
# executed.
#
# If no args are passed to case_name, then the boolean inverse of true_count is
# returned.  That is, it will be False if True has ever been returned by a
# previous case for this Switch, and True if there's never been a True before.
# This is helpful for the "default" condition in a switch/case structure.
#
# The following CaseFunctions are defined:
#    le, less_than_or_equal
#    lt, less_than
#    eq, equal
#    ne, not_equal
#    ge, greater_than_or_equal
#    gt, greater_than
#    between
#    contained_in
#    contains
#
# These are accessed like this:
#    case_name(CaseFunction(x))
# example:
#    if case(gt(7)):


# CaseFunction(case_function)
# This is a decorator class, used to grab the case_function and its arguments
# and hold them until they need to be executed.
#
# Example Use:
#    @CaseFunction
#    def starts_with_a(switch_arg, case_arg):
#        return switch_arg.lower().startswith(case_arg.lower())
