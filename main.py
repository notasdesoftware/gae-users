#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.api import users


class AdminZone(webapp2.RequestHandler):
    def get(self):
        self.response.write("<html><body>")
        self.response.write("<h1>Zona de administrador</h1>")
        self.response.write("<p>Administrador: %s</p>" % users.is_current_user_admin() )
        self.response.write("<a href='/profile'>Perfil de usuario</a>")
        self.response.write("<p><a href='%s'>Cerrar sesión</a> </p>" % users.create_logout_url('/'));
        self.response.write('</body></html>')


class UserZone(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        self.response.write("<html><body>")
        self.response.write("<h1>Perfil de usuario</h1>")
        self.response.write('<p><a href="/">&#60;&#60; Zona pública</a></p>');
        self.response.write("<p>Solo se puede estar en esta sección si se ha iniciado sesión</p>")
        self.response.write("<p>Email: %s</p>" % user.email())
        self.response.write("<p>ID de usuario: %s</p>" % user.user_id())
        self.response.write("<p>Nickname: %s</p>" % user.nickname())
        self.response.write("<p>Dominio: %s</p>" % user.auth_domain())
        self.response.write("<p><a href='%s'>Cerrar sesión</a> </p>" % users.create_logout_url('/'));
        self.response.write('</body></html>')


class PublicZone(webapp2.RequestHandler):
    def get(self):
        self.response.write("<html><body>")
        self.response.write("<h1>Zona pública</h1>")
        self.response.write("<p>Cualquier persona puede estar en esta sección.</p>")
        self.response.write("<ul>"
                                "<li><a href='/profile'>Perfil de usuario</a></li>"
                                "<li><a href='/admin'>Zona de administrador</a></li>"
                            "</ul>")
        self.response.write('</body></html>')
 
app = webapp2.WSGIApplication([
    ('/', PublicZone),
    ('/profile', UserZone),
    ('/admin', AdminZone)
], debug=True)
