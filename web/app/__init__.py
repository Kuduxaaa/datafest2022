# -*- coding: utf-8 -*-
# Coded By Kuduxaaa

import config

from flask import Flask, render_template
from flask_restful import Api

app = Flask(__name__, 
            template_folder='views',
            static_folder='public')


app.config.from_object(config.DevelopmentConfig)
api_router = Api(app, prefix = config.Config.API_PREFIX)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', error=e), 404


from app.controllers import main
from app.api import ping
from app.api import data

api_router.add_resource(ping.Ping, '/ping')
api_router.add_resource(data.Data, '/data')
app.register_blueprint(main.bp)
