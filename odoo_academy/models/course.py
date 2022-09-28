from odoo import api, fields, models


class Course(models.Model):
    _name = "academy.course"
    _description = "Course Info"

    name = fields.Char("Title", required=True)
    description = fields.Text(string="Description")

    level = fields.Selection(
        [
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
        ],
        string="Level",
        copy=False,
    )

    active = fields.Boolean('Active', default=True)
