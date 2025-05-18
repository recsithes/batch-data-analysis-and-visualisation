import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
OPENAI_API_KEY = "sk-test-1234567890abcdefABCDEF1234567890"
sdf = SmartDataframe(df, config={"llm": llm})
df = pd.read_csv('IPL_Squad_2023_Auction_Dataset.csv')
print(df.shape)
df.head()
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.head()
sdf.chat(df, prompt="Which players are the most costliest buys?")
prompts = """
Which players were the cheapest buys this season and which team bought them?
"""
sdf.chat(df, prompt=prompts)
prompts = """
Draw a Bargraph showing How much money was spent by each team this season overall.
"""
sdf.chat(df, prompt=prompts)
sdf.chat(df, prompt="How many bowler remained unsold and what was their base price?")
sdf.chat(df, prompt="How many players remained unsold this season?")
sdf.chat(df, prompt="Which type of players were majorly unsold?")
sdf.chat(df, prompt="What is total money spent by all teams in dollars?")
sdf.chat(df, prompt="Perform univariate analysis")
prompts = """
draw a barplot showing how much money was spent by Gujrat on all types of players?
"""
pandas_ai.run(df, prompt=prompts)
