from Calculator.Square import squaring
from Calculator.Division import division
from Statistics.PopulationMean import populationmean


def variance(num):
    try:
        pop_mean = populationmean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + squaring(i-pop_mean)
        return division(x, num_values)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")