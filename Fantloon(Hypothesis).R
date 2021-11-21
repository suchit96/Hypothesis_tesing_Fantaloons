
###############Hypothesis trsting#########################

##################Load a dataset#########################

library(readxl)

Fant<-read.csv(choose.files())
View(Fant)
attach(Fant)

table1<-table(Fant$Weekdays)
table1
table2<-table(Fant$Weekend)
table2
?prop.test
prop.test(x=c(113),n=(167))
# Weekdays (males) P-value = 0.6766467

prop.test(x=c(233),n=(287))
# Weekends (Females) P-value = 0.8118467
