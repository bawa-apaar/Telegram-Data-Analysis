# Analyzing-the-Narrative-Shift-of-Russian-Propaganda-on-Telegram
This is the comprehensive evaluation of the telegram posts that were broadcast by pro-Russian propaganda channels before and after Russia invaded Ukraine.

## Dataset
Given Telegram’s popularity and growing influence, I collect and analyze data from the most prominent Russian Telegram channels. Specifically, we (I, Dr. Ugur Kursuncu, Dr. Dilshod Achilov) identified four Telegram channels are: `Kadyrov_95 (3M subscribers)`, `Solovyov (1.3M subscribers)`, `Operation_Z (1.3M subscribers)`, and `Colonelcassed (843k subscribers)`. Main rationale for selecting these channels is driven by the following three factors: they (a) are consistently ranked in the top ten most following channels, (b) are led by the most prominent Kremlin-linked propagandists, (c) have been active content creators of Russian pro-war propaganda. While two of the channels (Kadyrov_95 and Solovyov) predominantly post content about general issues pertaining to Russia (and Kremlin’s related spin-off version), the other two mainly focus on Russian war efforts in Ukraine. 

I used telegram's Telethon library to interact with Telegram in order to extract messages from above mentinoed channels. 

To install Telethon:
`python3 -m pip install telethon`
CSV files for the data is present under Dataset folder.

We are analyzing the drift among the posts and corresponding user interaction among pro-russian channels from a year before to a year after the war. We performed comprehensive comparative analysis on the posts with respect to: (1) Post volume by modalities  (2) Views (3) Forwards (4) Reactions (5) Replies and (6) Content. 

Collected data from posts are in the russian language. Hence, all analysis are correspond to the russian language.

I've added subset_telegram_data.csv as subset of data only as whole dataset is more than 1 gb and isn't viable to upload that heavy file on github.

### scrape_telegram_channel.py - python code for data collection from telegram channels.

### EDA/volume_views_forwards_reactions_analysis.ipynb - Statistical Analysis on volume, views, forwards and reactions

### EDA/engagement score.ipynb - Statistical Analysis calculating the engagement score

### EDA/popularity score.ipynb - Statistical Analysis calculating the popularity score

### EDA/n-gram analysis.ipynb - n-gram analysis (unigrams, bigrams and trigrams)
