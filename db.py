# db.py
from motor.motor_asyncio import AsyncIOMotorClient

mongoURL = "mongodb+srv://admin:admin@cluster0.vsqvu32.mongodb.net/?appName=Cluster0"

client = AsyncIOMotorClient(mongoURL, tls=True)

database = client["ExpenseDB"]

user_collection = database["DevopBE"]
expense_collection = database["user_expenses"]
