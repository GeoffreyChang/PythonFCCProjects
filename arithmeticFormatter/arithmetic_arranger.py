import re


def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    num = []
    sign = []
    j = 0
    space = []
    for p in problems:
        num.append([int(x) for x in re.findall(r'\b\d+\b', p)])

        if re.findall(r'[a-zA-Z]', p):
            return "Error: Numbers must only contain digits."
        sign.append(re.findall(r'\+|-', p))
        if not sign[j]:
            return "Error: Operator must be '+' or '-'."
        for i in range(2):
            if num[j][i] > 9999:
                return "Error: Numbers cannot be more than four digits."
        j += 1
    for k in range(len(problems)):
        if num[k][0] > num[k][1]:
            space.append(len(str(num[k][0])))
        else:
            space.append(len(str(num[k][1])))

    arranged_problems = str(num[0][0]).rjust(space[0] + 2)
    for op1 in range(1, len(problems)):
        arranged_problems += str(num[op1][0]).rjust(space[op1] + 6)

    arranged_problems += "\n" + sign[0][0] + str(num[0][1]).rjust(space[0] + 1)
    for op2 in range(1, len(problems)):
        arranged_problems += sign[op2][0].rjust(5) + str(num[op2][1]).rjust(space[op2]+1)

    arranged_problems += "\n" + "".ljust(space[0] + 2, "-")
    for dash in range(1, len(problems)):
        arranged_problems += "    ".ljust(space[dash] + 6, "-")

    if answers:
        if sign[answers][0] == "+":
            arranged_problems += "\n" + str(num[0][0]+num[0][1]).rjust(space[0] + 2)
        else:
            arranged_problems += "\n" + str(num[0][0]-num[0][1]).rjust(space[0] + 2)
        for answers in range(1, len(problems)):
            if sign[answers][0] == "+":
                arranged_problems += str(num[answers][0] + num[answers][1]).rjust(space[answers] + 6)
            else:
                arranged_problems += str(num[answers][0] - num[answers][1]).rjust(space[answers] + 6)
    return arranged_problems

if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "1 - 3801"], True))
