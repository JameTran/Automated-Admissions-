## @file Read.py
#  @title Read
#  @author Jame Tran
#  @date Feb.16, 2019
from StdntAllocTypes import *
from DCapALst import *
from SALst import *

## @brief An abstract object that handles file I/O and uses two methods. One is to
#  read student information and load it into SALst. The other one is to read Deparment
#  information and load it into DCapALst
class Read:
    ## @brief A method to take in a text file, read the student information inside,
    #  and load it into SALst
    #  @details Takes in a text file s in the format specified. Splits each line using
    #  list comprehension and uses it to create (macid, SInfoT) tuples. Then add them
    #  to SALst
    #  @param1 the name of the text file with student info
    @staticmethod
    def load_stdnt_data(s):
        SALst.init()
        with open(s, 'r') as fp:
            for line in fp:
                result = [x.strip() for x in line.split(',')]
                macid = result[0]
                fname = result[1]
                lname = result[2]
                gender = GenT[result[3]]
                gpa = float(result[4])
                choices = []
                for i in range(5, len(result)):
                    choices.append(DeptT[result[i].strip('[]')])
                    if result[i].endswith(']'):
                        break
                freechoice = result[-1]
                sinfo = SInfoT(fname, lname, gender, gpa, SeqADT(choices),
                               freechoice)
                SALst.add_stdnt(macid, sinfo)

    ## @brief A method to read a text file containing department information in the assignment,
    #  and load it into DCapALst
    #  @details Each line in the file is read using list comprehension. Then, (DeptT, N) tuples
    #  are created where DeptT is the deparment and N is the capacity. Inputs them into DCapALst
    #  @param1 A string corresponding to the name of the input file
    @staticmethod
    def load_dcap_data(s):
        DCapALst.init()
        with open(s, 'r') as fp:
            for line in fp:
                result = [x.strip() for x in line.split(',')]
                department = DeptT[result[0]]
                capacity = int(result[1])
                DCapALst.add(department, capacity)
