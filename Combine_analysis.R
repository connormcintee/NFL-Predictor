library(readxl)
library(rpart)
library(dplyr)
data1=read_xlsx('~/Downloads/football_data/Combine_data.xlsx')
data1
data=as.data.frame(data1)
data
data2=filter(data, Pos == "RB")
plot(data2$BenchReps)
