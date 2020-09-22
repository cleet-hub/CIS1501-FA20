# -*- coding: utf-8 -*-
"""
@author: Christopher
Program that calculates how many more semesters 
and the total cost of completing a bachelors degree for the use
"""
import math

print('Hi, what is your name?')
user = input()
print('{}, how many credits have you earned?'.format(user))
earned_crdts = int(input())
print('{}, how many credits do you need to graduate?'.format(user))
required_crdts = int(input())
to_complete_crdts = required_crdts - earned_crdts 
print('{}, how many credits do you take per semester?'.format(user))
per_semester_crdts = int(input())
semesters_needed = math.ceil(to_complete_crdts/per_semester_crdts)
print('{}, how much does a credit cost?'.format(user))
crdt_cost = int(input())
remaining_cost = crdt_cost*to_complete_crdts
print('{}, based on the information you provided,' 
      ' you have {} semesters remaining at an expected minimum cost of {}'.format(user, semesters_needed, remaining_cost))
