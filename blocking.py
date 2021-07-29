import pandas as pd
import re
df_abt=pd.read_csv('abt.csv',encoding = 'ISO-8859-1')
df_buy=pd.read_csv('buy.csv',encoding = 'ISO-8859-1')
headings_buy = df_buy.columns
headings_abt = df_abt.columns

abt_blocks = pd.DataFrame(columns = ['block_key', 'product_id'])
buy_blocks = pd.DataFrame(columns = ['block_key', 'product_id'])

block_list=list(df_buy[headings_buy[3]])

for index in range(len(block_list)):
    if(str(block_list[index])=='nan'):

        product_name= df_buy[headings_buy[1]][index]
        p_list= (product_name.replace('-','')).split()
        
        #gets the manufacturer from product name
        for i in range(len(p_list)):
            if not bool(re.search(r'\d',p_list[i])):
                block_list[index]=p_list[i].lower()
                break
                
#gets a list of normalised manufacturer name  
block_list = [(str(block.split()[0]).replace(',','')).lower() for block in block_list]

for index in range(len(block_list)):
    buy_blocks.loc[index,'block_key']=block_list[index] 
    buy_blocks.loc[index,'product_id']=df_buy[headings_buy[0]][index]
buy_blocks.to_csv(r'buy_blocks.csv',index = False)

block_list = list(set(block_list))


i=0
for index in range(df_abt[headings_abt[1]].size):
    flag = 1
    for block in block_list:
        if (str((df_abt[headings_abt[1]][index]).split()[0]).replace(',','')).lower() == block:
            abt_blocks.loc[i,'block_key']=block 
            abt_blocks.loc[i,'product_id']=df_abt[headings_abt[0]][index]
            i+=1
            flag = 0
    if flag:
        abt_blocks.loc[i,'block_key']=(str((df_abt[headings_abt[1]][index]).split()[0]).replace(',','')).lower()
        abt_blocks.loc[i,'product_id']=df_abt[headings_abt[0]][index]
        i+=1        
abt_blocks.to_csv(r'abt_blocks.csv',index = False)         
