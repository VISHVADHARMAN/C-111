import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd 
import csv

df=pd.read_csv("D:/C-111/data1.csv")
data=df["Math_score"].tolist()

#Plotting the Graph
#fig=ff.create_distplot([data],["Math Scores"],show_hist=False)
#fig.show()

#Calculating the Mean and Standard Deviation of The Population Data
mean=statistics.mean(data)
std_deviation=statistics.stdev(data)

print("Mean of Population --> ",mean)
print("Standard Devaition of Population --> ",std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

#Pass the number of time you want the mean of data points as a parameter in range function in for loop
mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
    
#Calculating the mean and std_deviation of the sampling distribution
std_deviation=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)

print("Mean of sampling distribution --> ",mean)

#Plotting the mean of the sampling
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))

#Finding the standard deviaitions starting and ending value
first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

print("Std 1",first_std_deviation_start,first_std_deviation_end)
print("Std 2",second_std_deviation_start,second_std_deviation_end)
print("Std 3",third_std_deviation_start,third_std_deviation_end)

#Plotting the graph with traces

fig.show()
