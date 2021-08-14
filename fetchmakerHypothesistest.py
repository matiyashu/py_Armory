import numpy as np
import fetchmaker
# Number 7
from scipy.stats import binom_test
# Number 9
from scipy.stats import f_oneway
# Number 10
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# Number 13
from scipy.stats import chi2_contingency

# Number 1
fetch_maker = fetchmaker.dogs
# print(fetch_maker)

# Number 2
rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
# print(rottweiler_tl)

# Number 3
rottweiler_tl_mean = np.mean(rottweiler_tl)
rottweiler_tl_std = np.std(rottweiler_tl)
print('The rottweiler avg tail length is {} \n'. format(rottweiler_tl_mean))
print('The rottweiler std dev of tail length is {} \n'. format(rottweiler_tl_std))

# Number 4
whippet_rescue = fetchmaker.get_is_rescue('whippet')
# print(whippet_rescue)

# Number 5
# To count the number of entries that are not zero (1)
num_whippet_rescues = np.count_nonzero(whippet_rescue)
print('The count of (1) entry in the whippet_rescue is {} \n'.format(num_whippet_rescues))

# Number 6
# To get the number of samples using np.size
num_whippets = np.size(whippet_rescue)
print('The number of samples in the whippet_rescue is {} \n'.format(num_whippets))

# Number 7 and 8
expected_percentage_whippets_rescue = 0.08
binom_test_whippets_rescues = binom_test(num_whippet_rescues, num_whippets,expected_percentage_whippets_rescue)
print('The P-Value of the whippet_rescue is {} \n'.format(binom_test_whippets_rescues))
print('So the P-Value from the Whippet_Rescue Binomial Test is %.3f and therefore, we accept the null hypothesis, which is that there is no difference between the observed number of whippet rescues and our expected whippet rescues percentage'%(binom_test_whippets_rescues))
print('\n')

# Number 9
# since these datasets are numerical, we will be using ANOVA test to ensure the probability of False Positive stays 0.05 
whippets_weight = fetchmaker.get_weight('whippet')
terriers_weight = fetchmaker.get_weight('terrier')
pitbulls_weight = fetchmaker.get_weight('pitbull')
ANOVA_mid_size_dogs = f_oneway(whippets_weight, terriers_weight, pitbulls_weight)
print('The P-value obtained from the ANOVA test on these three popular breeds is %.3f and therefore, we reject the null hypothesis, which is there is significant difference in the average weights of these three dogs, but we do not know which pair of datasets is significantly different.'% (ANOVA_mid_size_dogs[1]))
print('\n')

# Number 10
# To know which pair has a significant difference in their mean, we must use Tukey's Range test
data = np.concatenate([whippets_weight, terriers_weight, pitbulls_weight])
labels = ['whippet'] * len(whippets_weight) + ['terrier'] * len(terriers_weight) + ['pitbull'] * len(pitbulls_weight)

tukey_result = pairwise_tukeyhsd(data, labels, alpha = 0.05)
print("Below is the table generated from the Tukey's Range Test to find out which pair of datasets is statistically different: \n {}".format(tukey_result))
print('\n')

# Number 11
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')
# print(poodle_colors)
# print(shihtzu_colors)

# Number 12
#First, obtain the color numbers for poodle breed
black_poodle = np.count_nonzero(poodle_colors == 'black')
brown_poodle = np.count_nonzero(poodle_colors == 'brown')
gold_poodle = np.count_nonzero(poodle_colors == 'gold')
grey_poodle = np.count_nonzero(poodle_colors == 'grey')
white_poodle = np.count_nonzero(poodle_colors == 'white')
#Secondly, obtain the color numbers for shihtzu breed
black_shihtzu = np.count_nonzero(shihtzu_colors == 'black')
brown_shihtzu = np.count_nonzero(shihtzu_colors == 'brown')
gold_shihtzu = np.count_nonzero(shihtzu_colors == 'gold')
grey_shihtzu = np.count_nonzero(shihtzu_colors == 'grey')
white_shihtzu = np.count_nonzero(shihtzu_colors == 'white')
#Next, create the contingency table using a list of lists
color_table = [[black_poodle, black_shihtzu],[brown_poodle, brown_shihtzu], [gold_poodle, gold_shihtzu], [grey_poodle, grey_shihtzu], [white_poodle, white_shihtzu]]

# Number 13
chi2, pval, dof, expected = chi2_contingency(color_table)
print('The statistic of the color_table dataset is %.3f \n'%(chi2))
print('The P-Value of the color_table dataset is %.3f \n'% (pval))
print('The degrees of freedom from the color_table dataset is {} \n'.format(dof))
print('The expected table is as follows: \n {}'.format(expected))
print('\n')
print('The conclusion from the Chi-Square test above is since the P-Value is %.3F, we reject the null hypothesis and stated that there is a significant difference between the datasets'% (pval))
