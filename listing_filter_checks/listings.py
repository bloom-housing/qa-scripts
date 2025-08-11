import pandas as pd
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("listings_csv_path", help="file path of the listings csv export")
parser.add_argument("units_csv_path", help="file path of the units csv export")
args = parser.parse_args()

listings_df = pd.read_csv(args.listings_csv_path)
unit_groups_df = pd.read_csv(args.units_csv_path)

active_listings_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') 
]

def printResults(df, msg=''):
    print(f"\n{msg}\n")
    print(f"Total: {len(df['Listing Id'].unique())}")
    print(df['Listing Name'].unique())

# TODO - research if pandas has a built in way to extract rent ranges from column
def rentFilter(df, min_rent=None, max_rent=None):
    listings = []

    for i, row in rent_df.iterrows():
        if row['Listing Name'] not in listings:
            if '%' in row['Monthly Rent']:
                listings.append(row['Listing Name'])
            else:
                rent_string = row['Monthly Rent']
                numbers_as_strings = re.findall(r'\d+', rent_string)
                min_r_check = False
                max_r_check = False
                for n in numbers_as_strings:
                    if min_rent >= int(n):
                        min_r_check = True
                    if max_rent <= int(n):
                        max_r_check = True
                    if min_r_check and max_r_check:
                        listings.append(row['Listing Name'])
                        break

    print(len(listings))
    print(listings)

def unit_filter(unit_type):
    df = unit_groups_df.loc[
        (unit_groups_df['Listing Id'].isin(active_listing_ids)) &
        (unit_groups_df['Unit Types'].str.contains(unit_type)) 
    ]
    return df

def community_filter(com_type):
    df = listings_df.loc[
        (listings_df['Listing Status'] == 'Public') &
        (listings_df['Community Types'].str.contains(com_type)) 
    ]
    return df

# Filter by bedroom size
print('BEDROOM SIZE')

active_listing_ids = active_listings_df['Listing Id'].tolist()

# Studio
sro_filter = unit_filter('Studio')
printResults(sro_filter, 'SRO')

# 1 bedroom
one_bd_filter = unit_filter('One Bedroom')
printResults(one_bd_filter,'1 BD')

# 2 bedroom
two_bd_filter = unit_filter('Two Bedroom')
printResults(two_bd_filter,'2 BD')

# 3 bedroom
three_bd_filter = unit_filter('Three Bedroom')
printResults(three_bd_filter,'3 BD')

# 4+ bedroom
four_bd_filter = unit_filter('Four') # filter seems to have trouble with the + sign
printResults(four_bd_filter,'4+ BD')

# Filter by community type
print('COMMUNITY TYPE')
filtered_df = community_filter('Residents with Disabilities')
printResults(filtered_df, 'Disabilities')

filtered_df = community_filter('Veterans')
printResults(filtered_df, 'Veterans')

filtered_df = community_filter('Seniors 62+')
printResults(filtered_df, 'Seniors 62+')

filtered_df = community_filter('Supportive Housing for the Homeless')
printResults(filtered_df, 'Homeless')

filtered_df = community_filter('Families')
printResults(filtered_df, 'Families')

filtered_df = community_filter('Seniors 55+')
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

