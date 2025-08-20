# lib/debug.py
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

# create author and magazines
a1 = Author("Bianca Wanjiku")
m1 = Magazine("TechWorld", "Technology")
m2 = Magazine("RobloxMag", "Gaming")

# add articles
a1.add_article(m1, "AI in 2025")
a1.add_article(m2, "Thrill in Playing Roblox")
a1.add_article(m1, "The Future of Robotics")

# print all articles
print("\n--- All Articles ---")
for article in Article.all:
    print(f"Title: {article.title}, Author: {article.author.name}, Magazine: {article.magazine.name}")

# print magazines written by author
print("\n--- Magazines by Author ---")
for mag in a1.magazines():
    print(f"{mag.name} ({mag.category})")

# print topic areas
print("\n--- Topic Areas ---")
topics = a1.topic_areas()
if topics:
    for topic in topics:
        print(topic)
else:
    print("No topic areas found.")

