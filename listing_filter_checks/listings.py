import pandas as pd

listings_df = pd.read_csv('listings.csv')
unit_groups_df = pd.read_csv('unitGroups.csv')

def printResults(df, msg=''):
    print(f"\n{msg}\n")
    print(f"Total: {len(df['Listing Id'].unique())}")
    print(df['Listing Name'].unique())


# Filter by bedroom size
print('BEDROOM SIZE')
filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') 
]

listing_ids = filtered_df['Listing Id'].tolist()

sro_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('Studio')) 
]

printResults(sro_filter, 'SRO')

# 1 bedroom
one_bd_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('One Bedroom')) 
]

printResults(one_bd_filter,'1 BD')

# 2 bedroom
two_bd_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('Two Bedroom')) 
]

printResults(two_bd_filter,'2 BD')

# 3 bedroom
three_bd_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('Three Bedroom')) 
]

printResults(three_bd_filter,'3 BD')

# 4+ bedroom
four_bd_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('Four')) # filter seems to have trouble with the + sign
]

printResults(four_bd_filter,'4+ BD')

# Filter by community type
print('COMMUNITY TYPE')
filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Community Types'].str.contains('Residents with Disabilities')) 
]

printResults(filtered_df, 'Disabilities')

filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Community Types'].str.contains('Veterans')) 
]

printResults(filtered_df, 'Veterans')

filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Community Types'].str.contains('Seniors 62+')) 
]

printResults(filtered_df, 'Seniors 62+')

filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Community Types'].str.contains('Supportive Housing for the Homeless')) 
]

printResults(filtered_df, 'Homeless')

filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Community Types'].str.contains('Families')) 
]

printResults(filtered_df, 'Seniors Families')

filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Community Types'].str.contains('Seniors 55+')) 
]

printResults(filtered_df, 'Seniors 55+')

# Filter by rent range
# NOTE - always return if Rent Type == 'Percentage Of Income'
# TODO - determine if 'Monthly Rent is null' is included in rent range filter results

# Filter by section 8
filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Accept Section 8'] == 'Yes') 
]

printResults(filtered_df, 'Section 8')