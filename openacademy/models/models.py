# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Model to store Courses'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one(
        'res.users', string="Responsible",
        index="true", ondelete='set null'
    )
    
    sessions_ids = fields.One2many('openacademy.session', 'course_id')

class Professor(models.Model):
    _name = 'openacademy.professor'
    _description = 'Model to store professors'

    name = fields.Char(string="Name", required=True)
    description = fields.Text()

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', 
                            string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner',string="Attendees")
