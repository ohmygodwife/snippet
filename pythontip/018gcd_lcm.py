a=3
b = 60

x = b / a
end = int(round(pow(x, 0.5)))
for i in range(1, end+1):
  if x % i == 0:
    m = i
    n = x / i

print a*m, a*n