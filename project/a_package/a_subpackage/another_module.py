

print("main.another_module =", __package__, ",",  __name__)
def another_module_main():
    print("another_module.py =", __package__, ",",  __name__)
    #pass

def another_module_return_something():
    return "another module string"

if __name__ == '__main__':
    another_module_main()