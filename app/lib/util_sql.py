from app import db


class ResourceMixin():
    def save(self):
        db.session.add(self)
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        return db.session.commit()
