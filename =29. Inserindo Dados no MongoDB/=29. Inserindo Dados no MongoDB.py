from pymongo import MongoClient

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "titulo": "FastApi",
    "category": "BackEnd",
    "author": {
        "name": "Nicolas",
        "email": "nicolas@email.com"
    }
}

post2 = {
    "titulo": "Streamlit",
    "category": "Data Analysis",
    "author": {
        "name": "Davi",
        "email": "daviverson@email.com"
    }
}

result = mycol.insert_one(post1)
result = mycol.insert_one(post2)
print("Documento incluído com sucesso!")