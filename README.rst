===========
switch_case
===========

A Dynamic, non-cascading Switch/case implementation for Python.
Since this class was made for users transitioning from languages with switch cases, no reserved words exist for switch case, or should ever be made (to prevent long term use of switch cases). This project exists to demonstrate the power of Python and help transitioning coders.

Here are a few examples of switch cases (from wikipedia) translated from native language to switch_case.py Python implementation:

Ruby
====

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