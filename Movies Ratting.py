import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

movies=pd.read_csv('movies1.csv')
movie_link=pd.read_excel('movie_links.xlsx')
movi=pd.read_excel('movi.xlsx')
ratings = pd.read_csv('ratings1.csv')
tags=pd.read_csv('tags1.csv')
links=pd.read_csv('links.csv')
#movie dataset
movies.describe()

movies.info()

movies.shape

movies.count
 
movies.dtypes

movies.columns

movies.isnull().sum()
#links dataset
links.describe()

links.info()

links.shape

links.count
 
links.dtypes

links.columns

links.isnull().sum()

#tags dataset

tags.describe()

tags.info()

tags.shape

tags.count
 
tags.dtypes

tags.columns

tags.isnull().sum()

#rating dataset

ratings.describe()

ratings.info()

ratings.shape

ratings.count
 
ratings.dtypes

ratings.columns

ratings.isnull().sum()

#movies dataset

m1 = g12['genres'].str.get_dummies('|')

print(m1)
# m2 is the merged dataset of movies and ratings

m2 = g12.join(g12.pop('genres').str.get_dummies('|'))

print (m2)
#finding the total number of years of movie released

g1=movies.groupby(['year'],as_index=False)['movie_name'].count()

print(g1)
#Barchart
plt.figure(figsize=(20,6))
plt.xticks(rotation=90)
sns.barplot(x='year',y='movie_name',data=g1,ci=None)
#pie chart
plt.figure(figsize=(10,10))
plt.pie(g1['movie_name'],labels=g1['year'],autopct='%0.1f%%')
#count the genres

genres=movies['genres'].str.get_dummies('|').sum()

print(genres)

#bar chart for the count for genres

plt.figure(figsize=(6,6))
plt.xticks(rotation=90)
sns.barplot(x='genres',y='count',data=movi,ci=None)

#pie chart for the count for genres

plt.figure(figsize=(10,10))
plt.pie(movi['count'],labels=movi['genres'],autopct='%0.1f%%')

#Finding the avarege ratings for each and every genres
 
Action=m2.groupby(['Action'],as_index=False)['rating'].mean()
Adventure=m2.groupby(['Adventure'],as_index=False)['rating'].mean()
Animation=m2.groupby(['Animation'],as_index=False)['rating'].mean()
Biography=m2.groupby(['Biography'],as_index=False)['rating'].mean()
Children=m2.groupby(['Children'],as_index=False)['rating'].mean()
Comedy=m2.groupby(['Comedy'],as_index=False)['rating'].mean()
Crime=m2.groupby(['Crime'],as_index=False)['rating'].mean()
Documentary=m2.groupby(['Documentary'],as_index=False)['rating'].mean()
Drama=m2.groupby(['Drama'],as_index=False)['rating'].mean()
Epic=m2.groupby(['Epic'],as_index=False)['rating'].mean()
Fantasy=m2.groupby(['Fantasy'],as_index=False)['rating'].mean()
Film_Noir=m2.groupby(['Film-Noir'],as_index=False)['rating'].mean()
Horror=m2.groupby(['Horror'],as_index=False)['rating'].mean()
IMAX=m2.groupby(['IMAX'],as_index=False)['rating'].mean()
print(IMAX)
Musical=m2.groupby(['Musical'],as_index=False)['rating'].mean()
Mystery=m2.groupby(['Mystery'],as_index=False)['rating'].mean()
Romance=m2.groupby(['Romance'],as_index=False)['rating'].mean()
Satire=m2.groupby(['Satire'],as_index=False)['rating'].mean()
Sci_Fi=m2.groupby(['Sci-Fi'],as_index=False)['rating'].mean()
Sports=m2.groupby(['Sports'],as_index=False)['rating'].mean()
Thriller=m2.groupby(['Thriller'],as_index=False)['rating'].mean()
War=m2.groupby(['War'],as_index=False)['rating'].mean()
Western=m2.groupby(['Western'],as_index=False)['rating'].mean()

#Finally we got the avaeage rating for every genres
#then i mannualy noted and created it in .xlsx dataset

genres_ratings=pd.read_excel('ratings_genres.xlsx')



plt.figure(figsize=(6,6))
plt.xticks(rotation=90)
sns.barplot(x='genres',y='rating',data=genres_ratings,ci=None)

drop1=m2.drop(['movieId','movie_name','rating'],axis=1)

years_count = m2.groupby(['year'],as_index=False)['Action', 'Adventure','Animation', 'Biography', 'Children', 'Comedy', 'Crime', 'Documentary','Drama', 'Epic', 'Fantasy', 'Film-Noir', 'Horror', 'IMAX', 'Musical','Mystery', 'Romance', 'Satire', 'Sci-Fi', 'Sports', 'Thriller', 'War','Western'].sum().T


count1 = pd.read_excel('genres_count_years.xlsx')

plt.figure(figsize=(6,6))
plt.xticks(rotation=90)
sns.barplot(x='genres',y='year_2002',data=count1,ci=None)
count1.isnull().sum()

Action = count1.groupby(['year_1902'],as_index = False)['genres'].sum()

plt.figure(figsize=(10,10))
plt.pie(count1['year_2008'],labels=count1['genres'])#,autopct='%0.1f%%')

print(m2.rating > 4)


# ratings with < 1
h1 = m2[m2.rating <= 1]

# ratings with 1 to 2
h2 = m2[m2.rating <= 2]
h2 = h2[h2.rating > 1]

# ratings with 2 to 3
h3 = m2[m2.rating <= 3]
h3 = h3[h3.rating > 2]

# ratings with 3 to 4
h4 = m2[m2.rating <= 4]
h4 = h4[h4.rating > 3]

# rating with 4 to 5
h5 = m2[m2.rating <= 5]
h5 = h5[h5.rating > 4]















