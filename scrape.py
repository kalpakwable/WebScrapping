import requests,sqlite3
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt



# Connect to SQL Server
conn = sqlite3.connect('DRIVER=mcom.microsoft.sqlserver;'
                      'SERVER=my_server;'
                      'DATABASE=my_database;'
                      'UID=kalpak123;'
                      'PWD=Qwerty@123')

cursor = conn.cursor()

# Create a table to store news items if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INT PRIMARY KEY IDENTITY(1,1),
        category NVARCHAR(255),
        title NVARCHAR(255),
        Published NVARCHAR(255),
        author NVARCHAR(255),
        time NVARCHAR(255),
        date NVARCHAR(255),      
        body NVARCHAR(MAX),
        source NVARCHAR(255),
    )
''')



try:
    origin = requests.get('https://inshorts.com/en/read/science')
    origin.raise_for_status()

    soup = BeautifulSoup(origin.text,'html.parser').encode("utf-8") ## have added this utf8 because I was getting a error UnicodeEncodeError 'charmap' coded can't encode character
    
    science = soup.find('div',style_="min-height: calc(100vh - 348px);").find_all('div')

    for news_cate1 in science:
        Category = news_cate1.find('div',class_="QqxB5Ed9A73reHbF2fQC").get_text(strip=True).split('')[10]
        Title = news_cate1.find('span',itemprop = 'headline').text
        Published = news_cate1.find('div').get_text(strip = True).split('')[1]
        Author = news_cate1.find('span', class_ = 'Author' ).text
        Time = news_cate1.find('span', class_ = 'datePublished' ).strong.text
        Date = news_cate1.find('span', class_ = 'Date' ).Date
        Body = news_cate1.find('div',itemprop = 'articleBody').text
        Source = news_cate1.find('div').a.text

        cursor.execute('''
        INSERT INTO news (date, time, author, title, body, source, category)
        
        ''', (news_cate1['Category'],news_cate1['Published'],news_cate1['Title'],news_cate1['Author'], news_cate1['Time'],news_cate1['Date'],
          news_cate1['Body'], news_cate1['Source']))
        
except Exception as e:
    print(e)



try:
    origin = requests.get('https://inshorts.com/en/read/technology')
    origin.raise_for_status()

    soup = BeautifulSoup(origin.text,'html.parser').encode("utf-8") 
    
    technology = soup.find('div',style_="min-height: calc(100vh - 348px);").find_all('div')

    for news_cate1 in technology:
        Category = news_cate1.find('div',class_="QqxB5Ed9A73reHbF2fQC").get_text(strip=True).split('')[10]
        Title = news_cate1.find('span',itemprop = 'headline').text
        Published = news_cate1.find('div').get_text(strip = True).split('')[1]
        Author = news_cate1.find('span', class_ = 'Author' ).text
        Time = news_cate1.find('span', class_ = 'datePublished' ).strong.text
        Date = news_cate1.find('span', class_ = 'Date' ).Date
        Body = news_cate1.find('div',itemprop = 'articleBody').text
        Source = news_cate1.find('div').a.text

        cursor.execute('''
        INSERT INTO news (date, time, author, title, body, source, category)
        
        ''', (news_cate1['Category'],news_cate1['Published'],news_cate1['Title'],news_cate1['Author'], news_cate1['Time'],news_cate1['Date'],
          news_cate1['Body'], news_cate1['Source']))
        
except Exception as e:
    print(e)



try:
    origin = requests.get('https://inshorts.com/en/read/automobile')
    origin.raise_for_status()

    soup = BeautifulSoup(origin.text,'html.parser').encode("utf-8") ## have added this utf8 because I was getting a error UnicodeEncodeError 'charmap' coded can't encode character
    
    automobile = soup.find('div',style_="min-height: calc(100vh - 348px);").find_all('div')

    for news_cate1 in automobile:
        Category = news_cate1.find('div',class_="Qdlnsjhldvhbj78Wyldnvlnvl").get_text(strip=True).split('')[10]
        Title = news_cate1.find('span',itemprop = 'headline').text
        Published = news_cate1.find('div').get_text(strip = True).split('')[1]
        Author = news_cate1.find('span', class_ = 'Author' ).text
        Time = news_cate1.find('span', class_ = 'datePublished' ).strong.text
        Date = news_cate1.find('span', class_ = 'Date' ).Date
        Body = news_cate1.find('div',itemprop = 'articleBody').text
        Source = news_cate1.find('div').a.text 
  
        cursor.execute('''
        INSERT INTO news (date, time, author, title, body, source, category)
        
        ''', (news_cate1['Category'],news_cate1['Published'],news_cate1['Title'],news_cate1['Author'], news_cate1['Time'],news_cate1['Date'],
          news_cate1['Body'], news_cate1['Source']))
except Exception as e:
    print(e)



try:
    origin = requests.get('https://inshorts.com/en/read/hatke')
    origin.raise_for_status()

    soup = BeautifulSoup(origin.text,'html.parser').encode("utf-8") ## have added this utf8 because I was getting a error UnicodeEncodeError 'charmap' coded can't encode character
    
    hatke = soup.find('div',style_="min-height: calc(100vh - 348px);").find_all('div')

    for news_cate1 in hatke:
        Category = news_cate1.find('div',class_="Swyeiksknm73reHbF2fQC").get_text(strip=True).split('')[10]
        Title = news_cate1.find('span',itemprop = 'headline').text
        Published = news_cate1.find('div').get_text(strip = True).split('')[1]
        Author = news_cate1.find('span', class_ = 'Author' ).text
        Time = news_cate1.find('span', class_ = 'datePublished' ).strong.text
        Date = news_cate1.find('span', class_ = 'Date' ).Date
        Body = news_cate1.find('div',itemprop = 'articleBody').text
        Source = news_cate1.find('div').a.text  

        cursor.execute('''
        INSERT INTO news (date, time, author, title, body, source, category)
        
        ''', (news_cate1['Category'],news_cate1['Published'],news_cate1['Title'],news_cate1['Author'], news_cate1['Time'],news_cate1['Date'],
          news_cate1['Body'], news_cate1['Source']))    
except Exception as e:
    print(e)


# Commit the changes and close the connection
conn.commit()
conn.close()


# Extract text from news items
text = ' '.join([news_item['title'] + ' ' + news_item['body'] for news_item in news_cate1])

# Specify keywords for analysis
keywords = ["Diwali", "Offer", "Discount", "Dhamaka", "Dead", "Fire", "Burn"]

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(text))

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
