from calculator import calculator_discount


def test_discount():
	assert calculator_discount(100, False) == 10

def test_discount():
	assert calculator_discount(100, True) == 20