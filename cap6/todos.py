todos = open("todos.txt", "a")

print("Put out the trash.", file=todos)
print("Feed the cat.", file=todos)
print("Prepare tax return.", file=todos)

todos.close
