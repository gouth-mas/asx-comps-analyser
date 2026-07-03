import statistics
import yfinance as yf

target = input("Enter target ticker: ").strip().upper()
comps_input = input("Enter comparable tickers (comma separated): ").strip().upper()
comp_tickers = [t.strip() for t in comps_input.split(",")]

all_tickers = [target] + comp_tickers

rows = []

for ticker in all_tickers:
    info = yf.Ticker(ticker + ".AX").info
    
    market_cap = info.get("marketCap", None)
    total_debt = info.get("totalDebt", None)
    cash = info.get("totalCash", None)
    ebitda = info.get("ebitda", None)
    revenue = info.get("totalRevenue", None)
    pe = info.get("trailingPE", None)
    pb = info.get("priceToBook", None)
    name = info.get("longName", None)
    
    ev = market_cap + total_debt - cash if market_cap and total_debt and cash else 0
    ev_ebitda = ev / ebitda if ev and ebitda else 0
    ev_revenue = ev / revenue if ev and revenue else 0
    
    rows.append({
        "ticker": ticker,
        "name": name,
        "ev": ev,
        "ev_ebitda": ev_ebitda,
        "ev_revenue": ev_revenue,
        "pe": pe,
        "pb": pb,
    })
print("\n" + "="*70)
print("  COMPARABLE COMPANIES ANALYSIS")
print("="*70)
print(f"Target: {target}\n")
print(f"{'Ticker':<6} {'Name':<30} {'EV($B)':>8} {'EV/EBITDA':>10} {'EV/Rev':>8} {'P/E':>8} {'P/B':>6}")
print("-"*70)

ev_ebitda_vals = []
ev_revenue_vals = []
pe_vals = []
pb_vals = []

for row in rows:
    ev_b = row['ev'] / 1_000_000_000 if row['ev'] else 0
    pe_str = f"{row['pe']:>7.1f}x" if row['pe'] else "    N/A"
    pb_str = f"{row['pb']:>5.1f}x" if row['pb'] else "  N/A"
    print(f"{row['ticker']:<6} {row['name'][:28]:<30} {ev_b:>7.1f}B {row['ev_ebitda']:>9.1f}x {row['ev_revenue']:>7.2f}x {pe_str} {pb_str}")
    
    if row['ev_ebitda']: ev_ebitda_vals.append(row['ev_ebitda'])
    if row['ev_revenue']: ev_revenue_vals.append(row['ev_revenue'])
    if row['pe']: pe_vals.append(row['pe'])
    if row['pb']: pb_vals.append(row['pb'])

print("-"*70)
print(f"{'Mean':<38} {statistics.mean(ev_ebitda_vals):>9.1f}x {statistics.mean(ev_revenue_vals):>7.2f}x {statistics.mean(pe_vals):>7.1f}x {statistics.mean(pb_vals):>5.1f}x")
print(f"{'Median':<38} {statistics.median(ev_ebitda_vals):>9.1f}x {statistics.median(ev_revenue_vals):>7.2f}x {statistics.median(pe_vals):>7.1f}x {statistics.median(pb_vals):>5.1f}x")
print("="*70)