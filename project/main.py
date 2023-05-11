import a_package.a_module as a_module
import a_package.a_subpackage.another_module as another_module

print("main.py =", __package__, ",",  __name__)
def main():
    print("main.py =", __package__, ",",  __name__)
    #pass

def call_a_module():
    x = a_module.a_module_main()
    print(x)

def call_another_module():
    x = another_module.another_module_main()
    pass
    #print(x) #devuelve None

def call_another_module_return_something():
    x = another_module.another_module_return_something()
    print(x)

if __name__ == '__main__':
    #main()
    #call_a_module()
    call_another_module()
    call_another_module_return_something()