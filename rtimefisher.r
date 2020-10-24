test_ct <- 5e6
data <- c(30, 86, 24, 38)
testdata <- matrix(data, nrow=2)
for (i in 1:test_ct){
    fisher.test(testdata)
}
