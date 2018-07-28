#this class will assess each variable for the requirements of MRA as well a perform MRA
import math
class MRA:


    def __init__(self, variable_0, variable_1, variable_2, variable_3, variable_4):
        self.variable_0 = variable_0
        self.variable_1 = variable_1
        self.variable_2 = variable_2
        self.variable_3 = variable_3
        self.variable_4 = variable_4


    def jarque_bera_test(self, variable): #Testing for Normality in each variable
        skewness = 0.0
        kurtosis = 0.0
        temp = []
        avg_variable = 0.0
        sample_size = len(variable)
        standard_deviation = 0.0
        numerator_skew = 0.0
        numerator_kurt = 0.0
        t = 0.0
        jb_statistic = 0.0
        significance_level = 0.05 #Chosen probability is 5%
        chi_sq_critical_value = 5.991
        num = 0

        for j in range(sample_size): #Calculation the mean
            num = num + variable[j]
        avg_variable = num/sample_size

        for h in range(len(variable)): #Calculating standard deviation
            t = t + ((variable[h] - avg_variable)**2)
        standard_deviation = math.sqrt(t/sample_size-1)

        for i in range(len(variable)):    #Calculating numerator for skewness formula
            numerator_skew = numerator_skew + ((variable[i] - avg_variable)**3)
            numerator_kurt = numerator_kurt + ((variable[i] - avg_variable)**4)

        skewness = numerator_skew/(sample_size*(standard_deviation**3))
        kurtosis = (numerator_kurt/(sample_size*(standard_deviation**4))) - 3
        print("Skewness", skewness)
        print("Kurtosis", kurtosis)

        jb_statistic = sample_size * ((skewness**2/6) + (kurtosis**2/24)) #jb statistic value should be compared with chi square critical value with df 2

        if jb_statistic < chi_sq_critical_value:
            print("Variable follows a Normal Distribution")
        else:
            print("Variable does not follow a Normal Distribution")


    def dagostino_test(self, variable):
        d_statistic = 0.0
        sample_size = len(variable)
        numerator = 0.0
        sum_of_sq = 0.0
        xi_sq = 0.0
        xi_all_sq = 0.0
        d_crit_min = 0.2740
        d_crit_max = 0.2862
        variable.sort()

        for j in range(sample_size):
            numerator = numerator + ((j-(sample_size+1/2))*(variable[j]))

        for h in range(sample_size):
            xi_sq = xi_sq + (variable[h]**2)
            xi_all_sq = xi_all_sq + variable[h]

        xi_all_sq = (xi_all_sq**2)

        sum_of_sq = xi_sq - (xi_all_sq/sample_size)

        d_statistic = numerator/math.sqrt((sample_size**3)*sum_of_sq)

        if d_statistic <= d_crit_min or d_statistic >= d_crit_max:
            print("Variable does not follow a Normal Distribution")
            print(d_statistic)
        else:
            print("Variable follows a normal distribution")
            print(d_statistic)


    def rel_btw_depV_and_indV(self, variable): #Checking if there is a linear relationship between dependent and independent variable
        pearson_coefficient = 0.0
        #assumption : variables need to follow normal distribution

















