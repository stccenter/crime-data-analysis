library(glmnet)

setwd("C:\\Project\\Crime\\chapter\\Data\\8. Lasso")
loadx <- data.matrix(read.csv("Factors.csv"))
loady <- data.matrix(read.csv("Binary_variable.csv"))

x <- data.matrix(loadx[,(4:19)])
y <- data.matrix(loady[,2])

set.seed(12345)
cv.lasso <- cv.glmnet(x,y, family = "binomial", alpha=1,  type.measure = "deviance")#gaussian
plot(cv.lasso)

model <- glmnet(x, y, family = "binomial", alpha=1, lambda = cv.lasso$lambda.lse)

c(cv.lasso$lambda.min, cv.lasso$lambda.1se)
coef(cv.lasso, cv.lasso$lambda.min)
coef(cv.lasso, cv.lasso$lambda.1se)