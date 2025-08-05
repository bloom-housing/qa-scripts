# UI filter to csv mapping

## Group 1 - Confirmed listings

csv header = 'Is Listing Verified'

### Filter options:

- 'Yes'
- 'No'

## Group 2 - Availability

csv header = combination of 'Marketing Status' and 'Waitlist Status' (calculated per unit group).

### Filter options:

- 'Waitlist Status' = 'Yes' -> Open Waitlist
- 'Waitlist Status' = 'No' -> Closed Waitlist
- 'Marketing Status' = 'Under Construction' -> Coming soon.

**Note -> The "Units Available" filter option does not work see https://app.zenhub.com/workspaces/bloom-5dc32d7144bd400001315dac/issues/gh/bloom-housing/bloom/4919**

**Note!**
In UI filter "Under Construction" will take priority. So if a unit has a closed waitlist and it is under construction it will not return on a closed waitlist filter. For script results to match UI filter results when searching for a waitlist you must explicitly include `df['Marketing Status'] != 'Under Construction'` in the search.

## Group 3 - Home type

csv header = 'Home Type'

### Filter options:

- 'apartment'
- 'duplex'
- 'house'
- 'townhome'

## Group 4 - Bedroom size

csv header = 'Unit Types'

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

**Rent Range filter currently has a bug. See https://app.zenhub.com/workspaces/bloom-5dc32d7144bd400001315dac/issues/gh/bloom-housing/bloom/5204**

### Filter options:

rent range - tbd how to filter this - possible column = 'Monthly Rent'

**csv header 2 = 'Accept Section 8'**

### Filter options:

- 'Yes'

## Group 6 - Region

csv header = 'Building Region'

### Filter options:

- 'Eastside'
- 'Greater_Downtown'
- 'Westside'
- 'Southwest'

## Group 7 - Accessibility Features

csv header = 'Property Amenities'

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

csv header = 'Listing Name'

- will do partial match against all listing names

## Group 9 - Community

csv header = 'Community Types'

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
