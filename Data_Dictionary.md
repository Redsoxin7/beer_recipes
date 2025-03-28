# Data Dictionary

## `styles_2021_cleaned` DataFrame

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| `Style` | string | The name of the beer style according to BJCP guidelines |
| `Category` | string | The broader category the beer style belongs to |
| `ogmin` | float | Minimum Original Gravity value for the style |
| `ogmax` | float | Maximum Original Gravity value for the style |
| `fgmin` | float | Minimum Final Gravity value for the style |
| `fgmax` | float | Maximum Final Gravity value for the style |
| `abvmin` | float | Minimum Alcohol By Volume percentage for the style |
| `abvmax` | float | Maximum Alcohol By Volume percentage for the style |
| `ibumin` | float | Minimum International Bitterness Units for the style |
| `ibumax` | float | Maximum International Bitterness Units for the style |
| `srmmin` | float | Minimum Standard Reference Method color value for the style |
| `srmmax` | float | Maximum Standard Reference Method color value for the style |

## `beer_recipes` DataFrame

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| `Recipe Name` | object (string) | The name of the beer recipe |
| `Style` | object (string) | The name of the beer style of the recipe |
| `Style Number` | object (string) | The BJCP style number/identifier for the beer style |
| `OG` | float64 | Original Gravity - the density of the wort before fermentation |
| `Plato` | float64 | Degrees Plato - alternative measurement of wort density (sugar content) |
| `FG` | float64 | Final Gravity - the density of the beer after fermentation |
| `ABV` | float64 | Alcohol By Volume - percentage of alcohol in the finished beer |
| `IBU` | float64 | International Bitterness Units - measure of beer bitterness |
| `Source` | object (string) | The source or origin of the beer recipe |
| `Category` | object (string) | The broader category the beer style belongs to |

## Relationship Between the DataFrames

The two DataFrames are related through the `Style` column:

- `styles_2021_cleaned` contains the BJCP style guidelines with acceptable ranges for various beer characteristics (OG, FG, ABV, IBU).
- `beer_recipes` contains actual beer recipes with measured values for these same characteristics.

When analyzing beer recipe compliance, the actual values in `beer_recipes` (OG, FG, ABV, IBU) are compared against the acceptable ranges defined in `styles_2021_cleaned` to determine if a recipe meets the style guidelines.

For example, a recipe for an American IPA in `beer_recipes` would be checked against the min/max values for OG, FG, ABV, and IBU specified for American IPA in the `styles_2021_cleaned` DataFrame to determine if the recipe complies with the style guidelines.

The `Style Number` in `beer_recipes` provides an additional reference to the BJCP style guidelines, though the analysis primarily uses the `Style` name for matching.