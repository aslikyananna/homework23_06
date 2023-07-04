x = 10
def my_functio():
     x = 20
     print("lokal", x)
     print("global", globals()["x"])
my_functio()
