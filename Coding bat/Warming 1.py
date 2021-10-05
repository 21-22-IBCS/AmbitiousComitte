#1 Sleep in
'''
1/The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


    sleep_in(False, False) → True
    sleep_in(True, False) → False
    sleep_in(False, True) → True

'''
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
print(sleep_in(True, False))

#2 Diff 21
'''
2/
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


 diff21(19) → 2
 diff21(10) → 11
 diff21(21) → 0

'''
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

number = diff21(10)
print(number)

#3 nearHundred
'''

Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

'''
#4 missing_char
'''

Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

'''
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

print(near_hundred(int(input())))

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
