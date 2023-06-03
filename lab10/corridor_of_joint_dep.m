xlimits = [1 size(input, 1)]

figure
hold on
ir_plotmodelset(irproblem, [-50 250])
errorbar(input, max(w2) * eps, "b")

xlim(xlimits)
ylim([input(1) - max(w2) * eps, input(end) + max(w2) * eps])

title("Corridor of joint dependencies")
xlabel("n")
ylabel("mV")

figure
hold on
ir_plotmodelset(irproblem, [-50 250])
errorbar(input, max(w2) * eps, "b")

xlim(xlimits)
ylim([input(1) - max(w2) * eps, input(end) + max(w2) * eps])

title("Corridor of joint dependencies")
xlabel("n")
ylabel("mV")
xlim("auto")
ylim("auto")


