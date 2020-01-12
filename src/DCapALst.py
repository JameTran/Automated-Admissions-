## @file DCapALst.py
#  @title DCapALst
#  @author Jame Tran
#  @date Feb.16, 2019
from StdntAllocTypes import *

## @brief A class called DCapALst that consists of a set of (Departments, capacity)
#  tuples. Contains methods for adding, removing, and getting tuple and department
class DCapALst:
    s = set()

## @brief A method to initialize the DCapALst set
    @staticmethod
    def init():
        DCapALst.s = set()

## @brief A method to add a (d, n) tuple to the set
#  @details takes in a (d, n) tuple. Checks if d is in list, If it is, raise a
#  KeyError exception. Otherwise, add (d, n) tuple
#  @param1 Department of type DeptT
#  @param2 Capacity in form of Natural int
    @staticmethod
    def add(d, n):
        in_elem = False
        for element in DCapALst.s:
            if d in element:
                in_elem = True
        if in_elem is True:
            raise KeyError
        else:
            DCapALst.s = DCapALst.s | {(d, n)}  # | is set union

## @brief A method to remove a (d,n) tuple given d
#  @details takes in department. Checks if d is in list. If it is, remove it
#  otherwise, raise a KeyError exception
# @param1 Department of type DeptT
    @staticmethod
    def remove(d):
        in_elem = False
        for element in DCapALst.s:
            if d in element:
                DCapALst.s = DCapALst.s - {element}
                in_elem = True
                # set difference of s & tuple with d
        if in_elem is False:
            raise KeyError

## @brief A method to recieve the tuple corresponding to d
#  @details Takes in d, checks list for d. If d is in list, return (d,n) tuple
#  Else, raise KeyError Exception
#  @param Department of type DeptT
#  @return Tuple (d, n), where d is of type DeptT and n is of type int
    @staticmethod
    def elm(d):
        for element in DCapALst.s:
            if d in element:
                return (element)

## @brief A method to recieve the capacity of a (d,n) tuples
#  @details Takes in d, checks list for d. If d is in list, return n from (d, n)
#  tuple. Else, raise KeyError
#  @param Department of type DeptT
#  @return capacity of type int
    @staticmethod
    def capacity(d):
        in_elem = False
        for element in DCapALst.s:
            if d in element:
                in_elem = True
                return (element[1])
        if in_elem is False:
            raise KeyError
