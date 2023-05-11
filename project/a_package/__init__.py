from a_package.a_subpackage.another_module import another_module_main

print("init del package")

print("__init__.py =", __package__, ",",  __name__)

#another_module_main()

if __name__ == '__main__':
    another_module_main()