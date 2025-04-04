def Sugar_added_decorator(func):
    def wrapper():
        print("here's your tea! with Sugar! ☕ + 🤭 ")
        func()
    return wrapper

@Sugar_added_decorator
def give_me_tea():
    print("here's your tea! ☕")

give_me_tea()