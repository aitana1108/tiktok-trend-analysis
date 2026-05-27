import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
hashtags = pd.read_csv('top_hashtags_2025.csv')
monthly = pd.read_csv('monthly_trends_2025.csv')
country = pd.read_csv('country_platform_summary_2025.csv')

# Filter TikTok only
tiktok_hashtags = hashtags[hashtags['platform'] == 'TikTok']
tiktok_monthly = monthly[monthly['platform'] == 'TikTok']
tiktok_country = country[country['platform'] == 'TikTok']

# Chart 1 - Top 10 hashtags by views
top10 = tiktok_hashtags.nlargest(10, 'views')
plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x='views', y='hashtag', palette='rocket')
plt.title('Top 10 TikTok Hashtags by Views (2025)')
plt.xlabel('Total Views')
plt.ylabel('Hashtag')
plt.tight_layout()
plt.savefig('chart1_top_hashtags.png')
plt.close()
print("Chart 1 done")

# Chart 2 - Monthly engagement trend
tiktok_monthly['year_month'] = tiktok_monthly['year_month'].astype(str)
monthly_grouped = tiktok_monthly.groupby('year_month')['avg_er'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_grouped, x='year_month', y='avg_er', marker='o', color='red')
plt.title('Average TikTok Engagement Rate by Month (2025)')
plt.xlabel('Month')
plt.ylabel('Average Engagement Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart2_monthly_engagement.png')
plt.close()
print("Chart 2 done")

# Chart 3 - Top 10 countries by engagement
top_countries = tiktok_country.nlargest(10, 'median_er')
plt.figure(figsize=(12, 6))
sns.barplot(data=top_countries, x='median_er', y='country', palette='mako')
plt.title('Top 10 Countries by TikTok Engagement Rate (2025)')
plt.xlabel('Median Engagement Rate')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('chart3_top_countries.png')
plt.close()
print("Chart 3 done")

print("All charts saved!")