# Listings Filter Check

## Summary

A script to facilitate manually verifying the rental finder and listings filter work as expected. This script was created with the Detroit replatform effort in mind but may be useful for any jurisdiction with the feature flag enabled.

## Scope

This script will match several predefined filters based on the listings csv export found in the partner portal. It is intended to make UI testing against existing data easier by removing the necessity to manually parse through the 2 csv files.

### Out of Scope

Please note the following is out of scope

- Automated comparison between csv files and UI filter
- Verification that csv data is correct
- Automatic downloading the most up to date csv file

## Setup

This script is only guaranteed to work as expected with python 3.13.X.

In you terminal install the dependencies with `pip install -r requirements.txt`

You will need a partner portal admin user to download the csv files

## How to Run

1. From the partner portal export the most recent listings csv. This will download 2 csv files, one for listings and one for unitGroups.
2. In terminal enter `python listings.py <PATH_TO_LISTINGS.CSV> <PATH_TO_UNITGROUPS.CSV>
3. You will be given the option to choose a preset filter or an interactive single filter option. Choose which is applicable to your use case and set the corresponding filter from either the rental finder or listings filter on the public site.
4. Verify the listing totals and the listing names match your terminal output and the public site UI.

## Adding More Filters

Predefined filters are set in the `preset_filters.py` file. If you wish to define more preset filters please check the [filter_to_csv_map](filter_to_csv_map.md) documentation to see which csv headings match up to which UI filters.
