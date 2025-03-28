# Beer Recipe Analysis
## Objective: 
### The goal of this capstone project is to determine the frequency of beer recipes, uploaded to 2 beer recipe websites by style. Style is based on the BJCP Style Guideline published in 2021. In addition to freqency this analysis will include a determination of the percent of the recipes, as entered, are within the tolerance of the beer style. 

## Overview:
### This project involves web scraping beer recipe data from two sources, Beersmith.com and BrewersFriend.com, to create a unified dataset of homebrew and craft beer recipes. The scraped data is merged and cross-referenced with the 2021 BJCP Style Guidelines, which define acceptable ranges for Original Gravity (OG), Final Gravity (FG), Alcohol by Volume (ABV), and International Bitterness Units (IBU) for various beer styles. The analysis focuses on determining the frequency of different beer styles within the dataset and evaluating how well individual recipes align with BJCP-defined style parameters. This project provides insights into homebrewers' adherence to style guidelines and potential trends in recipe formulation.
 ###   - BJCP.org - The Beer Judge Certification Program is a non-profit organization founded in 1985 that certifies and ranks beer judges worldwide. Its primary purpose is to promote knowledge, understanding, and appreciation of diverse beer, mead, and cider styles, while developing standardized evaluation methods for these beverages.
 ###   - Beersmith.com - Beersmith.com is a platform centered around home brewing software, offering tools and resources for creating and managing recipes for beer, mead, wine, and cider.
 ###   - Brewersfriend.com - Brewer's Friend is an online platform designed to assist homebrewers and professional brewers with recipe formulation, brewing calculations, and batch tracking.

## Tools & Libraries Summary  
This project was conducted using Jupyter Notebook within VSCode, running Python 3.13.2 in a virtual environment (venv). Assistance was provided through AI tools, including ChatGPT, Perplexity, and Cursor utilizing Claude-3.7.  

### Libraries Used  
- **Data Handling & Processing:** `pandas`, `numpy`  
- **Visualization:** `matplotlib.pyplot`, `matplotlib.colors`, `seaborn`, `WordCloud`  
- **Styling & Terminal Output:** `rich` (including `rich.console`, `rich.table`)  
- **Randomization:** `random`  

### Data Cleaning Process  
Cleaning included handling missing values (NaNs) appropriately, standardizing beer style names to match the 2021 BJCP Style Guidelines, and restructuring data by splitting multi-value columns into separate fields. This preprocessing ensured accurate comparisons of OG, FG, ABV, and IBU against BJCP-defined style ranges, improving the integrity of the analysis.


## Primary Files

1. [beersmith_recipes.csv](https://beersmithrecipes.com/recent/) - scraped data that contains certain fields of 100% of the all grain beer recipes that have been uploaded by users.

2. [bf_recipes.csv](https://www.brewersfriend.com/homebrew-recipes/all-grain/) - scraped data that contains select fields of 100% of the all-grain beer recipes that have been uploaded by users.

3. [styles_2021.json](https://github.com/ascholer/bjcp-styleview/blob/main/styles.json) - dataset that contains the criteria used to judge beer. Will help determine if recipes meet the criteria to be considered a specific style of beer. (This was acquired from ascholer on github)

4. Beer_recipe_scrape.ipynb - Notebook that contains the code to scrape the Beersmith.com website.

5. Brewersfriend.ipynb & scrape.py - notebook & python code to scrape the brewersfriend.com website. Technical issue with saving data required secondary file.

6. **Data_Dictionary.md:** is the custom data dictionary for this project. 

7. **README.md:** provides overview of the project, information on running the project, sources of information, and description of project features. 

8. **Beer_capstone.ipynb:** a Jupyter Notebook in which the steps for data cleaning, merging of data sets, calculation of new values, data visualization, and interpretation are located. 

9. **requirements.txt:** this is the file used for pip install of project requirements. 

## Data Dictionary
### Please see the Data_Dictionary.md file in this repo. 

## Running the Program:
### Check that your system meets the following requirements:
- Ensure you have Python installed. Python 3 is required. This project is written using version 3.11.9. You can download Python from https://www.python.org/downloads/.
- Ensure you have installed Git. This program is needed to clone the repository. You can download Git from https://git-scm.com/downloads.

### Follow these steps for running the project files locally:
1. Navigate in your browser to the repository at https://github.com/TinaBaldwin/US_Cities_Data.git
2. Open a terminal (command line) in your preferred software, i.e. Gitbash
3. In the terminal, navigate to the directory in which you want to clone the repository
4. In the browser, copy the URL for the repository
4. Enter into Gitbash: *git clone 'paste copied repository url'*
5. Navigate to the cloned folder from your terminal
6. In order to keep the project's dependencies isolated from your system's Python environment, create a virtual environment by entering the following into the terminal, based on your system; and install the required packages:
- On Windows: 
    1. if using command prompt:
        - enter *python -m venv venv* (creates new virtual environment named venv in your current directory)
        - to active virtual environment enter *.\venv\Scripts\activate* (your prompt should indicate you are now in venv)
    2. if using Git Bash:
        - enter *python -m venv venv* (creates new virtual environment named venv in your current directory)
        - then to activate enter *source venv/Scripts/activate* (your prompt should indicate you are now in venv)   
- On macOS and Linux: 
        - enter *python3 -m venv venv* (creates new virtual environment named venv in your current director)
        - to activate virtual environment enter *source venv/bin/activate* (your prompt should indicate you are now in venv)      
7. Once you are in the virtual environment, for all the above systems, enter into terminal *pip install -r requirements.txt*
8. Now you are ready to run the project!
    - If you have Jupyter Notebook installed, enter into terminal *jupyter notebook* and open the .ipynb file.
    - If you have Visual Studio Code (VS Code), you can open the .ipynb file in VS Code and run all the cells with the run all button at top of page or you can run each cell individually with the arrow/executve button on top left of each cell. 
    - You may get a pop up asking you to install the ipykernel package, if you do go ahead and install it. 
8. When you are finished running the project, you can deactivate the virtual environment, by entering into the terminal *deactivate*

### The following packages will be required to run the program:
- pandas
- matplotlib
- numpy
- ipykernel

## Sources:
### Datasets (There are two data sets used and both come from Kaggle (https://www.kaggle.com/). These data sets have been cleaned and merged into one.)
-  US Cities (https://www.kaggle.com/datasets/louise2001/us-cities): For cities within the United states, this data set includes city, state, population, cost of living, etc.  
- US Cities Urban Connectivty: EDA (https://www.kaggle.com/code/vellis1/us-cities-urban-connectivity-eda): Got cities within the United States, this data set includes city, state, Walk Score and numbers of amenities like tennis courts, walking trails, basketball hoops, public restrooms, etc.

## Features:
1. Loading Data - Read in two CSV data files.
2. Data preparation - In the first three sections of Cleaning_USCities_Connectivity.ipynb the data is cleaned, pandas merge completed, and new values are calculated based on the new data set.  
3. Visualization of data - The fourth section of Cleaning_USCities_Connectivity.ipynb uses Matplotlib to crease 3+ visualizations of data. 
4. Data Dictionary - Data_Dictionary.md is a custom built data dictionary document. 
5. Virtual Environment usage - Readme document includes instructions on how to setup a virtual environment. 
6. interpretation - The fifth section of Cleaning_USCities_Connectivity.ipynb contains the final analysis of the data and future recommendations.



## Directions for downloading and running the project:
1. clone the repository from GitHub - https://github.com/TinaBaldwin/US_Cities_Data.git
2. cd into the project directory
3. Create a virtual environment by using this in the project directory
   - python -m venv venv
4. Activate the virtual environment 
   - In windows - venv\Scripts\activate
   - On MacOS/Linux - source venv/bin/activate
   -In Git Bash - source venv/Scripts/activate
5. Note, the prompt should change and show the virtual envirnoment (venv)
6. Install the required dependencies
   - pip install -r requirements.txt




