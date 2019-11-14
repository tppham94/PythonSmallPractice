def divide (number):
  try:
    return 50/number
  except ZeroDivisionError:
    print("Trying to divide by 0 here.")

print(divide(5))
print(divide(10))
print(divide(0))
