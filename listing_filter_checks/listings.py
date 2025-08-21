import pandas as pd
import re
import argparse
import preset_filters as presets
import pdb

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
def rentFilter(df, d_min=None, d_max=None):
    listings = []

    # Monthly Rent column may contain any of the following:
    #  1. single flat rent preceded by $
    #  2. range of flat rent values separated by -
    #  3. single percentage value followed by % 
    #  4. range of percentage values separated by -
    #  5. flat rent value(s) and percentage value separated by , 
    
    for i, row in df.iterrows():
        # Ignore duplicates
        if row['Listing Name'] not in listings:
            rent_string = row['Monthly Rent']
            # Always include percentage of income listings in rent range results
            if '%' in rent_string:
                listings.append(row['Listing Name'])
            else:
                # Extract all number values from Monthly Rent column
                numbers_as_strings = re.findall(r'\d+', rent_string)

                # For units with a range of flat rent values
                if '-' in rent_string:
                    a_min = int(numbers_as_strings[0])
                    a_max = int(numbers_as_strings[1])
                    if (a_max >= d_min and a_min <= d_max):
                        listings.append(row['Listing Name'])
                # For units with a single flat rent value
                else:
                    for n in numbers_as_strings:
                        if d_min <= int(n) and d_max >= int(n):
                            listings.append(row['Listing Name'])

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
        com_type = community_type_map.get(com_select, None)
        if com_type:
            printResults(community_filter.get(com_type), com_type)
        elif com_select != 'q':
            print("Invalid selection")
    elif filter_group == '1':
        bed_size_select = input("Enter bedroom size:\n0 = studio\n1 = 1 bedroom\n2 = 2 bedroom\n3 = 3 bedroom\n4 = 4+ bedroom\nq = quit\n")
        bed_size = bed_size_map.get(bed_size_select, None)
        if bed_size:
            printResults(unit_filter(bed_size), bed_size)
        elif bed_size_select != 'q':
            print("Invalid selection")
    elif filter_group == '2':
        printResults(sec8(), 'Section 8')
    elif filter_group == '3':
        rent_df = unit_groups_df.loc[
            (unit_groups_df['Listing Id'].isin(active_listing_ids))
        ]

        # Ignore null fields, listings without rent specified will not return in rent range filter
        rent_df = rent_df.dropna(subset=['Monthly Rent'])

        rr_min = input("Enter min rent: ")
        rr_max = input("Enter max rent: ")
        try:
            desired_min = int(rr_min)
            desired_max = int(rr_max)
            rentFilter(rent_df, desired_min, desired_max)
        except:
            print("Rent must be a number")     
    else:
        print("Invalid selection")


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
