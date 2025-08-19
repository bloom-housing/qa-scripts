# UI filter to csv mapping

The following maps the filter options available on the listings filter to the corresponding csv headers. It will also indicate which csv file the information is located in, listings.csv or unitGroups.csv.

## Group 1 - Confirmed listings

csv header: 'Is Listing Verified'  
csv file: listings

### Filter options:

- 'Yes'
- 'No'

## Group 2 - Availability

Availability is a combination of multiple csv headers across both csv files.

csv headers:  
header: 'Marketing Status'  
csv file: listings

header: 'Waitlist Status'  
csv file: unitGroups

header: 'Unit Group Vacancies'  
csv file: unitGroups

### Filter options:

- 'Waitlist Status' = 'Yes' -> Open Waitlist
- 'Waitlist Status' = 'No' -> Closed Waitlist
- 'Marketing Status' = 'Under Construction' -> Coming soon.
- 'Unit Group Vacancies' > 0 -> Available Units

**Note!**
In UI filter "Under Construction" will take priority. So if a unit has a closed waitlist and it is under construction it will not return on a closed waitlist filter. For script results to match UI filter results when searching for a waitlist you must explicitly include `df['Marketing Status'] != 'Under Construction'` in the search.

Unlike the behavior mentioned above for waitlist, vacant units that are under construction will return with the vacant unit filter.

## Group 3 - Home type

csv header: 'Home Type'  
csv file: listings

### Filter options:

- 'apartment'
- 'duplex'
- 'house'
- 'townhome'

## Group 4 - Bedroom size

csv header: 'Unit Types'  
csv file: unitGroups

### Filter options:

- 'Studio' -> Studio will work for either Studio or SRO checkbox
- 'One Bedroom'
- 'Two Bedroom'
- 'Three Bedroom'
- 'Four+ Bedroom'

## Group 5 - Rent

Current filter behavior for rent range:

- % of income, it will always return regardless of what rent range is being filtered on
- if rent is not set (n/a) is will never return regardless of what rent range is being filtered on

**csv header 1 = 'Monthly Rent'**

**NOTE -** A [preexisting bug](https://app.zenhub.com/workspaces/bloom-5dc32d7144bd400001315dac/issues/gh/bloom-housing/bloom/5204) resulted in some listings being saved incorrectly so that they return outside of the expected rent range. This issue is now fixed but the rent range search may be off by up to 5 listings.

### Filter options:

rent range - tbd how to filter this - column = 'Monthly Rent'

**csv header 2: 'Accept Section 8'**  
csv file 2: listings

### Filter options:

- 'Yes'

## Group 6 - Region

csv header: 'Building Region'  
csv file: listing

### Filter options:

- 'Eastside'
- 'Greater_Downtown'
- 'Westside'
- 'Southwest'

## Group 7 - Accessibility Features

csv header: 'Property Amenities'  
csv file: listing

### Filter options:

- 'elevator'
- 'wheelchairRamp'
- 'serviceAnimalsAllowed'
- 'accessibleParking'
- 'parkingOnSite'
- 'inUnitWasherDryer'
- 'laundryInBuilding'
- 'barrierFreeEntrance' -> "Barrier-free (no-step) property entrance"
- 'rollInShower'
- 'grabBars'
- 'heatingInUnit'
- 'acInUnit'
- 'hearing'
- 'visual' -> "units for those with visual disability"
- 'mobility' -> "units for those with mobility disabilities"
- 'barrierFreeUnitEntrance'
- 'loweredLightSwitch'
- 'barrierFreeBathroom'
- 'wideDoorways'
- 'loweredCabinets'

## Group 8 - Listing name

csv header: 'Listing Name'  
csv file: listing

- will do partial match against all listing names

## Group 9 - Community

csv header: 'Community Types'  
csv file: listing

### Filter options:

- 'Residents with Disabilities'
- 'Families'
- 'Supportive Housing for the Homeless'
- 'Seniors 55+'
- 'Seniors 62+'
- 'Veterans'

## Combining Filter Groups

There are some filters in the UI that don't return the exact search.

For example: selecting the studio checkbox for Group 4 - Bedroom size and "Closed waitlist" for Group 2 - Availability can return results where the listing has a studio apartment with an open waitlist and a 1 bedroom with a closed waitlist. This listing technically has a studio apartment **and** a closed waitlist but it does not have a studio apartment **with** a closed waitlist. To mimic this behavior in this script it can be performed as 2 separate queries. The first finding "studio" and the second looking for "closed waitlist" where the listing name matches the results returned from the first query.
