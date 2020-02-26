player = {
  "x": 500
}
x = 200

if player["x"] < x:
  x = 300
else:
  player["x"] += 1

print(x)
print(player["x"])