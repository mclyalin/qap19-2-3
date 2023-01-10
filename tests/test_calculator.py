import pytest
from qap19_2_3.calculator import Calculator


NUMBER1 = 3
NUMBER2 = 2

@pytest.fixture
def calculator():
  return Calculator()

def test_add(calculator):
  expected = NUMBER1 + NUMBER2
  answer = calculator.add(NUMBER1, NUMBER2)
  assert expected == answer

def test_subtract(calculator):
  expected = NUMBER1 - NUMBER2
  answer = calculator.subtract(NUMBER1, NUMBER2)
  assert expected == answer

def test_multiply(calculator):
  expected = NUMBER1 * NUMBER2
  answer = calculator.multiply(NUMBER1, NUMBER2)
  assert expected == answer

def test_divide(calculator):
  expected = NUMBER1 / NUMBER2
  answer = calculator.divide(NUMBER1, NUMBER2)
  assert expected == answer