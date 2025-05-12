# Custom RangeError Exception
class RangeError(Exception):
 pass
 # Function to check character count
 def check_file_character_count(filename):
     try:
        with open(filename, 'r') as file:
            content = file.read()
            char_count = len(content)
            print(f"Character count: {char_count}")
            if char_count < 100:
               raise RangeError("characters less than the range")
            else:
               print("Character count is within acceptable range.")
     except FileNotFoundError:
        print(f"File '{filename}' not found.")
     except RangeError as e:
        print("RangeError:", e)             
 check_file_character_count("sample.txt")