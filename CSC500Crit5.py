#Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
#The program should first ask for the number of years. The outer loop will iterate once for each year. The inner 
#loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the 
#inches of rainfall for that month. After all iterations, the program should display the number of months, the total 
#inches of rainfall, and the average rainfall per month for the entire period.
print('Part 1')
howManyYears = int(input('How many years of rainfall?'))
howManyMonths = howManyYears * 12
rainfallTotal = 0
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while howManyYears > 0:
    print('Year '+ str(howManyYears) +' :')


    for month in months:
        rainfall = float(input("How many inches for "+ month +":"))
        rainfallTotal += rainfall
    
    howManyYears -= 1

print('Total Months: '+ str(howManyMonths) +', Rainfall total:'+ str(rainfallTotal) +' inches, Average monthly rainfall:'+ str(round(rainfallTotal/howManyMonths,2)) +' per month')



    #If a customer purchases 0 books, they earn 0 points.
    #If a customer purchases 2 books, they earn 5 points.
    #If a customer purchases 4 books, they earn 15 points.
    #If a customer purchases 6 books, they earn 30 points.
    #If a customer purchases 8 or more books, they earn 60 points.

print('Part 2')

books = int(input('Enter the number of books purchased this month to receive points: '))
points=0
if books >= 2 and books < 4:
    points = 5
elif books >= 4 and books <6:
    points = 15
elif books >=6 and books <8:
    points = 30
elif books >=8:
    points = 60

print('Points this month: '+ str(points)+' points')
