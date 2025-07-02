from typing import Union

from fastapi import FastAPI, status

app = FastAPI()


# Addition
@app.post("/addition", status_code=status.HTTP_200_OK)
def print_addition(a, b):
    sum = int(a) + int(b)
    return {
        "a": a,
        "b": b,
        "sum": sum,
    }


# Subtraction
@app.post("/subtract", status_code=status.HTTP_200_OK)
def print_subtract(x, y):
    subtract = int(x) - int(y)
    return {
        "x": x,
        "y": y,
        "subtract": subtract,
    }


# Multiplication
@app.post("/multiply", status_code=status.HTTP_200_OK)
def print_multiply(a, b):
    result = int(a) * int(b)
    return {
        "a": a,
        "b": b,
        "product": result,
    }


# Division
@app.post("/divide", status_code=status.HTTP_200_OK)
def print_divide(x, y):
    result = int(x) / int(y)
    return {
        "x": x,
        "y": y,
        "quotient": result,
    }


# Modulus
@app.post("/modulus", status_code=status.HTTP_200_OK)
def print_modulus(c, d):
    result = int(c) % int(d)
    return {
        "c": c,
        "d": d,
        "modulus": result,
    }

# Power
@app.post("/power", status_code=status.HTTP_200_OK)
def print_power(a, b):
    result = int(a) ** int(b)
    return {
        "a": a, 
        "b": b, 
        "power": result
    }

# Square
@app.post("/square", status_code=status.HTTP_200_OK)
def print_square(z):
    result = int(z) ** 2
    return {
        "z": z,
        "square": result,
    }

# Square root 
@app.post("/square-root", status_code=status.HTTP_200_OK)
def print_square_root(x):
    result = int(x) ** 0.5
    return {
        "x": x, 
        "square_root": result
    }


# Cube
@app.post("/cube", status_code=status.HTTP_200_OK)
def print_cube(a):
    result = int(a) ** 3
    return {
        "a": a,
        "cube": result,
    }
    
# Percentage    
@app.post("/percentage", status_code=status.HTTP_200_OK)
def print_percentage(a, b):
    percentage = (int(a) / int(b)) * 100
    return {
        "a": a,
        "b": b,
        "percentage": percentage
    }    
    
    
    
