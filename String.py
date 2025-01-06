name = "Urvashi Tiwari .."
print("My name is:",name)
# Print the length of the name

Length = len(name)
print("Length is:",Length)
print(name[7:14])
print(name[:8])
print(name[-12:-1])

# used for searching 
if "Tiwari" in name:
    print("Yes")
else:
    print("No")

# the upper() method convert a string to upper case
print(name.upper())

# the lower() method convert a string to lower case 
print(name.lower())

# Strings are immutable in python or java
# The strip() method removes any white spaces after and before the string.
print(name.strip())   

# the rstrip() removes any trailing characters
print(name.rstrip("."))

# The replace() method replace all occurances of a strings with new strings
print(name.replace("U","S"))
print(name.replace("Tiwari","Pandey"))

# The split method() splits the given string
print(name.split(" "))
python= "second day of pratice"

""" The capitalize() method in Python converts the first character of a string 
 to uppercase and the rest to lowercase. This method is useful for formatting strings."""
print(python.capitalize())
print(len(name))

# the center() method aligns the string to the center as per the parameter given by the user
print(len(name.center(40)))

# The count()method returns the number of times the given value has occured in the given string
defination = """Python is a high-level, general-purpose programming language and Python is a versatile and powerful programming language"""
print(defination.count("Python"))

# The endswith() method checks if the string end with the given value, if yes then return true else false
print(defination.endswith("language"))

# The find() method search the first occurance of the given value
print(defination.find("programming"))
print(defination.find("programmings"))

# The index() method search the first occurance of the given value and return the index where it is present else raise an exception
print(defination.index("powerful"))

# A-Z,a-z,0-9
print(name.isalnum())
str2 ="Welcome00"
print(str2.isalnum())

# A-z,a-z
str1 = "welcome"
print(str1.isalpha())

# The islower() method return true if contains all the caracter in lower case, else returns false
print(str1.islower())

# The isprintable() method returns true if all the given strings are printable, if not, then return false 
print(str1.isprintable())

# The isspace method() return true if and only if the given string contains white spaces, if not, then return false
print(str2.isspace())

# The istitle method() returns true if the first letter of the each word of the string is capitalized, else return false
print(str2.istitle())

# The isupper() method return true if contains all the character in upper case, else return false
str3 ="STRING"
print(str3.isupper())

# The startswith() method checks if string starts with the given value. If yes then return true, else false
print(defination.startswith("Python"))

# The swapcase() method change the character casing of the string, uppercase converted to lowercase and lowercase to uppercase
print(name.swapcase())
print(defination.swapcase())

# The title() method capitalizes each letter of the word in the string
print(name.title())
print(defination.title())

