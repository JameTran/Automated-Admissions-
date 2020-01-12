from StdntAllocTypes import *
from AALst import *
from DCapALst import *


class SALst:
    s = []

    @staticmethod
    def init():
        SALst.s = []

    @staticmethod
    def add(m, i):
        is_in = False
        for element in SALst.s:
            if m in element:
                is_in = True
                break
        if (is_in):
            print('exception: element already inside')
        else:
            SALst.s = list(set(SALst.s) | {(m, i)})

    @staticmethod
    def remove(m):
        is_in = False
        for element in SALst.s:
            if m in element:
                is_in = True
                x = element
                break
        if (is_in):
            SALst.s = list(set(SALst.s) - {x})
        else:
            print('exception: no such element')

    @staticmethod
    def getS():
        for i in SALst.s:
            print(i)

    @staticmethod
    def elm(m):
        for element in SALst.s:
            if m in element:
                print(element)
                break

    @staticmethod
    def info(m):
        in_list = False
        for element in SALst.s:
            if m in element:
                print(element[1])
                in_list = True
        if (in_list is False):
            print('exception: key error')

    @staticmethod
    def sort():
        for i in SALst.s:
            for j in range(len(SALst.s)-1):
                if ((SALst.s[j])[1]).gpa > ((SALst.s[j+1])[1]).gpa:
                    test = ((SALst.s[j+1])[1]).gpa
                    list(((SALst.s[j+1])[1]).gpa) = list(((SALst.s[j])[1]).gpa)
                    ((SALst.s[j])[1]).gpa = test
        print(SALst.s)



sinfo = SInfoT('Bob', 'Tran', GenT.male, 12.0,
               SeqADT([DeptT.civil, DeptT.chemical]), True)
sinfo1 = SInfoT('fname', 'lname', GenT.female, 8.2,
               SeqADT([DeptT.engphys, DeptT.mechanical]), False)
sinfo2 = SInfoT('bruh', 'fuck', GenT.female, 8.1,
               SeqADT([DeptT.materials, DeptT.software]), True)
test = SALst()
test.init
test.add('tranj52', sinfo)
test.add('kazia3', sinfo1)
test.add('friasg', sinfo2)
test.sort()
