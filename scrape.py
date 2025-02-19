import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import sqlite3
import openpyxl
import json
import random

def scrape_recipes(page=1):
    url = f"https://www.brewersfriend.com/homebrew-recipes/all-grain/page/{page}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    recipes = []
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        
        if table:
            rows = table.find_all('tr')
            
            for row in rows:
                cols = row.find_all('td')
                # Check if this is a recipe row by verifying:
                # 1. It has enough columns
                # 2. The Style column (cols[1]) doesn't start with "Author:"
                # 3. The row has a link in the first column
                if (len(cols) >= 8 and 
                    not cols[1].get_text(strip=True).startswith('Author:') and 
                    cols[0].find('a')):
                    
                    recipe = {
                        'Title': cols[0].find('a').get_text(strip=True),
                        'Style': cols[1].get_text(strip=True),
                        'Size': cols[2].get_text(strip=True),
                        'OG': cols[3].get_text(strip=True),
                        'FG': cols[4].get_text(strip=True),
                        'ABV': cols[5].get_text(strip=True),
                        'IBU': cols[6].get_text(strip=True),
                        'Color': cols[7].get_text(strip=True)
                    }
                    recipes.append(recipe)
        
        return recipes
    
    except requests.RequestException as e:
        print(f"Error scraping page {page}: {e}")
        return []

def main():
    all_recipes = []
    start_page = 1
    
    # Try to load existing progress
    try:
        with open('scraping_progress.json', 'r') as f:
            progress = json.load(f)
            all_recipes = progress['recipes']
            start_page = progress['last_page'] + 1
            print(f"Resuming from page {start_page}")
    except FileNotFoundError:
        print("Starting new scraping session")
    
    try:
        # Scrape pages
        for page in range(start_page, 10790):
            print(f"Scraping page {page}...")
            recipes = scrape_recipes(page)
            all_recipes.extend(recipes)
            
            # Save progress every 10 pages
            if page % 10 == 0:
                progress = {
                    'last_page': page,
                    'recipes': all_recipes
                }
                with open('scraping_progress.json', 'w') as f:
                    json.dump(progress, f)
                print(f"Progress saved at page {page}")
            
            # Add a delay between requests (2-4 seconds)
            time.sleep(random.uniform(2, 4))
        
        # Convert final results to DataFrame
        df = pd.DataFrame(all_recipes)
        
        # Save in multiple formats with error handling
        try:
            df.to_csv('beer_recipes.csv', index=False)
            print(f"Saved {len(all_recipes)} recipes to beer_recipes.csv")

            # df.to_excel('beer_recipes.xlsx', index=False)
            print(f"Saved {len(all_recipes)} recipes to beer_recipes.xlsx")

            df.to_json('beer_recipes.json', orient='records')
            print(f"Saved {len(all_recipes)} recipes to beer_recipes.json")

            with sqlite3.connect('beer_recipes.db') as conn:
                df.to_sql('recipes', conn, if_exists='replace', index=False)
                print("Saved recipes to beer_recipes.db")
                
        except ImportError as e:
            print(f"Error: Missing required package - {e}")
        except Exception as e:
            print(f"Error saving files: {e}")
            
    except KeyboardInterrupt:
        print("\nScraping interrupted by user")
        # Save progress on interrupt
        progress = {
            'last_page': page - 1,
            'recipes': all_recipes
        }
        with open('scraping_progress.json', 'w') as f:
            json.dump(progress, f)
        print(f"Progress saved at page {page-1}")

if __name__ == "__main__":
    main()
