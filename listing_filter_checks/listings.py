import pandas as pd
import re
import argparse
import preset_filters as presets

parser = argparse.ArgumentParser()
parser.add_argument("listings_csv_path", help="file path of the listings csv export")
parser.add_argument("units_csv_path", help="file path of the units csv export")
args = parser.parse_args()

listings_df = pd.read_csv(args.listings_csv_path)
unit_groups_df = pd.read_csv(args.units_csv_path)

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


active_listings_df = listings_df.loc[
    (listings_df['Listing Status'] == 'Public') 
]
active_listing_ids = active_listings_df['Listing Id'].tolist()

def unit_filter(unit_type):
    return unit_groups_df.loc[
        (unit_groups_df['Listing Id'].isin(active_listing_ids)) &
        (unit_groups_df['Unit Types'].str.contains(unit_type)) 
    ]

def community_filter(com_type):
    return listings_df.loc[
        (listings_df['Listing Status'] == 'Public') &
        (listings_df['Community Types'].str.contains(com_type)) 
    ]

def sec8():
    return listings_df.loc[
        (listings_df['Listing Status'] == 'Public') &
        (listings_df['Accept Section 8'] == 'Yes') 
    ]

filter_group_map = {
    '0': 'Community Types',
    '1': 'Unit Types',
    '2': 'Accept Section 8',
    '3': 'Monthly Rent'
}
community_type_map = {
    '0': 'Residents with Disabilities',
    '1': 'Veterans',
    '2': 'Seniors 62+',
    '3': 'Supportive Housing for the Homeless',
    '4': 'Families',
    '5': 'Seniors 55+'
}

bed_size_map = {
    '0': 'Studio',
    '1': 'One Bedroom',
    '2': 'Two Bedroom',
    '3': 'Three Bedroom',
    '4': 'Four'
}

def build_filter():
    if filter_group == '0':
        com_select = input("Enter a community type:\n0 = disabilities\n1 = veterans\n2 = seniors 62+\n3 = homeless\n4 = families\n5 = seniors 55+\nq = quit\n")
        com_type = community_type_map[com_select]
        # TODO handle invalid input
        printResults(community_filter(com_type), com_type)
    elif filter_group == '1':
        bed_size_select = input("Enter bedroom size:\n0 = studio\n1 = 1 bedroom\n2 = 2 bedroom\n3 = 3 bedroom\n4 = 4+ bedroom\nq = quit\n")
        bed_size = bed_size_map[bed_size_select]
        # TODO - handle invalid bed size
        printResults(unit_filter(bed_size), bed_size)
    elif filter_group == '2':
        printResults(sec8(), 'Section 8')
    elif filter_group == '3':
        rr_min = input("Enter min rent: ")
        rr_max = input("Enter max rent: ")
        # TODO - handle invalid input
        min_rent = int(rr_min)
        max_rent = int(rr_max)

        rent_df = unit_groups_df.loc[
            (unit_groups_df['Listing Id'].isin(active_listing_ids))
        ]

        # ignore null fields
        rent_df = rent_df.dropna(subset=['Monthly Rent'])
        rentFilter(rent_df, min_rent, max_rent)
    else:
        print("invalid filter group selected")


filter_mode = input("Enter 0 for preset filters or 1 for interactive filters\n\nEnter: ")
if filter_mode == '0':
    preset_select = input('''
    Select from the following preset filters:
    0: Studio or 1 bedroom for veterans
    1: Verified listings with vacancies for residents with disabilities that contain wheelchair ramp, roll in showers, or wide doorways
    2: Verified listings with 2 or 3 bedrooms
    3: Single family home or townhouse with open waitlist or vacancies for families
    4: Listings that accept section 8 for seniors 62+
    5: Verified studio apartment listings in greater downtown with ac in unit for seniors 55+
    
    Enter: ''')

    if preset_select == '0':
        printResults(presets.vet_0_1_bed(listings_df, unit_groups_df))
    elif preset_select == '1':
        printResults(presets.vacant_disabilities(listings_df, unit_groups_df))
    elif preset_select == '2':
        printResults(presets.confirmed_2_3_bed(listings_df, unit_groups_df))
    elif preset_select == '3':
        printResults(presets.vacant_open_home_fam(listings_df, unit_groups_df))
    elif preset_select == '4':
        printResults(presets.confirmed_sec8_sen62(listings_df))
    elif preset_select == '5':
        printResults(presets.combo_select(listings_df, unit_groups_df))
    else:
        print("Invalid selection")
else:
    print("Starting interactive mode")
    filter_group = input("\nEnter group to filter by:\n0 = community type\n1 = unit type\n2 = section 8\n3 = rent range\nq = quit\n\nEnter: ")

    while filter_group != 'q':
        
        build_filter()
        filter_group = input("\nEnter group to filter by:\n0 = community type\n1 = unit type\n2 = section 8\n3 = rent range\nq = quit\n\nEnter: ")
