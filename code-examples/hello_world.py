#!/usr/bin/env python
# encoding: utf-8
"""
hello_world.py
Created by Robert Dempsey on 04/03/15.
Example taken from Getting Started With PyParsing by Paul McGuire

Tested with Python 3.4.2
"""

from pyparsing import *

# Input
hello_strings = """Hello, World!
Hi, Mom!
Good morning, Miss Crabtree!
Yo, Adrian!
Whattup, G?
How's it goin', Dude?
Hey, Jude!
Goodbye, Mr. Chips!"""

# Define your grammar
word = Word(alphas+"'.")
salutation = Group( OneOrMore(word) )
comma = Suppress(",")
greetee = Group( OneOrMore(word) )
endpunc = oneOf("! ?")
greeting = salutation + comma + greetee + endpunc

# Use the grammar
for t in hello_strings.split('\n'):
  salutation, greetee, endpunc = greeting.parseString(t)
  print(salutation, greetee, endpunc)

# Process the results
# Nothing to do here