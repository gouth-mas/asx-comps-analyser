# ASX Comparable Companies Analyser

A live comparable companies analysis tool built in Python. Input a target 
ASX stock and a set of peers — the tool pulls real-time financial data via 
Yahoo Finance and outputs a formatted comps table with key valuation multiples.

## Multiples calculated
- Enterprise Value (EV)
- EV/EBITDA
- EV/Revenue  
- P/E (trailing)
- P/B

## Output
Formatted comps table with mean and median benchmarks across all companies.

## How to run
```bash
pip install yfinance
python comps.py
```

Enter a target ticker (e.g. WES) and comma-separated comparables 
(e.g. WOW,COL,JBH) when prompted.

## Libraries
yfinance, statistics
