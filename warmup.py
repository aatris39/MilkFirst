def getName():
  print("What is your name?")
  n = "Bob" # make this input() later
  return n

def printGreeting(nm):
  global name
  print("Hello, " + nm + ".  My name is " + name + ". How are you?")

name = "Alexa"
user = getName()
printGreeting(user)