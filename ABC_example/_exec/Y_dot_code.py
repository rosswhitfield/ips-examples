#! /usr/bin/env python

"""
Y_dot_code.py 3/10/2018 (Batchelor)
A simple "physics" code which in a real application would typically be a massively 
parallel code, and which likely was written as a stand-alone with no thought of coupling 
to other codes.  The philosopy of the IPS is to not require any modification of the 
"physics" code's usual I/O.  

This code reads one input file "Y_dot_code.in" which is a surrogate for all the namelists and input
input files a serious code might need.  What it actually does is to calculate Y_dot for the 2D
system of ODEs:
X_dot = a_lin*X + b_nonlin*X*Y
Y_dot = c_lin*Y + d_nonlin*X*Y
Writes Y_dot into file "Y_dot_code.out"

"""
#from __future__ import print_function
import time
import utils.simple_assignment_file_edit as edit

print('Y_dot_code Running')

# Get data from input file

data_dict = edit.input_file_to_variable_dict('Y_dot_code.in')
c_lin = float(data_dict['c_lin'])
d_nonlin = float(data_dict['d_nonlin'])
X = float(data_dict['X'])
Y = float(data_dict['Y'])

# Do big calculation

Y_dot = c_lin*Y + d_nonlin*X*Y
time.sleep(2)	# Wait a few seconds to pretend to be doing something

# Write data to output file
variable_dict = {'Y_dot' : Y_dot}
edit.variable_dict_to_output_file(variable_dict, 'Y_dot_code.out')

# That's all folks