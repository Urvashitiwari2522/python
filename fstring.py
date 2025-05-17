# fstring is also known as literal string , the primary focus of this mechanisn  is to make the interpolation easier
letter = "hey, my name is {} and i am from {}"
name ="urvashi"
country ="Varanasi"
letter.format(name,country)
print(letter.format(name,country))
print(f"hey, my name is {name} and i am from {country}")