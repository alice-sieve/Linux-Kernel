# Linux Patch Scraper

This project scrapes those messages which contains the PATCH keyword from https://www.spinics.net/lists/ for all of the topics as present on the website, there are over 430 topics.  

## Directory Structure

.
├── README.md
├── spinics-linux-fedora [1]
│   ├── create_patch_files.py
│   └── topics
│       ├── spinics-linux-fedora
│       └── spinics-linux-fedora.sh
└── spinics-lists [2]
    ├── create_patch_files.py
    └── topics
        ├── spinics-lists
        └── spinics-lists.sh



### Usage & Flow

for [1]

- execute /topics/spinics-lists.sh using `bash`.
- this will scrape all the links which contains `PATCH` keyword & write them in topic wise txt files.
- now use `python3 create_patch_files.py` this will write HTML files which contains PATCHES in respective directory for each topic.

### Prerequisites

What things you need to install the software and how to install them

- Python Libraries

```
glob 
os
fileinput
re
shutil
```

- Bash


## Authors

* **Mayank Singh** - [code-monk08](https://github.com/code-monk08)