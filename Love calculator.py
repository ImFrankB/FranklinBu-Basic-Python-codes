

print("Welcome to love calculator")

name1= input("First name: ")
name2= input("Second name: ")

combined_name = name1 + name2
Lowered_name = combined_name.lower()

t = Lowered_name.count("t")
r = Lowered_name.count("r")
u = Lowered_name.count("u")
e = Lowered_name.count("e")

fdigit= t+r+u+e

l = Lowered_name.count("l")
o = Lowered_name.count("o")
v = Lowered_name.count("v")
e = Lowered_name.count("e")

Sdigit = l+o+v+e

score = int(str(fdigit) + str(Sdigit))

print(f"T = {t}")
print(f"R = {r}")
print(f"U = {u}")
print(f"E = {e}")

print(f"L = {l}")
print(f"o = {o}")
print(f"v = {v}")
print(f"E = {e}")


print(f"your score is {score}.")

    
    




 