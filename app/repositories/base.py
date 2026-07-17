from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, model):
        self.db.add(model)
        return model
    
    def get_by_id(self, model_class, model_id):
        return self.db.query(model_class).filter(model_class.id == model_id).first()

    def delete(self, model):
        self.db.delete(model)
