def decorator(cb):
  def wrapper():
    print("Before")
    cb()
    print("After")

  return wrapper

@decorator
def foo():
  print("[This is the actual program...]")

foo()