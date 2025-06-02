from app.database import db
import asyncio

async def test_connection():
    users = await db.users.find().to_list(10)
    print(users)

if __name__ == "__main__":
    asyncio.run(test_connection())
