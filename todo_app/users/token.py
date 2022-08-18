from todo_app import db,login_manager,app
from itsdangerous import URLSafeSerializer
from todo_app.models import User

def get_token(self):
    s = URLSafeSerializer(app.config['SECRET_KEY'])
    return s.dumps({'user_id': self.id})

#@staticmethod
def verify_token(token, expiration=120):
    s = URLSafeSerializer(app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token,max_age=expiration)['user_id']
    except:
        return None
    return User.query.get(user_id)
