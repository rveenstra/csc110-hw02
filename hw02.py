# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Read two numbers from the user and returns them as integers."""
    
    x_string = input("give me x: ")
    x = int(x_string)
    
    y_string = input("give me y: ")
    y = int(y_string)
    return x,y
    # ADD a Docstring for this function
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    
# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Computes and prints product and sum of 2 numbers"""
    mult_res = a * b
    add_res = a + b
    print("mult result: ", mult_res)
    print("add result: ", add_res)
    return mult_res/add_res

    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """prints inputs and multadd results formatted with borders"""
    print("****************")
    print("RESULTS:")
    print("first number: ", a)
    print("second number: ", b)
    print("multadd result: ", ab_multadd)
    print("================")
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below

def main ():
    """Docstring for main function"""
    x,y = read_two_ints()
    xy_multadd = compute_multadd(x, y)
    print_fancy(x, y, xy_multadd)
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    # TODO: add your call instead of this line

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    # TODO: add your call instead of this line

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    # TODO: add your call instead of this line


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
