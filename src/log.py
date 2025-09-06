from decorators import log


@log(filename="log.txt")
def my_function(x, y):
    return x + y


if __name__ == "__main__":
    my_function(1, 2)
