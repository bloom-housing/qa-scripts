import pandas as pd
import re

listings_df = pd.read_csv('listings.csv')
unit_groups_df = pd.read_csv('unitGroups.csv')

active_listings_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') 
]

def printResults(df, msg=''):
    print(f"\n{msg}\n")
    print(f"Total: {len(df['Listing Id'].unique())}")
    print(df['Listing Name'].unique())

# TODO - research if pandas has a built in way to extract rent ranges from column
def rentFilter(df, min_rent, max_rent):
    listings = []

    for i, row in rent_df.iterrows():
        if row['Listing Name'] not in listings:
            if '%' in row['Monthly Rent']:
                listings.append(row['Listing Name'])
            else:
                rent_string = row['Monthly Rent']
                numbers_as_strings = re.findall(r'\d+', rent_string)
                for n in numbers_as_strings:
                    if min_rent >= int(n) and max_rent <= int(n):
                        listings.append(row['Listing Name'])
                        break

    print(len(listings))
    print(listings)

# Filter by bedroom size
print('BEDROOM SIZE')

active_listing_ids = active_listings_df['Listing Id'].tolist()

sro_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(active_listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('Studio')) 
]

printResults(sro_filter, 'SRO')

# 1 bedroom
one_bd_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(active_listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('One Bedroom')) 
]

printResults(one_bd_filter,'1 BD')

# 2 bedroom
two_bd_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(active_listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('Two Bedroom')) 
]

printResults(two_bd_filter,'2 BD')

# 3 bedroom
three_bd_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(active_listing_ids)) &
    (unit_groups_df['Unit Types'].str.contains('Three Bedroom')) 
]

printResults(three_bd_filter,'3 BD')

# 4+ bedroom
four_bd_filter = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(active_listing_ids)) &
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

printResults(filtered_df, 'Families')

filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Community Types'].str.contains('Seniors 55+')) 
]

printResults(filtered_df, 'Seniors 55+')

# Filter by rent range
print('RENT RANGE')
rent_df = unit_groups_df.loc[
    (unit_groups_df['Listing Id'].isin(active_listing_ids))
]

# ignore null fields
rent_df = rent_df.dropna(subset=['Monthly Rent'])

min_rent = 0
max_rent = 0
rentFilter(rent_df, min_rent, max_rent)

# Filter by section 8
filtered_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') &
    (listings_df['Accept Section 8'] == 'Yes') 
]

printResults(filtered_df, 'Section 8')