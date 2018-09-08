from app.bp.auth import bp


@bp.route('/user')
def user():
    pass


@bp.route('/login', methods=['GET', 'POST'])
def login():
    pass


@bp.route('/register', methods=['GET', 'POST'])
def register():
    pass
