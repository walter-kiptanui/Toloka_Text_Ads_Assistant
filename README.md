# Toloka_Text_Ads_Assistant 
Toloka is an online platform where one can perform tasksand get paid. One of the tasks include classifying text data. "Is the Ad a Good Match to the Search Term" is one such task.
It involves classify text data dispayed by a web page given a user's search term. The text data can be classified as either Good or Other.These are the labels of the data.
With regards to this, I am creating a chatbot that will try to automatically classify the text data. This involves data scraping, data preparation and natural language processing (NLP)
I have done manual data scraping from the task's page. The raw data that I have obtained I have stored it in MySQL software where I have prepared the data in appropriate tables.
The table has 5 colums; Task_ID, User_Search_Term, Ad, Website and relevance.
After data collection and preparation I exported the data to a local location in my PC in a csv format. The classification project was done on google colab.
Up to now, I have used 2 models to compare the prediction accuracy
