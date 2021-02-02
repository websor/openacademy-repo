# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

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
    datetime_test = fields.Datetime(default=fields.Datetime.now)
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string='Instructor', domain=[('instructor','=',True)])
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', 
                            string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner',string="Attendees")
    taken_seats = fields.Float(compute='_taken_seats')
    active = fields.Boolean(default=True)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats = 0
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            self.active = False
            return {
                'warning':{
                'title': "Incorrect 'seats' value",
                'message': "The number of available seats may not be negative",
                }
            }
        if self.seats < len(self.attendee_ids):
            self.active = False
            return  {
                'warning':{
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendee",
                }
            }
        self.active = True

    #Restrictivo
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for record in self.filtered('instructor_id'):
            if record.instructor_id in record.attendee_ids:
                raise exceptions.ValidationError("A session instructor can't be")