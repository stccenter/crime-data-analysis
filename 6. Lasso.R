library(glmnet)

setwd("C:\\Project\\Crime\\RegressionModel\\data\\")
loaddata <- data.matrix(read.csv("Factors.csv"))

x <- data.matrix(loaddata[,(3:15)])
y <- data.matrix(loaddata[,(16)])

set.seed(54321)
cv.lasso <- cv.glmnet(x,y, family = "binomial", alpha=1,  type.measure = "deviance")#gaussian
plot(cv.lasso)

model <- glmnet(x, y, family = "binomial", alpha=1, lambda = cv.lasso$lambda.lse)

c(cv.lasso$lambda.min, cv.lasso$lambda.1se)
coef(cv.lasso, cv.lasso$lambda.min)
coef(cv.lasso, cv.lasso$lambda.1se)