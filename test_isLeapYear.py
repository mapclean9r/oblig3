from main import isLeapYear


def test_year_dividable_by_4_is_LeapYear():
    assert isLeapYear(2000) == False
    assert isLeapYear(2004) == True
    assert isLeapYear(2008) == True
    assert isLeapYear(2012) == True
    assert isLeapYear(2016) == True


def test_year_dividable_by_100_is_not_a_LeapYear():
    assert isLeapYear(1800) == False
    assert isLeapYear(1700) == False
    assert isLeapYear(1703) == False
    assert isLeapYear(1702) == False
    assert isLeapYear(1709) == False


def test_dividable_by_400_is_LeapYear():
    assert isLeapYear(1200) == True
    assert isLeapYear(800) == True
    assert isLeapYear(804) == True
    assert isLeapYear(808) == True
    assert isLeapYear(812) == True
