import json

originDestinationDefinitions = json.dumps(
    {
        "w_geocode": "workplace census block",
        "h_geocode": "residence census block",
        "commuters": "number of commuters between blocks",
        "year": "census year"
    }
 )

originDestinationCharacteristicsDefinitions= json.dumps(
      {
        "h_geocode": "Residence census block",
        "c000": "Total number of jobs",
        "ca01": "Number of jobs for workers age 29 or younger",
        "ca02": "Number of jobs for workers age 30 to 54",
        "ca03": "Number of jobs for workers age 55 or older",
        "ce01": "Number of jobs with earnings $1250/month or less",
        "ce02": "Number of jobs with earnings $1251/month to $3333/month",
        "ce03": "Number of jobs with earnings greater than $3333/month",
        "cns01": "Number of jobs in NAICS sector 11 (Agriculture, Forestry, Fishing and Hunting)",
        "cns02": "Number of jobs in NAICS sector 21 (Mining, Quarrying, and Oil and Gas Extraction)",
        "cns03": "Number of jobs in NAICS sector 22 (Utilities)",
        "cns04": "Number of jobs in NAICS sector 23 (Construction)",
        "cns05": "Number of jobs in NAICS sector 31-33 (Manufacturing)",
        "cns06": "Number of jobs in NAICS sector 42 (Wholesale Trade)",
        "cns07": "Number of jobs in NAICS sector 44-45 (Retail Trade)",
        "cns08": "Number of jobs in NAICS sector 48-49 (Transportation and Warehousing)",
        "cns09": "Number of jobs in NAICS sector 51 (Information)",
        "cns10": "Number of jobs in NAICS sector 52 (Finance and Insurance)",
        "cns11": "Number of jobs in NAICS sector 53 (Real Estate and Rental and Leasing)",
        "cns12": "Number of jobs in NAICS sector 54 (Professional, Scientific, and Technical Services)",
        "cns13": "Number of jobs in NAICS sector 55 (Management of Companies and Enterprises)",
        "cns14": "Number of jobs in NAICS sector 56 (Administrative and Support and Waste\nManagement and Remediation Services)",
        "cns15": "Number of jobs in NAICS sector 61 (Educational Services)",
        "cns16": "Number of jobs in NAICS sector 62 (Health Care and Social Assistance)",
        "cns17": "Number of jobs in NAICS sector 71 (Arts, Entertainment, and Recreation)",
        "cns18": "Number of jobs in NAICS sector 72 (Accommodation and Food Services)",
        "cns19": "Number of jobs in NAICS sector 81 (Other Services [except Public Administration])",
        "cns20": "Number of jobs in NAICS sector 92 (Public Administration)",
        "cr01": "Number of jobs for workers with Race: White, Alone",
        "cr02": "Number of jobs for workers with Race: Black or African American Alone",
        "cr03": "Number of jobs for workers with Race: American Indian or Alaska Native Alone",
        "cr04": "Number of jobs for workers with Race: Asian Alone",
        "cr05": "Number of jobs for workers with Race: Native Hawaiian or Other Pacific Islander\nAlone",
        "cr07": "Number of jobs for workers with Race: Two or More Race Groups",
        "ct01": "Number of jobs for workers with Ethnicity: Not Hispanic or Latino",
        "ct02": "Number of jobs for workers with Ethnicity: Hispanic or Latino",
        "cd01": "Number of jobs for workers with Educational Attainment: Less than high school",
        "cd02": "Number of jobs for workers with Educational Attainment: High school or equivalent,\nno college",
        "cd03": "Number of jobs for workers with Educational Attainment: Some college or Associate\ndegree1",
        "cd04": "Number of jobs for workers with Educational Attainment: Bachelor's degree or\nadvanced degree",
        "cs01": "Number of jobs for workers with Sex: Male",
        "cs02": "Number of jobs for workers with Sex: Femal",
        "year": "Date on which data was created, formatted as YYYYMMDD"
      }
)
