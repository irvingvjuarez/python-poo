def decorator(cb):
  def wrapper(*args):
    print("Before")
    cb(*args)
    print("After")

  return wrapper

@decorator
def foo():
  print("[This is the actual program...]")


if __name__ == "__main__":
	foo()