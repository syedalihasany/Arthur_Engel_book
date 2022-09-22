# Chapter 1 (The invariance principal)
# E1

x0 = 67.00                                      # x0 = a , y0 = b and x0 > y0 > 0
y0 = 4.00

x = x0
y = y0
for index in range(1000):
    x_next = (x + y)/2
    y_next = (2*x*y) / (x + y)
    x = x_next
    y = y_next

print("x is :")
print(x)
print("y is : ")
print(y)                                       # both x and y converge to approx sqrt(a*b) but I didn't get how arthur reaches to this conclusion              