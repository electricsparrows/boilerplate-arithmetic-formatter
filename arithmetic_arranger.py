

def arithmetic_arranger(problems, show_ans = False):
    """
    :param problems:  array of strings of arithmetic problems
    :return:
    """
    if len(problems) > 5:
        return "Error: Too many problems."

    l1 = []
    l2 = []
    l3 = []
    answer = []

    for expr in problems:
        #extract operands and operator
        args = expr.split()
        op1 = args[0]
        op2 = args[2]
        operator = args[1]
        # error handling
        if not (operator == "+" or operator == "-"):
            return "Error: Operator must be '+' or '-'."
        # check numbers are less than 4 digits
        elif len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # check if op1 and op2 contain digits only
        try:
            ans = get_expr_ans(int(op1), int(op2), operator)
        except ValueError as e:
            return "Error: Numbers must only contain digits."

        pexp = single(op1, op2, operator, ans)
        l1.append(pexp[0])
        l2.append(pexp[1])
        l3.append(pexp[2])
        answer.append(pexp[3])

    res = ("    ".join(l1) + "\n" + "    ".join(l2) + "\n" + "    ".join(l3))
    if show_ans:
        res += ("\n" + "    ".join(answer))
    return res


def single(num1, num2, opstr, ans):
    num1 = str(num1)
    num2 = str(num2)
    ans = str(ans)

    if len(num1) != len(num2):
        num1, num2 = add_spaces(num1, num2)

    ans = add_spaces(ans, num2)[0]

    # nums are of same length:
    line1 = "  " + num1
    line2 = opstr + " " + num2
    line3 = "".join(["-" for i in range(len(line2))])
    line4 = " " + ans
    if int(ans) > 0:
        line4 = " " + line4
    #print(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4)
    return [line1, line2, line3, line4]

def get_expr_ans(n1:int, n2:int, operator)-> int:
    if operator == "+":
        return n1+n2
    elif operator == "-":
        return n1-n2

def add_spaces(n1, n2):
    """
    :param n1: string
    :param n2: string
    :return:   tuple of two number strings with same amt of spaces.
    """
    len1 = len(n1)
    len2 = len(n2)
    spaces = max(len1, len2) - min(len1, len2)

    if len1 < len2:
        # add len(num2)-len(num1) spaces to num1
        #spaces = len2 - len1
        for i in range(spaces):
            n1 = " " + n1
    else:
        #spaces = len1 - len2
        for i in range(spaces):
            n2 = " " + n2
    
    return (n1, n2)


#print(single(354, 123, "+", 477))
#print(single(123, 1231, "+", 1354))
# print(single(1235, 12, "-", 1223))
# print()
# print(single(234, 1234, "-", 234-1234))
# print(single(-34, -123, "-", 157))
# print(single(-345, 10, "+", -335))

#print( arithmetic_arranger(["192 + 23", "12 + 145", "5284 + 122"], True) )
#print(arithmetic_arranger(["1245 - 231", "123 + 1", "3641 - 1234", "2643 - 235", "2962 - 83"], True))

