n = int(input())
AC = 0
WA = 0
TLE = 0
RE = 0
for i in range(n):
  s = input()
  if s=="AC":
    AC+=1
  elif s=="WA":
    WA+=1
  elif s=="TLE":
    TLE+=1
  else:
    RE+=1
print(f"AC x {AC}")
print(f"WA x {WA}")
print(f"TLE x {TLE}")
print(f"RE x {RE}")