from flask import *
from database import init_db
from controllers.__init__ import *

app = Flask(__name__)
app.register_blueprint(viagens_controller)
app.register_blueprint(index_controller)
app.register_blueprint(passageiros_controller)
#app.register_blueprint(admin_controller)
#app.register_blueprint(reserva_controller)
app.secret_key = '1234566789'
if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)