## @file AALst.py
#  @title AALst
#  @author Jame Tran
#  @date Feb.16, 2019
from StdntAllocTypes import *

## @brief An abstract object AALst that contains a set of tuples (Department, str)
#  and methods on them
class AALst:
    s = []

    ## @brief A method to initialize the set, filling it with departments of type
    #  DeptT and initally empty sequence of strings
    @staticmethod
    def init():
        AALst.s = [(DeptT.civil, []), (DeptT.chemical, []),
                   (DeptT.electrical, []), (DeptT.mechanical, []),
                   (DeptT.software, []), (DeptT.materials, []),
                   (DeptT.engphys, [])]

# [ expression for item in list if conditional ]
    ## @brief A method to add a (DeptT, str) tuple to the set
    @staticmethod
    def add_stdnt(dep, m):
        for i in AALst.s:
            if dep in i:
                (i[1]).append(m)

   ## @brief A method that returns current string sequence for a given department
   #  @param1 Department of type DeptT
   #  @return list of strings
    @staticmethod
    def lst_alloc(d):
        for element in AALst.s:
            if d in element:
                return element[1]

    ## @brief A method to give the length of the string sequence for a given deparment
    #  @param1 Department of type DeptT
    #  @return Int of length of string sequence
    @staticmethod
    def num_alloc(d):
        for element in AALst.s:
            if d in element:
                return len(element[1])
