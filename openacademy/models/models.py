# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Model to store Courses'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

class Professor(models.Model):
    _name = 'openacademy.professor'
    _description = 'Model to store professors'

    name = fields.Char(string="Name", required=True)
    description = fields.Text()