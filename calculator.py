def plus(a: float, b: float) -> float:
    return a + b


def minus(a: float, b: float) -> float:
    return a - b


def umnoz(a: float, b: float) -> float:
    return a * b


def delit(a: float, b: float) -> float:
    return a / b


while True:
    print(" -------------Actions------------- \n",
          "| Write (+) for addition        | \n",
          "| Write (-) for subtraction     | \n",
          "| Write (*) for multiplication  | \n",
          "| Write (/) for division        | \n",
          "| Write (end) for close program | \n",
          "--------------------------------- \n")

    sign = str(input("Write sign: "))
    if sign == "end":
        print("Calculator was closed! Thank you:) \n")
        break

    a = float(input("Write first number: "))
    b = float(input("Write second number: "))
    if sign == "+":
        print("Answer: ", plus(a, b))
    elif sign == "-":
        print("Answer: ", minus(a, b))
    elif sign == "*":
        print("Answer: ", umnoz(a, b))
    elif sign == "/":
        if b == 0:
            print("Error! Division by zero! \n")
        else:
            print("Answer: ", delit(a, b))
