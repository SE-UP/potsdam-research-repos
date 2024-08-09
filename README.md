
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12607763.svg)](https://doi.org/10.5281/zenodo.12607763)
![Data license](https://i.creativecommons.org/l/by/4.0/88x31.png)
![Code License](https://img.shields.io/badge/License-MIT-black?style=flat-square&logo=none&labelColor=white&color=black)


## Introduction

This repository contains the data and findings for paper - 



## Contents

1. `data/`: This directory contains the raw data collected from the research repositories.
The [all_research_repos.csv](data/all_research_repos.csv) file specifically contains data used in this analysis, which is limited to ***research*** repositories. 
(Note: The files [all_org_repos.csv](data/all_org_repos.csv.csv) and [all_user_repos.csv](data/all_user_repos.csv) include repositories labeled as research/non_research)
2. `analysis/`: This folder contains plot_analysis.ipynb file with graphs/plots used in paper. 
The analysis and result graphs can be found in the [plot_analysis.ipynb](analysis/plot_analysis.ipynb) Jupyter notebook.
3. `scripts/`: This directory contains the code code used for plotting graphs in jupyternotebook. 


## Methodology

 [SWORDS-template-UP v1.0.0](https://github.com/Software-Engineering-Group-UP/SWORDS-template-UP) have been used for gathering GitHub profiles, repositories and additional software developement variables. This is an exteded version of [SWORDS-template](https://github.com/UtrechtUniversity/SWORDS-template) 

## Data Collection

To collect the necessary data for our analysis, follow these steps:

1. Collect GitHub profiles of users and organizations by using the [SWORDS-template-UP collect_users](https://github.com/Software-Engineering-Group-UP/SWORDS-template-UP/tree/main/collect_users) script.
2. Collect repositories of GitHub profiles using the [SWORDS-template-UP collect_repositories](https://github.com/Software-Engineering-Group-UP/SWORDS-template-UP/tree/main/collect_repositories) script.
3. Collect additional variables by running specific scripts, such as:
    - [Presence of folder named test](https://github.com/Software-Engineering-Group-UP/SWORDS-template-UP/blob/main/collect_variables/scripts/soft_dev_pract/test_folder.py)
    - [Comment at the start of program/scripts](https://github.com/Software-Engineering-Group-UP/SWORDS-template-UP/tree/main/collect_variables/scripts/soft_dev_pract)
    - [Check which continuous integration technique is used](https://github.com/Software-Engineering-Group-UP/SWORDS-template-UP/blob/main/collect_variables/scripts/soft_dev_pract/continious_integration.py)
    - [Checking if additional linting/testing rules are defined](https://github.com/Software-Engineering-Group-UP/SWORDS-template-UP/blob/main/collect_variables/scripts/soft_dev_pract/add_ci_rules.py)
    - [Finding out howfair variables](https://github.com/Software-Engineering-Group-UP/SWORDS-template-UP/tree/main/collect_variables/scripts/howfairis_api)


## Usage

To reproduce our analysis, follow these steps:

1. Clone this repository.
2. Navigate to the `analysis/` directory.
3. Run the analysis script.

## License 
- **Code**: The code in this repository is licensed under the MIT License. See the [LICENSE](./LICENSE.txt) file in the root directory for details.
- **Data**: The data in this repository is licensed under the [Creative Commons Attribution 4.0 International License](./data/LICENSE_data.txt).


## Citation 
Please cite it as described in the [CITATION.cff](CITATION.cff) file.
