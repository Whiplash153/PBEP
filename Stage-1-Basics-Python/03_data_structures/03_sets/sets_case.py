registered = {"alice", "bob", "carol", "dave"}

active = {"carol", "dave", "eve"}

inactive = registered - active

ghosts = active - registered

loyal = active & registered

print("registered:", registered)
print("active:", active)
print("inactive:", inactive)
print("ghosts:", ghosts)
print("loyal:", loyal)