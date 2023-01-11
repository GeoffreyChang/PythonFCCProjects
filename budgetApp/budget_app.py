import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.sum = 0

    def __repr__(self):
        print_stuff = ""
        for i in range(len(self.ledger)):
            temp = list(self.ledger[i].values())
            print_stuff += f'{temp[1].ljust(23, " ")[0:23]:<10}{temp[0]:>7.2f}\n'
        return f'{self.name.center(30, "*")}\n{print_stuff}Total: {self.sum}'

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.sum += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.sum

    def transfer(self, amount, receiver):
        if self.withdraw(amount, f"Transfer to {receiver.name}"):
            receiver.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if self.sum - amount < 0:
            return False
        else:
            self.sum -= amount
            return True


def create_spend_chart(categories):
    grand_total = []
    chart = f"Percentage spent by category\n"
    percentages = []
    for cat in categories:
        total = 0
        print(cat)
        for i in range(len(cat.ledger)):
            if list(cat.ledger[i].values())[0] < 0:
                total += list(cat.ledger[i].values())[0]
        grand_total.append(total)

    for num in grand_total:
        percentages.append(math.floor(num/sum(grand_total)*10))

    for j in range(10, -1, -1):
        line = f"{j * 10:>3}| "
        if percentages[0] >= j:
            line += "o"
        else:
            line += " "

        if percentages[1] >= j:
            line += "  o"
        else:
            line += "   "

        if percentages[2] >= j:
            line += "  o  "
        else:
            line += "     "

        if j == 0:
            chart += line + "\n    ----------\n"
        else:
            chart += line + "\n"
    largest = [categories[0].name, categories[1].name, categories[2].name]
    largest = largest.index(max(largest, key=len))
    largest = len(categories[largest].name)
    for h in range(largest):
        if h == largest - 1:
            chart += f"{categories[0].name.ljust(largest, ' ')[h]:>6}{categories[1].name.ljust(largest, ' ')[h]:>3}" \
                     f"{categories[2].name.ljust(largest, ' ')[h]:>3}  "
        else:
            chart += f"{categories[0].name.ljust(largest, ' ')[h]:>6}{categories[1].name.ljust(largest, ' ')[h]:>3}" \
                     f"{categories[2].name.ljust(largest, ' ')[h]:>3}  \n"
    return chart


if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.4)
    business.withdraw(10.99)
    actual = create_spend_chart([business, food, entertainment])
    print(actual)
    expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    print(expected)
    print(actual==expected)