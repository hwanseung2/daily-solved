def checking(f, name):
    print("check start")
    f(name)
    print("check end")
    return f

@checking
def naming(naming, name):
    print(f"name: {name}")

naming("hwanseung")