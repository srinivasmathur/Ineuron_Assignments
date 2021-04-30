def compute(denominator):
  try:
    return 5/denominator
  except Exception as e:
    return e

print(compute(0))