dictionary = {
  'ram':200,
  'shyam':249,
  'Shreeya':388

}
topper =None
heighest = 0

for x, y in dictionary.items():
  if y >heighest:
    heighest = y
    topper = x

print (f"Topper is {topper} with marks {heighest}")