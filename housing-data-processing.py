import pandas as pd


# import data from datasets
lihtc = pd.read_csv('./datasets/lihtc-ri-output.csv')  # ri low income housing tax credit data
sec_eight = pd.read_csv('./datasets/ri-sec-8.csv')  # ri section 8 active properties

#TODO: replace NaNs in the dataframes with ' ' to allow bug-free string building instead of ignoring address2

# build address strings for lihtc table
# extract important address strings
lihtc_addrs_cells = [lihtc.PROJ_ADD.values.tolist(),
                     lihtc.PROJ_CTY.values.tolist(),
                     lihtc.PROJ_ST.values.tolist()]
lihtc_addrs_tup = list(zip(*lihtc_addrs_cells))

lihtc_addrs_str = []  #initialize list of strings
for i in range(0, len(lihtc_addrs_tup)):
    lihtc_addrs_str.insert(0, ' '.join(lihtc_addrs_tup.pop()))

# build address strings for section eight table
sec_eight_addrs_cells = [sec_eight.address_line1_text.values.tolist(),
                         sec_eight.city_name_text.values.tolist(),
                         sec_eight.state_code.values.tolist()]
sec_eight_addrs_tup = list(zip(*sec_eight_addrs_cells))

sec_eight_addrs_str = []
for k in range(0, len(sec_eight_addrs_tup)):
    sec_eight_addrs_str.insert(0, ' '.join(sec_eight_addrs_tup.pop()))


# merge strings with property names

lidf = lihtc.PROJECT
lidf.name = 'Name'
sdf = sec_eight.property_name_text
sdf.name = 'Name'

df2 = pd.concat([lidf, pd.DataFrame(lihtc_addrs_str)], axis=1)
df3 = pd.concat([sdf, pd.DataFrame(sec_eight_addrs_str)], axis=1)

df = pd.concat([df2,df3])  # this dataframe has the names and addresses

# TODO: code by number of units
