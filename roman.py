class RomanNumeralConverter(object):

  # def __init__(self, input):
  #   self.input = input

  

  @classmethod
  def to_roman(cls, number):
    roman_values = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 50: "L"}


    if number == 10:
      numeral = roman_values[10]
    elif number == 9:
      numeral = roman_values[9]
    elif number > 5 and number < 9:
      numeral = roman_values[5] + roman_values[1]*(number-5)
    elif number == 5:
      numeral = roman_values[5]
    elif number == 4:
      numeral = roman_values[4]
    elif number <= 3:
      numeral = roman_values[1]*number
    return numeral


  @classmethod
  def from_roman(cls, roman):
    return 1
    
