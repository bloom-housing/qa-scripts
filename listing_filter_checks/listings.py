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

community_type_map = {
    '1': 'Residents with Disabilities',
    '2': 'Veterans',
    '3': 'Seniors 62+',
    '4': 'Supportive Housing for the Homeless',
    '5': 'Families',
    '6': 'Seniors 55+'
}

bed_size_map = {
    '0': 'Studio',
    '1': 'One Bedroom',
    '2': 'Two Bedroom',
    '3': 'Three Bedroom',
    '4': 'Four'
}
active_listing_ids = active_listings_df['Listing Id'].tolist()

filter_group = input("Enter group to filter by:\nc = community type\nu = unit type\ns = section 8\nr = rent range\n")

if filter_group == 'u':
    # Filter by bedroom size
    bed_size_select = input("Enter bedroom size:\n0 = studio\n1 = 1 bedroom\n2 = 2 bedroom\n3 = 3 bedroom\n4 = 4+ bedroom\nq = quit\n")
    print('BEDROOM SIZE')
    bed_size = bed_size_map[bed_size_select]
    # TODO - handle invalid bed size
    bed_size_filter = unit_filter(bed_size)
    printResults(bed_size_filter, bed_size)
elif filter_group == 'c':
    # Filter by community type
    com_select = input("Enter a community type:\n1 = disabilities\n2 = veterans\n3 = seniors 62+\n4 = homeless\n5 = families\n6 = seniors 55+\nq = quit\n")
    print('COMMUNITY TYPE')
    com_type = community_type_map[com_select]
    # TODO handle invalid input
    filtered_df = community_filter(com_type)
    printResults(filtered_df, com_type)
elif filter_group == 's':
    # Filter by section 8
    filtered_df = listings_df.loc[
        (listings_df['Listing Status'] == 'Public') &
        (listings_df['Accept Section 8'] == 'Yes') 
    ]

    printResults(filtered_df, 'Section 8')
elif filter_group == 'r':
    rr_min = input("Enter min rent: ")
    rr_max = input("Enter max rent: ")
    # TODO - handle invalid input
    min_rent = int(rr_min)
    max_rent = int(rr_max)

    print('RENT RANGE')
    rent_df = unit_groups_df.loc[
        (unit_groups_df['Listing Id'].isin(active_listing_ids))
    ]

    # ignore null fields
    rent_df = rent_df.dropna(subset=['Monthly Rent'])
    rentFilter(rent_df, min_rent, max_rent)
else:
    print("invalid filter group selected")
