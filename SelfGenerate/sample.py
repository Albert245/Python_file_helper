import inspect

# Define the function to generate its own code
def generate_factorial_code():
    # Generate the code dynamically
    code = '''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
'''

    return code

# Generate the code for the factorial function
factorial_code = generate_factorial_code()

# Execute the generated code
exec(factorial_code)

# Call the factorial function
result = factorial(5)
print(result)