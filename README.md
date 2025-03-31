# Beer Recipe Analysis
## Objective: 
### The goal of this capstone project is to determine the frequency of beer recipes, uploaded to 2 beer recipe websites by style. Style is based on the Beer Judge Certification Program(BJCP) Style Guideline published in 2021. In addition to frequency this analysis will include a determination of the percent of the recipes, as entered, are within the tolerance of the beer style as established by BJCP.

## Overview:
### This project involves web scraping beer recipe data from two sources, BeerSmith.com and BrewersFriend.com, to create a unified dataset of homebrew and craft beer recipes. The scraped data is merged and cross-referenced with the 2021 BJCP Style Guidelines, which define acceptable ranges for Original Gravity (OG), Final Gravity (FG), Alcohol by Volume (ABV), and International Bitterness Units (IBU) for various beer styles. The analysis focuses on determining the frequency of different beer styles within the dataset and evaluating how well individual recipes align with BJCP-defined style parameters. This project provides insights into homebrewers' adherence to style guidelines and potential trends in recipe formulation.
 ###   - BJCP.org - The Beer Judge Certification Program is a non-profit organization founded in 1985 that certifies and ranks beer judges worldwide. Its primary purpose is to promote knowledge, understanding, and appreciation of diverse beer, mead, and cider styles, while developing standardized evaluation methods for these beverages.
 ###   - Beersmith.com - Beersmith.com is a platform centered around home brewing software, offering tools and resources for creating and managing recipes for beer, mead, wine, and cider.
 ###   - Brewersfriend.com - Brewer's Friend is an online platform designed to assist homebrewers and professional brewers with recipe formulation, brewing calculations, and batch tracking.

## Tools & Libraries Summary  
This project was created using Jupyter Notebook within VSCode, running Python 3.13.2 in a virtual environment (venv). Assistance was provided through AI tools, including ChatGPT, Perplexity, and Cursor. AI was the primary tool used to create the 2 web scrapers. (Since learning to scrape was new to me and I had no exposue to it, I used AI to get me started. Neither scraper worked without interaction and input.)

### Libraries Used  
- **Data Handling & Processing:** `pandas`, `numpy`, `typing`, `re`, `inspect`
- **Visualization:** `matplotlib`, `seaborn`, `WordCloud`, `rich`
- **Utility:** `time`
- **Web Scraping** `Selenium`, `bs4(BeautifulSoup)`

### Data Cleaning Process  
Cleaning included handling missing values (NaNs) appropriately, standardizing beer style names to match the 2021 BJCP Style Guidelines, and restructuring data by splitting multi-value columns into separate fields. This preprocessing ensured accurate comparisons of OG, FG, ABV, and IBU against BJCP-defined style ranges, improving the integrity of the analysis.


## Primary Files

1. [Input_Files/beersmith_recipes.csv](https://beersmithrecipes.com/recent/) - scraped data that contains certain fields of 100% of the all grain beer recipes that have been uploaded by users.

2. [Input_Files/bf_recipes.csv](https://www.brewersfriend.com/homebrew-recipes/all-grain/) - scraped data that contains select fields of 100% of the all-grain beer recipes that have been uploaded by users.

3. [Input_Files/styles_2021.json](https://github.com/ascholer/bjcp-styleview/blob/main/styles.json) - dataset that contains the criteria used to judge beer. Will help determine if recipes meet the criteria to be considered a specific style of beer. (This was acquired from ascholer on github)

4. [Scrape_Files/Beer_recipe_scrape.ipynb] - Notebook that contains the code to scrape the Beersmith.com website. This scraper was set up to use chrome.

5.[Scrape_Files/scrape.py] - python code to scrape the brewersfriend.com website. This scraper uses BeautifulSoup and is not set up for a specific browser. To run from terminal: make sure you access the relative path. If in the Scrape_Files directory enter: python3 scrape.py. To interrupt the program before completion hit: CTRL + C. 

6. **Data_Dictionary.md:** is the custom data dictionary for this project. 

7. **README.md:** provides overview of the project, information on running the project, sources of information, and description of project features. 

8. **Beer_capstone.ipynb:** a Jupyter Notebook in which the steps for data cleaning, merging of data sets, calculation of new values, data visualization, and interpretation are located. **(This is the Primary Notebook)**

9. **requirements.txt:** this is the file used for pip install of project requirements. 

## Data Dictionary
### Please see the Data_Dictionary.md file in this repo. 

## Running the Program:

To run this project, follow these steps:

1. Clone the repository: `git clone https://github.com/Redsoxin7/beer_recipes.git`
2. Install the virtual Environment. (See instructions below)
3. Install the necessary dependencies: `pip install -r requirements.txt`
4. Run or Explore the primary notebook: `Beer_capstone.ipynb`
5. Run or Explore the scraping notebook: `Scrape_Files/Beer_recipe_scrape.ipynb`
6. Run or Explore the scraping program: `Scrape_Files/scrape.py`
7. When you are finished running the project, you can deactivate the virtual environment, by entering into the terminal *deactivate*

##### Virtual Environment Commands

| Command | Linux/Mac | GitBash |
| ------- | --------- | ------- |
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |

### Helpful steps to run the project files locally:
1. Navigate in your browser to the repository at `https://github.com/Redsoxin7/beer_recipes.git`
2. Open a terminal (command line) in your preferred software, i.e. Gitbash, terminal
3. In the terminal, navigate to the directory in which you want to clone the repository
4. In the browser, copy the URL for the repository
4. Enter into Gitbash: *`https://github.com/Redsoxin7/beer_recipes.git`*
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
    - If you have Visual Studio Code (VS Code), you can open the .ipynb file in VS Code and run all the cells with the run all button at top of page or you can run each cell individually with the arrow/execute button on top left of each cell. (Cells down stream are dependant on cells above them, so run them in order)
    - You may get a pop up asking you to install the ipykernel package, if you do go ahead and install it. 
8. When you are finished running the project, you can deactivate the virtual environment, by entering into the terminal *deactivate*

### The following packages will be required to run the program:
- pandas
- matplotlib
- numpy
- ipykernel
- typing
- re
- inspect`
- matplotlib
- seaborn
- WordCloud
- rich
- time`
- Selenium
- bs4(BeautifulSoup)`

### Feature Requirements met
Feature Selection:  
**Loading data.** 

| FEATURE  | DIFFICULTY  | COMPLETED |
| :---- | :---- | :---- |
| Scrape TWO pieces of data from anywhere on the internet and utilize it in your project.  | Intermediate  | Scraped 2 pieces of data: 1 from BeerSmith.com & 1 from Brewersfriend.com. Also downloaded style\_2021.json from a git repository. |
| Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.   | Intermediate   | Utilized both pandas merge and concat to combine data, calculated values to address missing data, and extracted data to create new columns. |
| Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data. | Easy  | Made 6 visualizations to display the data using both matplotlib and seaborn. Made 1 table with rich. |
| Utilize a virtual environment and include instructions in your README on how the user should set one up | Intermediate  | Utilized a virtual environment with instructions on how to set up in the readme and in the capstone project. |
| Build a custom data dictionary and include it either in your README or as a separate document. This will only apply if your data set does not already have a data dictionary or if you’re building a custom data set. For an example, see the resources to the right. | Easy  | Created a data dictionary for the combined recipe dataset and also for BJCP style guidelines. |
| Annotate your code with markdown cells in Jupyter Notebook, write clear code comments, and have a well-written README.md. Tidy up your notebook, and make sure you don’t have any empty cells or incomplete cells that don’t do anything. Make sure it’s all functional before your final github commit. | Intermediate  | Used comments within the code and markdown to help navigate the notebook.  |


## Some Advanced Features of the project (As captured by Gemini-2.5-pro-exp-03-25)

Okay, looking at the overall structure and techniques used in your notebook, here are some features that stand out as being beyond the absolute basics of data loading, cleaning, and plotting:

1.  **Complex Data Standardization via External Lookup:**
    *   The use of the `update_style_data` function, which reads an external Excel file (`BJCP_Updated.xlsx`) and uses `pd.merge` and `combine_first` to systematically correct and standardize a large number of inconsistent 'Style' and 'Style Number' entries based on a manually curated mapping. This goes far beyond simple renaming or mapping internal values.

2.  **Domain-Specific Calculations:**
    *   Implementing and applying specific brewing formulas like the **Balling formula** to calculate Final Gravity (`calculate_final_gravity`) and the formula to estimate Plato from OG (`clean_recipe_data` using `eval`). This demonstrates applying external domain knowledge within the code.

3.  **Advanced String Parsing with Regex:**
    *   The `parse_columns` function uses regular expressions (`re`) within helper functions (`extract_values`, `extract_float`) applied row-wise (`df.apply`) to parse complex, combined strings ('Stats', 'Beer Style') into multiple distinct numerical and categorical columns.

4.  **Dynamic Null Value Replacement using `inspect`:**
    *   The `replace_column_nulls` function uses the `inspect` module to dynamically determine the variable name of the DataFrame passed into it. This allows it to create unique placeholder names (e.g., "BS No Name 1", "BF No Name 1") based on the source DataFrame, which is a non-standard and more intricate approach to handling missing categorical data compared to simple imputation.

5.  **Sophisticated Compliance Analysis Logic:**
    *   The `create_and_display_compliance_summary` function involves complex logic:
        *   Filtering guidelines and recipes based on valid styles.
        *   Iterating through recipes and performing multiple conditional checks against style guideline ranges (OG, FG, ABV, IBU).
        *   Aggregating these boolean results into multiple summary statistics per style (e.g., % meeting 4/4, % meeting >=3/4, % OG compliant).
        *   Building a summary DataFrame iteratively.

6.  **Integration with `rich` for Enhanced Table Output:**
    *   Utilizing the `rich` library (`Console`, `Table`) within the `create_and_display_compliance_summary` function to generate a well-formatted, styled table directly in the notebook's output. This provides a much more polished presentation than standard `print` or `display(df)`.

7.  **Advanced Visualization Customization:**
    *   While using libraries like Matplotlib/Seaborn is standard, the level of customization in some plots, particularly Visualization 5 (`plot_category_style_distribution`), goes further:
        *   Generating random colors and custom colormaps.
        *   Adding text annotations directly onto the plot (`ax.text`) based on calculated values (unique style counts).
        *   Extensive legend customization (sorting alphabetically, repositioning, multiple columns, adjusting spacing).

These features showcase more advanced Pandas operations, application of domain knowledge, complex data transformation logic, integration with external files and libraries (`inspect`, `rich`), and detailed visualization control.

## Future Developments
- Create a Tableau dashboard 
    - To further analyze the categories and styles.
    - Determine if there are statistical differences between the recipes from BeerSmith and Brewers Friend.
- Create additional visualizations to explore the distribution of styles that adhered to the style guidelines.
- Learn more about Python so I can utilize advanced functions to make my code more productive and reusable.

## Learnings
- Spent too much time on the cleaning and homogenizing of the data. Didn't leave enough time to explore the data with additional tools like Tableau.

- Should have spent more time on the planning of the project. I went in too many directions when preparing the data for evaluation.

- Having seen some of my classmates projects...I need to use a better system of keeping my layout organized. With better outlining and header management it would have made the flow of the code better and would have allowed me to be more productive.










