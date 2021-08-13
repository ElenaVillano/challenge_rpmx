from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, fields
from werkzeug.utils import cached_property

import yaml

# String de coneccion a la base de datos
with open('../../conf/local/credentials.yaml', 'r') as f:
    config = yaml.safe_load(f)

db_conn_str = config['db']
link = "postgresql://" + db_conn_str['user'] + ":" + db_conn_str['password'] + "@" + db_conn_str['host'] + ":" + str(
    db_conn_str['port']) + "/" + db_conn_str['dbname']

# Create Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = link
api = Api(app)

# con esto ya entras a la base de datos
db = SQLAlchemy(app)


# Tabla deploy.mockup match _api
# Mapeo de la tabla db
class Match(db.Model):
    #__table_args__ = {'schema': 'api'}  # schema
    __tablename__ = 'predicciones'  # tabla del esquema

    y_test = db.Column(db.Integer)
    proba_fraude = db.Column(db.Float)
    y_pred = db.Column(db.Integer)
    id_user = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    order_txn = db.Column(db.Integer, primary_key=True)

# Swagger model for mashalling outputs
model = api.model('resultados', {
    'y_test': fields.Integer,
    'proba_fraude': fields.Float,
    'y_pred': fields.Integer,
    'id_user': fields.Integer,
    'order_txn': fields.Integer
})

# Final output inspection_id: '',results: [ ]
model_list = api.model('endpoint1_output', {
    'fecha': fields.Date,
    'resultados': fields.Nested(model)
})

#model_2 = api.model('resultados', {
#    'id_user': fields.Integer,
#    'y_test': fields.Integer,
#    'y_pred': fields.Integer
#})

# Final output inspection_id: '',results: [ ]
#model_list_2 = api.model('endpoint_2_output', {
#    'date': fields.Date,
#    'resultados': fields.Nested(model_2)
#})


@api.route('/endpoint1/<fecha>')
class ShowMatch(Resource):
    @api.marshal_with(model_list, as_list=True)
    def get(self, fecha):
        match = Match.query.filter_by(fecha=fecha).all()
        resultados = []
        for element in match:
            resultados.append({'y_test': element.y_test,
                               'proba_fraude': element.proba_fraude,
                               'y_pred': element.y_pred,
                               'id_user': element.id_user,
                               'order_txn': element.order_txn})
        return {'fecha': fecha, 'resultados': resultados}


#@api.route('/endpoint2/<date>')
#class ShowMatch(Resource):
#    @api.marshal_with(model_list_2, as_list=True)
#    def get(self, date):
#        match = Match.query.filter_by(date=date).all()
#        resultados = []
#        for element in match:
#            resultados.append({'license_id': element.license_id,
#                               'label_value': element.label_value,
#                               'probability': element.probability})
#        return {'date': date, 'resultados': resultados}


if __name__ == '__main__':
    app.run(debug=True)
