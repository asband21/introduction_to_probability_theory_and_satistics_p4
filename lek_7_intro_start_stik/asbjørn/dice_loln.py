import numpy as np
import matplotlib.pyplot as plt

def roll_die(sides,n_experiments):
	return np.random.randint(1, sides+1,n_experiments)

def get_sample_mean_at_n(values):
	i = np.arange(1,np.size(values)+1)
	sample_mean = np.cumsum(values)/i
	return sample_mean

def get_sample_variance_at_n(values, sample_mean):
	i = np.arange(1,np.size(values)+1)
	sample_variance = np.cumsum(np.power(values-sample_mean,2))/(i-1)
	sample_std = np.sqrt(sample_variance)
	plus_std = sample_mean+sample_std
	minus_std = sample_mean-sample_std
	return sample_variance, sample_std, plus_std, minus_std

def create_histogram(values):
	n_bins = np.amax(values)
	beans = np.arange(0,n_bins+3)
	absolute_histogram, bns = np.histogram(values,bins=beans)
	normalized_histogram = absolute_histogram/np.size(values)
	return beans[:-1], absolute_histogram, normalized_histogram

if __name__=="__main__":
	n_sides = 6
	n_experiments = int(1e3)

	outcomes = roll_die(n_sides, n_experiments)
	mu = get_sample_mean_at_n(outcomes)
	sigma2, sigma, mu_plus_sigma, mu_minus_sigma = get_sample_variance_at_n(outcomes,mu) 
	
	plt.figure()
	plt.plot(outcomes, 'o', label="Outcomes")
	plt.plot(mu, label="Sample mean")
	plt.plot(mu_plus_sigma, 'g', label="Mean +- std")
	plt.plot(mu_minus_sigma, 'g')
	plt.xlabel("i-th dice roll")
	plt.ylabel("Value")
	plt.legend()


	plt.figure()
	plt.hist(outcomes, bins=6)			# Easily plot a histogram of the outcomes

	bns, abs_hist, norm_hist = create_histogram(outcomes) # Create histogram with function
	plt.figure()
	plt.bar(bns,norm_hist,width=1, align='center')
	plt.show()


