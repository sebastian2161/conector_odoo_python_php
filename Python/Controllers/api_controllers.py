# -*- coding: utf-8 -*-

from odoo import http
#from odoo import http
#import xmlrpc, xmlrpc.client
from xmlrpc import client
import re
import requests
import werkzeug.urls
import json

CORS = '*'



class Academy(http.Controller):
    # End-Point que busca el id del usuario activo 
    @http.route('/restfulapi/login1', type='json', auth='none', cors=CORS)
    def login02(self, db=None, login=None, password=None, **kw):
        #xmlrpclib = xmlrpc.client
        
        url = 'https://sebastian2161-ejercicio21-rama-v12-3904709.dev.odoo.com'
        db = db
        username = login
        password = password
        
        #return db
         
        common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        #print(common.version())
        try:
            uid = common.authenticate(db, username, password, {})
            return json.dumps({'user_id':uid})
        except:
            return json.dumps({'Error':'Invalid Request'})
        
        
        # End-Point que busca el id del usuario activo 
    @http.route('/restfulapi/login2', auth='none', cors=CORS)
    def login03(self, db=None, login=None, password=None, **kw):
        #xmlrpclib = xmlrpc.client
        
        url = 'https://sebastian2161-ejercicio21-rama-v12-3904709.dev.odoo.com'
        db = db
        username = login
        password = password
        
        #return db
         
        common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        #print(common.version())
        try:
            uid = common.authenticate(db, username, password, {})
            return json.dumps({'user_id':uid})
        except:
            return json.dumps({'Error':'Invalid Request'})