n = 16
exp = 0
i = n
while i > 1:
  if n%2 == 0:
    i = i/2
    exp += 1
  else:
    break
else:
  print(n,"is 2 to the", exp)
