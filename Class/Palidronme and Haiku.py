'''
Palidronme or not
ex: 1234321 is a palidronme because it reads the same backward as forward

'''
import re

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input()
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

'''
Haiku

'''
def clean_haiku(haiku):
    lines = haiku.split("\n") 
    lines = [line.lower()
                 .replace("[^a-z]","")
                 .strip() for line in lines]
    return lines

def count_syllables(line):
  words = line.split(" ")
  count = 0
  for word in words:
    matches = re.findall("[aeiouy]+", word)
    if word.endswith("e") and len(matches) > 1:
        count -= 1
    count += len(matches)
  return count

def validate_haiku(haiku):
    lines = clean_haiku(haiku)
    if len(lines) != 3:
        return False
    counts = [count_syllables(line) for line in lines]
    if counts != [5, 7, 5]:
        return False
    return True

#Test
tests = ["An old silent pond...\nA frog jumps into the pond,\nsplash! Silence again.",
         "My code is cool, right?\nJava # Python ; Ruby // Go:\nI know them all, yay!",
         "Autumn moonlight -\naworm digs silently\ninto the chestnut."]

print(tests)
for test in tests:
    print(validate_haiku(test))
    

