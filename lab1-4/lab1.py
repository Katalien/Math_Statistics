import matplotlib.pyplot as plt
import os
import distribution as ds

sample_sizes = [10, 50, 1000]
loc, scale = 0.0, 1.0
bins_num = 25

def plot_hist(dist_name):
    if not os.path.isdir("plot_hist/"):
        os.makedirs("plot_hist/")
    label_name = str(dist_name) + " distribution"
    plt.figure(figsize=(15, 5)).suptitle(label_name)
    for i in range(len(sample_sizes)):
        sample = ds.get_sample(dist_name, sample_sizes[i])
        plt.subplot(1, 3, i + 1)
        n, bins, patches = plt.hist(sample, bins_num, density=True, edgecolor='black', alpha=0.6)
        y = ds.get_density_func(dist_name, bins)
        plt.plot(bins, y, color='red', lw=1)
        plt.title('$N=%i' %sample_sizes[i], fontsize=10)
        plt.xlabel('numbers')
        plt.ylabel('density')
    # plt.show()
    plt.savefig("plot_hist/" + label_name + ".png")

def run_lab1():
    for dist in ds.distributions:
        plot_hist(dist)

def main():
    run_lab1()

if __name__ == '__main__':
    main()
