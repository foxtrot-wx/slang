import interpreter
## shell.py

# just for testing, will overhaul later
# while True:
#     raw = input('$ ')
#     print(interpreter.slang(raw))

with open('testfile.slg', 'r') as f:
    rf = f.read()

print(interpreter.slang(rf))