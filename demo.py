import pyconsole_codes
import pyconsole_codes.decode
import pyconsole_codes.encode
# text = "\033[32m Hello, World! \033[0m"
# print(text)
#print("\x1bZ1 123456\x1bM132543")
a = pyconsole_codes.decode.decode("\033[32m Hello, World! \033[0m")
b = pyconsole_codes.encode.encode(a)
print(b)
