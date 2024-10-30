def safe_print_division(a, b):
    try:
        # Try to perform the division
        result = a / b
    except :
        # If an exception occurs (e.g., division by zero), set result to None
        result = None
    finally:
        # This block will always execute, regardless of an exception
        print("Inside result: {}".format(result))
    
    # Return the result of the division or None if an exception occurred
    return result
