from sqlalchemy.orm import Session

class BaseRepository():
    def __init__(self, db: Session):
        self.db = db

    def create(self, model):
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model
    
    def get_by_id(self, model_class, model_id):
        return self.db.query(model_class).filter(model_class.id == model_id).first()

    def update(self, model):
        self.db.commit()
        self.db.refresh(model)
        return model

    def delete(self, model):
        self.db.delete(model)
        self.db.commit()
