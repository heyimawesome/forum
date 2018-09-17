from app import db


class ForumCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(32), index=True, unique=True)
    topics = db.relationship('ForumTopic', backref='category', lazy=True)


class ForumTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(32), index=True, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('forum_category.id'),
                            nullable=False)
    threads = db.relationship('ForumThread', backref='thread', lazy=True)


class ForumThread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer)
    topic_id = db.Column(db.Integer, db.ForeignKey('forum_topic.id'),
                         nullable=False)
    comments = db.relationship('ForumComment', backref='comment', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class ForumComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    thred_id = db.Column(db.Integer, db.ForeignKey('forum_thred.id'),
                         nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
