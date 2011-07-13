===========
switch_case
===========

A Dynamic, non-cascading Switch/case implementation for Python.
Since this class was made for users transitioning from languages with switch cases, no reserved words exist for switch case, or should ever be made (to prevent long term use of switch cases). This project exists to demonstrate the power of Python and help transitioning coders.

Here are a few examples of switch cases (from wikipedia) translated from native language to switch_case.py Python implementation:

Ruby
====

The following is a Ruby excerpt:: 

    case n
    when 0
        puts 'You typed zero'
    when 1, 9 
        puts 'n is a perfect square'
    when 2
        puts 'n is a prime number'
        puts 'n is an even number'
    when 3, 5, 7
        puts 'n is a prime number'
    when 4, 6, 8
        puts 'n is an even number'
    else
        puts 'Only single-digit numbers are allowed'
    end


Then you have the Python translation using switch_case.py, note that ruby does **not** have fall through.::

    #Import switch_case stuff, Ruby doesn't use the word "switch", so we alias it to be nice
    from switch_case import Switch as case

    when = case(n, fallthrough = False)
    if when(0):
        print 'You typed zero' #Python 3 works too...
    if when(1) or when(9):
        print 'n is a perfect square'
    if when(2):
        print 'n is a prime number'
        print 'n is an even number'
    if when(3) or when(5) or when(7):
        print 'n is a prime number'
    if when(4) or when(6) or when(8):
        print 'n is an even number'
    if when.default
        print 'Only single-digit numbers are allowed'

That's pretty close right?

