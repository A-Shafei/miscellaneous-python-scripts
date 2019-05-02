def adder(num1):
    def inner(num2):
        def moreinner(num3):
            return num1 + num2 + num3
        return moreinner
    return inner

def generate_link(user):
    result = ""
    for item in user:
        if item == " ":
            result = result + "%20"
        else:
            result = result + item
    return result

print(generate_link('matt c'))
