class InterceptingValidator():

    def __init__(self):
        self._validator = None
        self._input = "t" 

    def set_validator(self,validator):
        self._validator = validator

    def validate(self):
        return self._validator.validate(self._input)

class NumberValidator():
    """Checks if the input is a number or not """

    def validate(self, input):
        int_or_not = None

        try:
            user_input = int(input)
            print("Your input " + str(user_input) + " is an integer!")
            int_or_not = True
        except ValueError:
            print("Your input " + input + " is not an integer!")
            int_or_not = False

        return int_or_not

def check_input(ival):
    validator = NumberValidator()
    ival.set_validator(validator)
    return ival.validate()
