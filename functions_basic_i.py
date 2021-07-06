#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# will print out 5
#correct

# #2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#will give an error or will just return 5, most likely error
#correct but only about error

# #3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#will print 10
#wrong prints first return statement it runs into and exits function


# #4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#will only print 5, will not make it to the print(10) command
#correct

# #5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#will print 5 , print(x) will not print out anything else because nothing was returned
#half correct printed 5 but print(x) literally printed none

# #6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#will print 3 then 5 then None
#half correct printed 3 then 5 but couldn't add the nones so gave an error message
#moral of the story always return values :D

# #7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#will print 25
#correct

# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#will print 100 then 10
#correct

# #9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# #will print 7 then 14 then 21
#correct

# #10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#will print 8
#correct

# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#will print 500 then 500 then 300 then 500
#correct

# #12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#will print 500 then 500 then 300 then 300
#kind correct last print(b) is still 500 we returned b but never saved over

# #13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#will print 500 then 500 then 300 then 300
#correct

# #14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#will print 1 then 3 then 2
#correct

# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#will print 1 then 3 then 5 then 10
#correct