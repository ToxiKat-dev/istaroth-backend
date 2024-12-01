from app.constants import DB
from bson import ObjectId
from pymongo import errors as mongoErrors

collection = DB["template"]

class TemplateModel:
    def __init__(
        self,
        id:str = None,
    ):
        self.id = id

    def save(self):
        if self.id:
            result = collection.update_one(
                {"_id" : ObjectId(self.id)},
                {"$set" : self.to_dict()}
            )
            if result.modified_count != 1:
                raise mongoErrors.OperationFailure("Failed to update")
        else:
            raise AttributeError("id not found")
        
    def create(self):
        if not self.id:
            result = collection.insert_one(self.to_dict(addId=False))
            self.id = str(result.inserted_id)
        else:
            raise Exception()


    def find(filter:dict):
        docs = collection.find(filter)
        return TemplateModel.list_from_json(docs)
    
    def find_one(filter:dict):
        doc = collection.find_one(filter)
        if doc:
            return TemplateModel.from_json(doc)
        else:
            return None
        
    def find_by_id(id:str):
        doc = collection.find_one({"_id":ObjectId(id)})
        if doc:
            return TemplateModel.from_json(doc)
        else:
            return None

    def from_json(doc:dict):
        return TemplateModel(
            id = str(doc["_id"]),
        )
    
    def list_from_json(docs:list[dict]):
        return [TemplateModel.from_json(doc) for doc in docs]
    
    def to_dict(self, addId:bool = True):
        doc = {
        }
        if addId:
            doc["_id"] = ObjectId(self.id)
        return doc
    
    def to_json(self):
        return {
            "_id" : self.id,
        }