from app.database import db

async def create_task(user_id, data):
    task = {
        "user_id": user_id,
        "title": data.title,
        "description": data.description,
        "status": data.status,
        "due_date": data.due_date,
        "created_at": __import__("datetime").datetime.utcnow()
    }
    result = await db.tasks.insert_one(task)
    task["_id"] = result.inserted_id
    return task

async def get_tasks(user_id):
    tasks = await db.tasks.find({"user_id": user_id}).to_list(100)
    return tasks

async def get_task(user_id, task_id):
    from bson import ObjectId
    task = await db.tasks.find_one({"_id": ObjectId(task_id), "user_id": user_id})
    return task

async def update_task(user_id, task_id, data):
    from bson import ObjectId
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    await db.tasks.update_one({"_id": ObjectId(task_id), "user_id": user_id}, {"$set": update_data})
    return await get_task(user_id, task_id)

async def delete_task(user_id, task_id):
    from bson import ObjectId
    await db.tasks.delete_one({"_id": ObjectId(task_id), "user_id": user_id})
