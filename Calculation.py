
import operator
from Speak import say
################################                                 Function to perform calculations                                 ###############################

def calculate(query):
    ops = {
        'plus': operator.add,
        'add': operator.add,
        '+': operator.add,
        'minus': operator.sub,
        'subtract': operator.sub,
        '-': operator.sub,
        'times': operator.mul,
        'multiply': operator.mul,
        '*': operator.mul,
        'divided by': operator.truediv,
        'divide': operator.truediv,
        '/': operator.truediv,
        'mod': operator.mod,
        'modulus': operator.mod,
        '%': operator.mod,
        'power': operator.pow,
        '^': operator.pow
    }

    for word in ops:
        if word in query:
            try:
                left, right = query.split(word)
                left = float(left.strip())
                right = float(right.strip())
                result = ops[word](left, right)
                print(f"The result is {result}")
                say(f"The result is {result}.")
            except:
                print("Invalid calculation format.")
                say("Sorry, I couldn't perform the calculation due to an invalid format.")
