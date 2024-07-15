def buy_food(price1, price2, amount1, amount2):
  total1 = price1*amount1
  total2 = price2*amount2
  return total1, total2

print(buy_food(7.99, 6.40, 4, 5))
