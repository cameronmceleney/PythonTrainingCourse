#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard libraries
import logging as lg
import matplotlib.pyplot as plt
import numpy as np
import os as os
import sys as sys

# 3rd Party Packages
# Add here

# My packages / Any header files
# Here

"""
    Description of what main does
"""

"""
    Core Details
    
    Author      : cameronmceleney
    Created on  : 19/08/2022 11:40
    Filename    : main
    IDE         : PyCharm
"""


def logging_setup():
    # Initialisation of basic logging information. 
    lg.basicConfig(filename='logfile.log',
                   filemode='w',
                   level=lg.DEBUG,
                   format='%(asctime)s - %(message)s',
                   datefmt='%d/%m/%Y %I:%M:%S %p',
                   force=True)


def main():
    lg.info("Program start")

    # Enter code here

    lg.info("Program end")

    exit()


if __name__ == '__main__':
    logging_setup()

    main()
