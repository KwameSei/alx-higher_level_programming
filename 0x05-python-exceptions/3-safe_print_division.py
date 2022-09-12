#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        results = a / b
        print("Inside result: {:.1f}". format(results))
    except:
        results = None
        print("Inside result: {}". format(results))
    finally:
        return results
