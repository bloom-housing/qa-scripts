import pandas as pd


def vet_0_1_bed(l_df, u_df):
    l_df = l_df.loc[
        (l_df['Listing Status'] == 'Public') &
        (l_df['Community Types'].str.contains('Veterans')) 
    ]

    return u_df.loc[
        (u_df['Listing Id'].isin(l_df['Listing Id'])) &
        ((u_df['Unit Types'].str.contains('Studio')) |
        (u_df['Unit Types'].str.contains('One Bedroom')))
    ]


def vacant_disabilities(l_df, u_df):
    l_df = l_df.loc[
        (l_df['Listing Status'] == 'Public') &
        (l_df['Is Listing Verified'] == 'Yes') &
        (l_df['Property Amenities'].str.contains('wheelchairRamp')) &
        (l_df['Property Amenities'].str.contains('rollInShower')) &
        (l_df['Property Amenities'].str.contains('wideDoorways')) 
    ]

    return u_df.loc[
        (u_df['Listing Id'].isin(l_df['Listing Id'])) &
        (u_df['Unit Group Vacancies'] > 0) 
    ] 


def confirmed_2_3_bed(l_df, u_df):
    l_df = l_df.loc[
        (l_df['Listing Status'] == 'Public') &
        (l_df['Is Listing Verified'] == 'Yes') 
    ]

    return u_df.loc[
        (u_df['Listing Id'].isin(l_df['Listing Id'])) &
        ((u_df['Unit Types'].str.contains('Two Bedroom')) |
        (u_df['Unit Types'].str.contains('Three Bedroom'))) 
    ] 


def vacant_open_home_fam(l_df, u_df):
    l_df = l_df.loc[
        (l_df['Listing Status'] == 'Public') &
        ((l_df['Home Type'] == 'house') |
        (l_df['Home Type'] == 'townhome')) &
        (l_df['Community Types'].str.contains('Families')) 
    ]

    return u_df.loc[
        (u_df['Listing Id'].isin(l_df['Listing Id'])) &
        ((u_df['Unit Group Vacancies'] > 0) |
        (u_df['Waitlist Status'] == 'Yes'))
    ] 


def confirmed_sec8_sen62(l_df):
    return l_df.loc[
        (l_df['Listing Status'] == 'Public') &
        (l_df['Accept Section 8'] == 'Yes') &
        l_df['Community Types'].str.contains('Seniors 62+')
    ]

def accessibility(l_df):
    return l_df.loc[
        (l_df['Listing Status'] == 'Public') &
        (l_df['Property Amenities'].str.contains('wheelchairRamp')) &
        (l_df['Property Amenities'].str.contains('rollInShower')) &
        (l_df['Property Amenities'].str.contains('wideDoorways')) &
        (l_df['Property Amenities'].str.contains('elevator')) &
        (l_df['Property Amenities'].str.contains('serviceAnimalsAllowed')) &
        (l_df['Property Amenities'].str.contains('accessibleParking')) &
        (l_df['Property Amenities'].str.contains('parkingOnSite')) &
        (l_df['Property Amenities'].str.contains('laundryInBuilding')) &
        (l_df['Property Amenities'].str.contains('barrierFreeEntrance')) &
        (l_df['Property Amenities'].str.contains('grabBars')) &
        (l_df['Property Amenities'].str.contains('heatingInUnit')) &
        (l_df['Property Amenities'].str.contains('acInUnit')) &
        (l_df['Property Amenities'].str.contains('hearing')) &
        (l_df['Property Amenities'].str.contains('visual')) &
        (l_df['Property Amenities'].str.contains('mobility')) &
        (l_df['Property Amenities'].str.contains('loweredLightSwitch')) &
        (l_df['Property Amenities'].str.contains('barrierFreeBathroom')) &
        (l_df['Property Amenities'].str.contains('loweredCabinets')) 
    ]

def combo_select(l_df, u_df):
    l_df = l_df.loc[
        (l_df['Listing Status'] == 'Public') &
        (l_df['Is Listing Verified'] == 'Yes') & 
        (l_df['Home Type'] == 'apartment') & 
        (l_df['Building Region'] == 'Greater_Downtown') &
        (l_df['Property Amenities'].str.contains('acInUnit')) &
        (l_df['Community Types'].str.contains('Seniors 55+'))
    ]

    return u_df.loc[
        (u_df['Listing Id'].isin(l_df['Listing Id'])) &
        (u_df['Unit Types'].str.contains('Studio'))
    ] 

