#codecademy code challenge problem: prints a list with 'hello' added to the front of a list provided

def add_greetings(names):
  list=['Hello, ' + name for name in names]
  return list

print(add_greetings(["Owen", "Max", "Sophie"]))