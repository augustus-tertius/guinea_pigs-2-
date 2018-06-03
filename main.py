import services
import database
from wordcloud import WordCloud

# for start
# services.load_comments()

mondoDB = database.MongoDBManagment()

all_messages = mondoDB.get_all()
print("Number of messages : " + str(all_messages.count()))
# for each_message in all_messages:
#     print(each_message)

all_text = []
for each_message in all_messages:
    all_text.append(each_message["text"])
print("Number of text : " + str(len(all_text)))

canonized_text = services.canonize_text(all_text)
print(canonized_text)

# services.generate_cloud(canonized_text)

