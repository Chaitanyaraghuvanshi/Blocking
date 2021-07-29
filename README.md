# Data Linkage using Blocking
Blocking method
The blocks for linking data are formed using the first word in manufacturer name in the file ‘buy.csv’. These words are collected and stored in a list. In order to fill in the missing values (NaN) under the manufacturer column of the file, the name of manufacturer is computed using the first word under the ‘name’ column. However, we choose the second word under the product name column if the first word is the model number. 

Since the manufacturer name is not mentioned, we check the product name column. After removing the unwanted characters from the text (such as ‘-’), we check the first word. Since the first word is the model number we take the next word as our block name. To check for model number, we check if there is a digit using a regular expression (re.search(r'\d',word)). In our case we therefore get ‘Skagen’.

Further pre-processing is done by removing characters such as ‘,’ in block names and converting every word to lower case, forming our block keys. The list contains a block key for every product in ‘buy.csv’ already. A dataframe is then created with product id and its block key for ‘buy.csv’.

We then take the unique elements in the list as our blocks. Each product in ‘abt.csv’ is compared with all the blocks using the first word in the ‘name’ column of ‘abt’. Here, we assume that the first word in ‘name’ is always going to be the manufacturer name. If the word matches any of the blocks, we add the product id and the block key to the dataframe for ‘abt.csv’. However, if it doesn’t match, we normalise the first word in ‘name’ (by removing unwanted characters and converting to lower case) and consider it as a new block. 

Evaluation of Performance
The pair completeness (PC) and the reduction ratio (RR) came to be 0.95897903372835
and 0.9451650723621121 respectively. The relatively small value of false negatives (45) 
when compared to the number of true positives (1052) accounts for the high value of PC. 
Similarly, for RR the sum of false positives (63678) and true positives (1052) is relatively less than the total number of all possible record pairs from the two data sets (1180452). 

The largest paired block is ‘sony’ which requires 31506 comparisons. This makes the blocking extremely expensive to carry out. Further, the method used for blocking may not work in every case. If the manufacturer name has a digit in it, for example, ‘7UP’, then our program will consider it as model number. Furthermore, if the first word in ‘name’ column in Abt is not the manufacturer name, then our blocking method becomes incorrect.

