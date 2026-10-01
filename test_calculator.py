from calculator import calculator_discount


def test_discount():
	assert calculator_discount(100, "premium") == 30

def test_discount():
	assert calculator_discount(100, "member") == 20

def test_discount():
	assert calculator_discount(100, "") == 10