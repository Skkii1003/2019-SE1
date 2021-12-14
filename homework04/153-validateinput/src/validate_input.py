#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def namecheck(firstname,lastname):
    if len(firstname) == 0:
        print("The first name must be filled in.")
    elif len(firstname) < 3:
        print('"{}" is not a valid first name. It is too short.'.format(firstname))
    if len(lastname) == 0:
        print("The last name must be filled in.")
    elif len(lastname) < 3:
        print('"{}" is not a valid last name. It is too short.'.format(lastname))
        
def codecheck(zipcode):
    if len(zipcode) == 0:
        print("The ZIP code must be numeric.")
        return
    else:
        for i in range(len(zipcode)):
            if zipcode[i] < '0' or zipcode[i] > '9':
                print("The ZIP code must be numeric.")
                return
        
def id(employeeid):
    if len(employeeid) != 7:
        print('{} is not a valid ID.'.format(employeeid))
        return
    for i in range(0,2):
        if employeeid[i] < 'A' or employeeid[i] > 'Z':
            print('{} is not a valid ID.'.format(employeeid))
            return
        else:
            continue  
    if employeeid[2] != '-':
        print('{} is not a valid ID.'.format(employeeid))
        return
    for i in range(3,7):
        if employeeid[i] < '0' or employeeid[i] > '9':
            print('{} is not a valid ID.'.format(employeeid))
            return

def validate():
    firstname = input("Enter the first name:")
    lastname = input("JEnter the last name:")
    zipcode = input("Enter the ZIP code: ")
    employeeid = input("Enter an employee ID: ")
    
    namecheck(firstname,lastname)
    codecheck(zipcode)
    id(employeeid)
    
    return
    