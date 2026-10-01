# Task 1.1:
def read_two_ints():
    """Read two numbers from the user and returns them as integers."""
    #read x input and convert to integer
    x_string = input("give me x: ")
    x = int(x_string)
    #read y input and convert to integer
    y_string = input("give me y: ")
    y = int(y_string)
    return x,y

    
# Task 2.1:
def compute_multadd(a, b):
    """Computes and prints product and sum of 2 numbers"""
    #create equation to find the multiplication of our 2 integers
    mult_res = a * b
    #create equation to find product of our 2 integers
    add_res = a + b
    print("mult result:", mult_res)
    print("add result:", add_res)
    return mult_res/add_res

# Task 3.1:
def print_fancy(a, b, ab_multadd):
    """prints inputs and multadd results formatted with borders"""
    #print with borders in a neat organized way
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("================")


def main ():
    """Docstring for main function"""
    #call our outputs and invoke arguments
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
