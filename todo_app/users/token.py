from todo_app import db,login_manager,app

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from todo_app.models import User


def get_token(self, expires_sec=600):
    s = Serializer(app.config['SECRET_KEY'], expires_sec)
    return s.dumps({'user_id': self.id}).decode('utf-8')

# @staticmethod
def verify_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token)['user_id']
    except:
        return None
    return User.query.get(user_id)
