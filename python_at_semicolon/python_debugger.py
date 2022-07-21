a = 6
b = 8


def add(x, y):
    return x - y


# print(add(a, b))

def tell_me_more(language: str) -> str:
    languages = ("java", "python", "javaScript")
    assert language in languages, f"'{language}' not found"
    return language


try:
    print(tell_me_more("java"))
    print(tell_me_more("kiki"))
except:
    print("error")
