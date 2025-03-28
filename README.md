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

To run this project, follow these steps:

1. Clone the repository: `git clone https://github.com/Redsoxin7/beer_recipes.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Run or Explore the notebook: `Beer_capstone.ipynb`




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

## Features:
1. Acquiring data by scraping data from 2 different websites.
2. Acquiring data by copying a json file from a github repository.
3. Loading Data - Read in two CSV data files and json file.
2. Data preparation - Split columns into additional columns. 








