# Currency Conversion Script

This Python script fetches and displays the currency conversion rate for a given date using the Frankfurter API.

## Usage

To use the script, you need to provide three arguments in the following order:
1. `<date>`: The date for which you want the conversion rate (format: YYYY-MM-DD).
2. `<currency1>`: The currency you want to convert from (e.g., USD, EUR).
3. `<currency2>`: The currency you want to convert to (e.g., GBP, AUD).

```sh
python main.py <date> <currency1> <currency2>

Example 
python main.py 2022-01-01 GBP AUD

Expected output
The conversion rate on 2022-01-01 from GBP to AUD was 1.8583.The inverse rate was 0.53812.
