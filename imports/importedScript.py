
def myFunction():    
    print('This is the imported Script. The value of __name__ is ' + __name__)

def main():    
    myFunction()

main()

if __name__ == '__main__':    
    main()