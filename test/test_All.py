from StdntAllocTypes import *
from AALst import *
from DCapALst import *
from Read import *
from SeqADT import *
import pytest


def test_StdntAllocTypes():
    x = ['a', 'b', 'c', 'd']
    test = SeqADT(x)
    assert test.next() == 'a'
    assert test.next() == 'b'
    assert test.next() == 'c'
    assert test.next() == 'd'
    assert test.end() is True
    with pytest.raises(StopIteration):
        test.next()
    test.start()
    assert test.next() == 'a'


def test_StdntAllocTypes():
    test = SInfoT('Bob', 'Tran', GenT.male, 12.0,
                  SeqADT([DeptT.civil, DeptT.chemical]), True)
    assert test.fname == 'Bob'
    assert test.lname == 'Tran'
    assert test.gender == GenT.male
    assert test.gpa == 12.0
    assert test.freechoice is True
    assert test.choices.next() == DeptT.civil
    assert test.choices.next() == DeptT.chemical


def test_DCapALst():
    test = DCapALst()
    test.init()
    test.add(DeptT.materials, 5)
    test.add(DeptT.chemical, 7)
    assert test.elm(DeptT.chemical) == (DeptT.chemical, 7)
    assert test.capacity(DeptT.chemical) == 7
    with pytest.raises(KeyError):
        test.remove(DeptT.software)
    with pytest.raises(KeyError):
        test.add(DeptT.materials, 7)


def test_AALst():
    test = AALst()
    test.init()
    test.add_stdnt(DeptT.civil, 'jeff')
    assert ['jeff'] == test.lst_alloc(DeptT.civil)
    assert 1 == test.num_alloc(DeptT.civil)
    assert 0 == test.num_alloc(DeptT.software)


def test_SALst():
    sinfo = SInfoT('Bob', 'Tran', GenT.male, 12.0,
                   SeqADT([DeptT.civil, DeptT.chemical]), True)

    sinfo1 = SInfoT('fname', 'lname', GenT.female, 8.2,
                    SeqADT([DeptT.engphys, DeptT.mechanical]), False)

    sinfo2 = SInfoT('ay', 't', GenT.female, 8.1,
                    SeqADT([DeptT.materials, DeptT.software]), True)
    SALst.init()
    SALst.add_stdnt('tranj52', sinfo)
    with pytest.raises(KeyError):
        SALst.add_stdnt('tranj52', sinfo)
    with pytest.raises(KeyError):
        SALst.remove('test')
    assert SALst.elm('tranj52') is True
    assert ((SALst.info('tranj52')).fname) == 'Bob'
    SALst.add_stdnt('kazia3', sinfo1)
    SALst.add_stdnt('friasg', sinfo2)
    assert SALst.sort(lambda x: x.freechoice) == ['tranj52', 'friasg']
    assert SALst.average(lambda x: x.freechoice) == 10.05
    with pytest.raises(ValueError):
        assert SALst.average(lambda x: x.gpa > 15)
    DCapALst.add(DeptT.civil, 8)
    DCapALst.add(DeptT.engphys, 5)
    DCapALst.add(DeptT.electrical, 0)
    SALst.allocate()
    assert AALst.lst_alloc(DeptT.engphys) == ['kazia3']
    assert AALst.lst_alloc(DeptT.materials) == ['friasg']


def test_Read():
    Read.load_stdnt_data('StdntData.txt')
    assert SALst.elm('macid1') is True
    Read.load_dcap_data('DeptCap.txt')
    assert DCapALst.elm(DeptT.civil) == (DeptT.civil, 100)
