import pytest
from qap19_2_3.calculator import Calculator


NUMBER1 = 3
NUMBER2 = 2

@pytest.fixture
def calculator():
  return Calculator()

def test_add_passed(calculator):
  expected = NUMBER1 + NUMBER2
  answer = calculator.add(NUMBER1, NUMBER2)
  assert answer == expected

def test_subtract_passed(calculator):
  expected = NUMBER1 - NUMBER2
  answer = calculator.subtract(NUMBER1, NUMBER2)
  assert answer == expected

def test_multiply_passed(calculator):
  expected = NUMBER1 * NUMBER2
  answer = calculator.multiply(NUMBER1, NUMBER2)
  assert answer == expected

def test_divide_passed(calculator):
  expected = NUMBER1 / NUMBER2
  answer = calculator.divide(NUMBER1, NUMBER2)
  assert answer == expected