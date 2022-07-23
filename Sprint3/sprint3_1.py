def outer(name):
    def inner():
        print("Hello, {}!".format(name))
    return inner


tom=outer("Tom")
tom()
