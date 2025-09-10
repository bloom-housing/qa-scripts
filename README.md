# QA Scripts

A place for adhoc scripts and tools that can help support quality efforts. Examples of the sorts of scripts this repo can contain

- tools which can speed up daily development
- scripts to assist testing efforts
- proof of concepts's to try out automation ideas before incorporating them into existing pipelines
-

## Setup

The `.githooks` directory contains a pre-commit script to check for secrets before allowing a `git commit`. To enable this for your local clone please perform the following steps:

1. Install gitleaks. On mac you can run `brew install gitleaks`. For other install options see the [gitleaks docs](https://github.com/gitleaks/gitleaks?tab=readme-ov-file#installing)
2. `cd` into your local clone of the qa-scripts repo and run `git config core.hooksPath .githooks/`

## Who can Contribute

Anyone who has a tool or script they created and thinks others can benefit from. Scripts do not have to be specifically Bloom related but should somehow assist in the development or testing of Bloom related things.

## Contribution Guidelines

- Each script or tool will be organized into its own subfolder
- Each contribution will include a README located in that script's subfolder describing what it does and how to use it
- Reviews are encouraged but not required. Add a 'ready for review' tag and allow time for folks to review if they are interested.
- Each contribution should add the name with a link to the correct folder, and a brief description to the [Existing Scripts](#existing-scripts) section of this projects README
- Do not commit any secrets, passwords, keys or other sensitive information

## Maintenance

- If anyone comes across a script/tool that does not work they are encouraged to write up an issue to raise awareness of the problem
- Any tool/script that no longer functions should either be removed or updated with a fix

## Existing Scripts

| Name                                              | Description                                                                                                  |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [listing_filter_checks](./listing_filter_checks/) | Parses listings and unitGroups csv files to help with manually testing the listings filter and rental finder |
