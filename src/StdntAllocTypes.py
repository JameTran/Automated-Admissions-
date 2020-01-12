## @file StdntAllocTypes.py
#  @title StdntAllocTypes
#  @author Jame Tran
#  @date Feb.16, 2019
from SeqADT import *
from enum import Enum
from typing import NamedTuple


## @brief Creates an enumeration covering gender.
class GenT(Enum):
    male = 1
    female = 2


## @brief Creates an enumeration covering all possible departments
class DeptT(Enum):
    civil = 1
    chemical = 2
    electrical = 3
    mechanical = 4
    software = 5
    materials = 6
    engphys = 7


## @brief Creates a NamedTuple called SInfoT , containing fields and their types
# @details Fields are fname: string, lname: string, gender: GenT enum, gpa : float
# choices: SeqADT sequence ADT, freechoice: boolean
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
