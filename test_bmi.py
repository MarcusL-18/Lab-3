import LAB2.bmi as bmi

print("Test_bmi")


def test_normal_weight():
    result = bmi.calculate_bmi(1.73 , 60)
    assert (result == 0)

def test_over_weight():
    result = bmi.calculate_bmi(1.73 , 60)
    assert (result == 1)

def test_under_weight():
    result = bmi.calculate_bmi(1.73 , 50)
    assert (result == -1)