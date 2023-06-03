pkg load interval

input = csvread("Channel_1_500nm_0.23mm.csv")
eps = 1e-4

input_int = infsup(input - eps, input + eps)

##data_int;
data_regr;
##data_regr_reduce;
##omegas;
##regr_residuals;
##regr_reduce_residuals;
##mode_freq;
##inform_set;
##corridor_of_joint_dep;

