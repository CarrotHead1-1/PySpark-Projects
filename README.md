

Step 1: Data Collection 
    - Demographics (UK census data: age, income, emplyment, population density)
    - Competitor data (Google Maps, Yelp API?)
    - Mobility Data (TFL)
    - Real Estate rental price data 

Step 2: ETF with PySpark
    - Ingest demographic data
    - scrape competitor locations
    - combine transport data (station ridership near locations)

Step 3: Feature Engineering
    - Estate Foot traffic potential (population density + transit ridership)
    - competitor density index (competitors / population in area)
    - Disposible income (average income = average rent)

Step 4 Analysis 