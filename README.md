# Billing Statistics
## Introduction
This repository aims to build a framework that takes in billing data from various different Cloud services e.g. AWS/GCP/Azure to output the median, average and call out unexpected spikes in billing due to improper tool usage.

## Design
This repository implements SOLID design so that different platform implementations can be injected in without a large refactor in code.