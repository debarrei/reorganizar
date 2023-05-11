import sys


# main.py
def main():
    # Your program goes here
    pass

#print('\n'.join(sys.path))
print("main.py =", __package__, ",",  __name__)

if __name__ == '__main__':
    main()