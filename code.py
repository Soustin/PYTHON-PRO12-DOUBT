import plotly.figure_factory as pff
import statistics
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

reading_list = df["reading score"].to_list()

mean = statistics.mean(reading_list)
std_deviation = statistics.stdev(reading_list)
median = statistics.median(reading_list)
mode= statistics.mode(reading_list)

print("mean =", mean, "median =", median, "mode =", mode)
print(std_deviation)

first_std_dev_start, first_std_dev_end = mean - std_deviation, mean + std_deviation
sec_std_dev_start, sec_std_dev_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_dev_start, third_std_dev_end = mean - (3*std_deviation), mean + (3*std_deviation)

list_of_data_within_1_std_dev = [result for result in reading_list if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_std_dev = [result for result in reading_list if result > sec_std_dev_start and result < sec_std_dev_end]
list_of_data_within_3_std_dev = [result for result in reading_list if result > third_std_dev_start and result < third_std_dev_end]

print("Percentage of data lies within first standard deviation", format(len(list_of_data_within_1_std_dev)*100/len(reading_list)))
print("Percentage of data lies within second standard deviation", format(len(list_of_data_within_2_std_dev)*100/len(reading_list)))
print("Percentage of data lies within third standard deviation", format(len(list_of_data_within_3_std_dev)*100/len(reading_list)))

read_list = [reading_list]
std_1_st = [first_std_dev_start]
std_1_end = [first_std_dev_end]
std_2_st = [sec_std_dev_start]
std_2_end = [sec_std_dev_end]
mean_1 = [mean]

hist_data = [reading_list, first_std_dev_start, first_std_dev_end, sec_std_dev_start, sec_std_dev_end, mean]
group_labels = ['reading-list','standard_Deviation 1 Start', 'standard_Deviation 1 End', 'standard_Deviation 2 Start', 'standard_Deviation 2 End', 'Mean']
Fig = pff.create_distplot(hist_data, group_labels, show_hist = False, curve_type = 'normal')
Fig.show()