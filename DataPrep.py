import csv
import math
from analysis.MultipleRegressionAnalysis import MRA

csv_filename = 'Manhattan_Property_On_Sale.csv' #each field will be stored in its own separate array
csv_rolling_sales = 'rollingsales_manhattan.csv'
street_address = []
Neighbourhood = []
Asking_Price = []
No_BR = []
No_Bath = []
Type_BLD = []
Sq_feet = []
med_neighbourhood_0 = []
med_neighbourhood_1 = []
med_neighbourhood_2 = []
med_neighbourhood_3 = []
med_neighbourhood_4 = []
med_neighbourhood_5 = []
med_neighbourhood_6 = []
med_neighbourhood_7 = []
med_neighbourhood_8 = []
med_neighbourhood_9 = []
med_neighbourhood_10 = []
med_neighbourhood_11 = []
med_neighbourhood_12 = []
med_neighbourhood_13 = []
med_neighbourhood_14 = []
med_neighbourhood_15 = []
med_neighbourhood_16 = []
med_neighbourhood_17 = []
med_neighbourhood_18 = []
med_neighbourhood_19 = []
med_neighbourhood_20 = []
med_neighbourhood_21 = []
med_neighbourhood_22 = []
population = {'TOTAL POP': 8242624, 'BRONX': 1385108, 'BROOKLYN': 2552911, 'MANHATTAN': 1585873, 'QUEENS': 2250002, 'STATEN ISLAND':468730}

def read_data(filename): #function reads data from csv file and stores in an array/python list
    data_array = []
    with open(filename) as csv_file:
        read_csv = csv.reader(csv_file)
        for each_row in read_csv:
            data_array.append(each_row)
    return data_array

data_array = read_data(csv_filename)

for index in data_array:
    street_address.append(index[0]) #each field is stored in its own array
    Neighbourhood.append(index[1])
    Asking_Price.append(index[2])
    No_BR.append(index[3])
    No_Bath.append(index[4])
    Sq_feet.append(index[5])
    Type_BLD.append(index[6])


street_address.pop(0) #removing heading from each fields
Neighbourhood.pop(0)
Asking_Price.pop(0)
No_Bath.pop(0)
No_BR.pop(0)
Sq_feet.pop(0)
Type_BLD.pop(0)

#cleaning each field of data to be used as a variables for MR analysis

#converting string arrays to int
No_BR = [float(i) for i in No_BR]
No_Bath = [float(j) for j in No_Bath]
Asking_Price = [int(h) for h in Asking_Price]



#converting Sq_feet items from string to integer

int_sq_feet = []
temp = [] #the temp array excludes empty datapoints
temp2 = [] #storing asking prices relative to temp
#finding the median of those data points and using the median as a replacement of the empty data points

#*********func
for i in range(len(Sq_feet)):
        if Sq_feet[i] == '':
            num = 0
        else:
            num = int(Sq_feet[i])
            temp.append(num)
            num2 = int(Asking_Price[i])
            temp2.append(num2) #going to find a correlation coefficient between these two variables, to estimate empty datapoint of variable sq_feet
        int_sq_feet.append(num)

#going to choose between using the median or the estimated value by line of best of fit
def median_calc(dataset):
    median = 0
    position = 0
    dataset.sort() #sorting array into ascending order
    if dataset.__len__() % 2 == 0:
        position = int(math.ceil((dataset.__len__() + 1) / 2 - 1))
        median = (dataset[position] + dataset[position +1])/2
    else:
        position = int(math.ceil((dataset.__len__() + 1) /2 - 1))
        median = dataset[position]
    return median

#simple linear regression to estimate empty data points for sq_feet variables
def average_arr(array):
    count = 0
    mean = 0
    for i in array:
        count = count + i
    mean = count/len(array)
    return mean

def simple_lin_regre(array_x, array_y):  #y = ax +b where y is the asking price and x the square feet of the property
    avg_array_x = average_arr(array_x)
    avg_array_y= average_arr(array_y)
    x_coeff = 0 #to calculate this value we need the correlation coefficient as well as Sy and Sx
    intercept = 0 # intercept = y estimate - x_coeff (x estimate)
    sum_of_y = 0
    sum_of_x = 0
    sum_of_x_squared = 0
    sum_of_xy = 0 # sum of product of x and y
    n = int(len(array_x))

    for i in range(n):
        sum_of_y = sum_of_y + array_y[i]
        sum_of_x = sum_of_x + array_x[i]
        sum_of_x_squared = sum_of_x_squared + (array_x[i] ** 2)
        sum_of_xy = sum_of_xy + (array_x[i]*array_y[i])

        x_coeff = (n*sum_of_xy - (sum_of_x)*(sum_of_y))/(n*sum_of_x_squared - (sum_of_x**2))
        intercept = (sum_of_y/n - x_coeff*(sum_of_x/n))
    a = [x_coeff, intercept]
    return a

h = simple_lin_regre(temp, temp2)
#replacing empty data points with estimated sq feet
for i in range(len(Sq_feet)):
    if Sq_feet[i] == '':
        int_sq_feet[i] = math.floor((int(Asking_Price[i]) - h[1])/h[0])

#finding the median of properties according to neighbourhood
#removing empty data points

def med_price_per_neighbourhood(name_of_neighbourhood):
    data_array_2 = read_data(csv_rolling_sales)
    neighbourhood_array = []
    temp3 = []
    sale_price = []
    temp4 = []
    median_value = 0

    for i in range(len(data_array_2)):
        if data_array_2[i][9] != '0': #filtering out records that have no sale price value
            if data_array_2[i][9] != '': #filtering out records of sales price that have not been documented
                if data_array_2[i][0] != '': #filtering out records of neighbourhoods that have not been documented
                    temp3.append(data_array_2[i][9])
                    neighbourhood_array.append(data_array_2[i][0])

    #converting list of strings to list of ints

    del temp3[0]
    for i in range(len(temp3)):
        sale_price.append(int(temp3[i]))

    #print(len(sale_price))
    #grouping sales prices according to neighbourhood

    del neighbourhood_array[0]
    for i in range(len(neighbourhood_array)):
       if name_of_neighbourhood == 'UPPER EAST SIDE' and (neighbourhood_array[i] == 'UPPER EAST SIDE (59-79)' or neighbourhood_array[i] == 'UPPER EAST SIDE (79-96)'):
            med_neighbourhood_0.append(sale_price[i])
       elif name_of_neighbourhood == 'UPPER WEST SIDE' and (neighbourhood_array[i] == 'UPPER WEST SIDE (59-79)' or neighbourhood_array[i] == 'UPPER WEST SIDE (79-96)' or neighbourhood_array[i] == 'UPPER WEST SIDE (96-116)'):
           med_neighbourhood_1.append(sale_price[i])
       elif name_of_neighbourhood == 'SOUTH BRIDGE' and neighbourhood_array[i] == 'SOUTH BRIDGE':
           med_neighbourhood_2.append(sale_price[i])
       elif name_of_neighbourhood == 'ROOSEVELT ISLAND' and neighbourhood_array[i] == 'ROOSEVELT ISLAND':
           med_neighbourhood_3.append(sale_price[i])
       elif name_of_neighbourhood == 'MURRAY HILL' and neighbourhood_array[i] == 'MURRAY HILL':
           med_neighbourhood_4.append(sale_price[i])
       elif name_of_neighbourhood == 'MORININGSIDE HEIGHTS' and neighbourhood_array[i] == 'MORNINGSIDE HEIGHTS':
          med_neighbourhood_5.append(sale_price[i])
       elif name_of_neighbourhood == 'MIDTOWN' and (neighbourhood_array[i] == 'MIDTOWN WEST' or neighbourhood_array[i] == 'MIDTOWN EAST' or neighbourhood_array[i] == 'MIDTOWN CBD'):
           med_neighbourhood_6.append(sale_price[i])
       elif name_of_neighbourhood == 'WASHINGTON HEIGHTS' and (neighbourhood_array[i] == 'WASHINGTON HEIGHTS LOWER' or neighbourhood_array[i] == 'WASHINGTON HEIGHTS UPPER'):
           med_neighbourhood_7.append(sale_price[i])
       elif name_of_neighbourhood == 'SOHO' and neighbourhood_array[i] == 'SOHO':
           med_neighbourhood_8.append(sale_price[i])
       elif name_of_neighbourhood == 'GRAMERCY' and neighbourhood_array[i] == 'GRAMERCY':
            med_neighbourhood_9.append(sale_price[i])
       elif name_of_neighbourhood == 'TRIBECA' and neighbourhood_array[i] == 'TRIBECA':
           med_neighbourhood_10.append(sale_price[i])
       elif name_of_neighbourhood == 'CHELSEA' and neighbourhood_array[i] == 'CHELSEA':
           med_neighbourhood_11.append(sale_price[i])
       elif name_of_neighbourhood == 'FLATIRON' and neighbourhood_array[i] == 'FLATIRON':
           med_neighbourhood_12.append(sale_price[i])
       elif name_of_neighbourhood == 'ALPHABET CITY' and neighbourhood_array[i] == 'ALPHABET CITY':
           med_neighbourhood_13.append(sale_price[i])
       elif name_of_neighbourhood == 'CLINTON' and neighbourhood_array[i] == 'CLINTON':
           med_neighbourhood_14.append(sale_price[i])
       elif name_of_neighbourhood == 'EAST VILLAGE' and neighbourhood_array[i] == 'EAST VILLAGE':
           med_neighbourhood_15.append(sale_price[i])
       elif name_of_neighbourhood == 'FINANCIAL' and neighbourhood_array[i] == 'FINANCIAL':
           med_neighbourhood_16.append(sale_price[i])
       elif name_of_neighbourhood == 'GREENWICH' and (neighbourhood_array[i] == 'GREENWICH VILLAGE CENTRAL' or neighbourhood_array[i] == 'GREENWICH VILLAGE WEST'):
            med_neighbourhood_17.append(sale_price[i])
       elif name_of_neighbourhood == 'HARLEM' and (neighbourhood_array[i] == 'HARLEM CENTRAL' or neighbourhood_array[i] == 'HARLEM EAST' or neighbourhood_array[i] == 'HARLEM UPPER'):
           med_neighbourhood_18.append(sale_price[i])
       elif name_of_neighbourhood == 'KIPS BAY' and neighbourhood_array[i] == 'KIPS BAY':
           med_neighbourhood_19.append(sale_price[i])
       elif name_of_neighbourhood == 'INWOOD' and neighbourhood_array[i] == 'INWOOD':
           med_neighbourhood_20.append(sale_price[i])
       elif name_of_neighbourhood == 'LOWER EAST SIDE' and neighbourhood_array[i] == 'LOWER EAST SIDE':
           med_neighbourhood_21.append(sale_price[i])
       else:
           med_neighbourhood_22.append(sale_price[i]) #MANHATTAN VALLEY

    temp4 = [med_neighbourhood_0, med_neighbourhood_1, med_neighbourhood_2, med_neighbourhood_3, med_neighbourhood_4, med_neighbourhood_5, med_neighbourhood_6, med_neighbourhood_7, med_neighbourhood_8,
             med_neighbourhood_10, med_neighbourhood_9, med_neighbourhood_11, med_neighbourhood_12, med_neighbourhood_13, med_neighbourhood_14, med_neighbourhood_15, med_neighbourhood_16, med_neighbourhood_17,
             med_neighbourhood_18, med_neighbourhood_19, med_neighbourhood_20, med_neighbourhood_21, med_neighbourhood_22]

    for index in temp4:
        if index:
            median_value = median_calc(index)
    return median_value


def get_neighbourhood_pop(name_of_a_neighbourhood):
    return population[name_of_a_neighbourhood]


a = MRA(int_sq_feet, No_Bath, No_BR, Asking_Price, Neighbourhood)
a.jarque_bera_test(Asking_Price)
a.dagostino_test(Asking_Price)

a.jarque_bera_test(int_sq_feet)
a.dagostino_test(int_sq_feet)

a.jarque_bera_test(No_Bath)
a.dagostino_test(No_Bath)

a.jarque_bera_test(No_BR)
a.dagostino_test(No_BR)
















