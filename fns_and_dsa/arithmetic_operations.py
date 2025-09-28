def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    
    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (string): Operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    float or string: Result of the operation or error message
    """
    operation = operation.lower().strip()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'"
