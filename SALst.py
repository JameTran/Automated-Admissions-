## @file SALst.py
#  @title SALst
#  @author Jame Tran
#  @date Feb.16, 2019
from StdntAllocTypes import *
from AALst import *
from DCapALst import *

## @brief A class containing a list of ('macid', SInfoT) tuples, and methods to add, delete
#  and recieve information on. Also contains methods to recieve average and sort by generic lambda
#  functions, and method to allocate students
class SALst:
    s = []

    ## @brief A method to initalize the list
    @staticmethod
    def init():
        SALst.s = []

    ## @brief A method to add an (m, i) tuple to the list
    #  @details First checks the list to see if the m value is already in there
    #  if it is, raise a KeyError. Else, add the (m, i) tuple to the list
    #  @param1 a string representing mac ids
    #  @param2 Student information of type SInfoT
    @staticmethod
    def add_stdnt(m, i):
        in_list = False
        for element in SALst.s or []:
            if m == element[0]:
                in_list = True
                break
        if (in_list is False):
            (SALst.s).append([m, i])
        else:
            raise KeyError

    ## @brief A method to remove a (m, i) tuple corresponding to a macid m
    #  @details First check whether m is in list. If it isnt, raise KeyError Exception
    #  Else, remove (m, i) tuple corresponding to m
    #  @param1 m of type string, corresponding to mac id
    @staticmethod
    def remove(m):
        in_list = False
        for element in SALst.s or []:
            if m in element:
                in_list = True
                the_element = element
                break
        if (in_list):
            (SALst.s).remove(the_element)
        else:
            raise KeyError

    ## @brief A method to check whether or not a (m, i) tuple corresponding to
    #  input m is in the list
    #  @param1 m of type string, where 'm' is a macid
    #  @return boolean of whether or not (m,i) is in list
    @staticmethod
    def elm(m):
        for element in SALst.s or []:
            if m in element:
                return True

    ## @brief A method to return student info give a macid
    #  @param1 takes in a string pertaining to macid
    #  @return student information of type SInfotT
    @staticmethod
    def info(m):
        for element in SALst.s or []:
            if m in element:
                return element[1]

    ## @brief a method to sort the list by a generic lambda expression
    #  @details First, sorts the list in descending order. Next, takes in
    #  a generic lambda expression as input and uses it to filter list using filter()
    #  returns filterd list
    #  @param1 lambda expression
    #  @return List of tuples (m, i) where m is macid of type string and i is student info
    #  of type SInfoT
    @staticmethod
    def sort(f):
        if SALst.s == []:
            raise Exception('List is empty')
        for i in SALst.s:
            for j in range(len(SALst.s) - 1):
                if ((SALst.s)[j])[1].gpa < ((SALst.s)[j+1])[1].gpa:
                    temp = (SALst.s)[j+1]
                    (SALst.s)[j + 1] = (SALst.s)[j]
                    (SALst.s)[j] = temp
        pre_filter = []
        for elem in SALst.s:
            pre_filter.append(elem[1])

        a = list(filter(f, pre_filter))
        final_list = []
        for elem in SALst.s:
            for j in a:
                if j in elem:
                    final_list.append(elem[0])
        return final_list
    @staticmethod
    def getS():
        print(SALst.s)


    ## @brief A method to calculate the average gpa of the list filtered by generic
    #  lambda method
    #  @details takes in list and filters it using lambda method. Then returns the average
    #  GPA. If the list is empty, raise a ValueError
    #  @param1 generic lambda expression
    #  @return average of type float
    @staticmethod
    def average(f):
        pre_filter = []
        for elem in SALst.s:
            pre_filter.append(elem[1])
        filtered = list(filter(f, pre_filter))
        if filtered == []:
            raise ValueError
        sum = 0
        for i in filtered:
            sum = sum + i.gpa
        average = sum / len(filtered)
        return average

    ## @brief A method to allocate the students into their preferred programs
    #  @details The method only allocates students with GPA 4.0 or higher. First, students
    #  with freechoice are sorted by GPA and directly placed into the programs of their choice.
    #  Next, students without free choice are allocated in based on department capacity. If students'
    #  First choice: if it is full, students are moved to their second choice, and so on.
    #  If a student is unable to be assigned, raise a RuntimeError
    @staticmethod
    def allocate():
        AALst.init()
        F = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in F:
            ch = (SALst.info(m)).choices
            AALst.add_stdnt(ch.next(), m)
        S = SALst.sort(lambda t: not t.freechoice and t.gpa >= 4.0)
        for m in S:
            ch = (SALst.info(m)).choices
            alloc = False
            while ((not alloc) and (not ch.end())):
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not alloc:
                    raise RuntimeError
