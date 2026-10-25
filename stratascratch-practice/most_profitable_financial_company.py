import pandas as pd
mask = forbes_global_2010_2014['sector'] == 'Financials'
financial_sector = forbes_global_2010_2014[mask]
profitable = financial_sector.sort_values(by = 'profits', ascending = False).nlargest(1, 'profits', keep = 'first')[['company','continent']]