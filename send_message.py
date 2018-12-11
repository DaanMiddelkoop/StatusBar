#!/usr/bin/python3

from communicate import *
import sys

NAME = "daan"
to = "pieter" #input("To whom? ")
message = " ".join(sys.argv[1:]) #input("Message: ")

print(write(NAME, to, message))