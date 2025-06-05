df['headline_length'] = df['headline'].apply(len)
publisher_counts = df['publisher'].value_counts()
df['publish_date'] = pd.to_datetime(df['publish_date'])
df['day_of_week'] = df['publish_date'].dt.day_name()
