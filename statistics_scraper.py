import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd 

header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}

url = 'https://stockanalysis.com/stocks/amd/financials/'

r = requests.get(url, headers = header)
stats = BeautifulSoup(r.text, 'html.parser')

table = stats.find('main', {'class': 'contain'})
income = table.find('div', {'class': 'table-wrap svelte-17fayh1'}).find_all('tr')

years = income[0].find_all('th')
revenue = income[1].find_all('td')
revenue_growth = income[2].find_all('td')
cost_of_revenue = income[3].find_all('td')
gross_profit = income[4].find_all('td')
sga = income[5].find_all('td')
r_and_d = income[6].find_all('td')
other_expenses = income[7].find_all('td')
operation_expenses = income[8].find_all('td')
operation_income = income[9].find_all('td')
interest_expense_income = income[10].find_all('td')
other_expense_income = income[11].find_all('td')
pretax_income = income[12].find_all('td')
income_tax = income[13].find_all('td')
net_income = income[14].find_all('td')
net_income_common = income[15].find_all('td')
net_income_growth = income[16].find_all('td')
shares_outstanding_basic = income[17].find_all('td')
shares_outstanding_diluted = income[18].find_all('td')
shares_changes = income[19].find_all('td')
eps_basic = income[20].find_all('td')
eps_diluted = income[21].find_all('td')
eps_growth = income[22].find_all('td')
fccps = income[23].find_all('td')
gross_margin = income[24].find_all('td')
operating_margin = income[25].find_all('td')
profit_margin = income[26].find_all('td')
fcfm = income[27].find_all('td')
effective_tax_rate = income[28].find_all('td')
editda = income[29].find_all('td')
editda_margin = income[30].find_all('td')
depreciation_amoritzation = income[31].find_all('td')
ebit = income[32].find_all('td')
ebit_margin = income[33].find_all('td')

relavent_years = len(years) - 1
# print(relavent_years)

# lists
time_period = []
revenue_text = []
rg_text = []
cost_rev_text = []
gp_text = []
sga_text = []
rd_text = []
oe_text = []
ope_text = []
oi_text = []
iei_text = []
oei_text = []
pri_text = []
it_text = []
ni_text = []
nic_text = []
nig_text = []
sob_text = []
sod_text = []
sc_text = []
eb_text = []
ed_text = []
eg_text = []
f_text = []
gm_text = []
om_text = []
pm_text = []
fcfm_text = []
etr_text = []
editda_text = []
edim_text = []
da_text = []
ebit_text = []
ebm_text = []

# add all table to array
for i in range(0, relavent_years):
    time_period.append(years[i].text)
    revenue_text.append(revenue[i].text)
    rg_text.append(revenue_growth[i].text)
    cost_rev_text.append(cost_of_revenue[i].text)
    gp_text.append(gross_profit[i].text)
    sga_text.append(sga[i].text)
    rd_text.append(r_and_d[i].text)
    oe_text.append(other_expenses[i].text)
    ope_text.append(operation_expenses[i].text)
    oi_text.append(operation_income[i].text)
    iei_text.append(interest_expense_income[i].text)
    oei_text.append(other_expense_income[i].text)
    pri_text.append(pretax_income[i].text)
    it_text.append(income_tax[i].text)
    ni_text.append(net_income[i].text)
    nic_text.append(net_income_common[i].text)
    nig_text.append(net_income_growth[i].text)
    sob_text.append(shares_outstanding_basic[i].text)
    sod_text.append(shares_outstanding_diluted[i].text)
    sc_text.append(shares_changes[i].text)
    eb_text.append(eps_basic[i].text)    
    ed_text.append(eps_diluted[i].text)
    eg_text.append(eps_growth[i].text)
    f_text.append(fccps[i].text)
    gm_text.append(gross_margin[i].text)
    om_text.append(operating_margin[i].text)
    pm_text.append(profit_margin[i].text)
    fcfm_text.append(fcfm[i].text)
    etr_text.append(effective_tax_rate[i].text)
    editda_text.append(editda[i].text)
    edim_text.append(editda_margin[i].text)
    da_text.append(depreciation_amoritzation[i].text)
    ebit_text.append(ebit[i].text)
    ebm_text.append(ebit_margin[i].text)

# print(time_period)

# save all data into a disctionary with keys being data type and values being the list of data, rstrip() at the end removes trailing lines from keys
income_dict = {
    time_period[0]: time_period[1:],
    revenue_text[0].rstrip(): revenue_text[1:],
    rg_text[0].rstrip(): rg_text[1:],
    cost_rev_text[0].rstrip(): cost_rev_text[1:],
    gp_text[0].rstrip(): gp_text[1:],
    sga_text[0].rstrip(): sga_text[1:],
    rd_text[0].rstrip(): rd_text[1:],
    oe_text[0].rstrip(): oe_text[1:],
    ope_text[0].rstrip(): ope_text[1:],
    oi_text[0].rstrip(): oi_text[1:],
    iei_text[0].rstrip(): iei_text[1:],
    oei_text[0].rstrip(): oei_text[1:],
    pri_text[0].rstrip(): pri_text[1:],
    it_text[0].rstrip(): it_text[1:],
    ni_text[0].rstrip(): ni_text[1:],
    nic_text[0].rstrip(): nic_text[1:],
    nig_text[0].rstrip(): nig_text[1:],
    sob_text[0].rstrip(): sob_text[1:],
    sod_text[0].rstrip(): sod_text[1:],
    sc_text[0].rstrip(): sc_text[1:],
    eb_text[0].rstrip(): eb_text[1:],
    ed_text[0].rstrip(): ed_text[1:],
    eg_text[0].rstrip(): eg_text[1:],
    f_text[0].rstrip(): f_text[1:],
    gm_text[0].rstrip(): gm_text[1:],
    om_text[0].rstrip(): om_text[1:],
    pm_text[0].rstrip(): pm_text[1:],
    fcfm_text[0].rstrip(): fcfm_text[1:],
    etr_text[0].rstrip(): etr_text[1:],
    editda_text[0].rstrip(): editda_text[1:],
    edim_text[0].rstrip(): edim_text[1:],
    da_text[0].rstrip(): da_text[1:],
    ebit_text[0].rstrip(): ebit_text[1:],
    ebm_text[0].rstrip(): ebm_text[1:]
    }

# print(income_dict)

# save dictionary as json, need to save as pandas dataframe later to convert to database format
with open('financeAnnualIncomeData.json', 'w') as f:
    json.dump(income_dict, f)

# print(r.status_code)
# print(stats)
# print(revenue[1])