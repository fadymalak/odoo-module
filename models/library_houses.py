import datetime
from odoo import fields, models , api
from odoo.exceptions import ValidationError

class House(models.Model):
    _name = "library.house"
    _description = "House info"
    house_owner = fields.Char("House owner name")
    room_ids = fields.One2many("library.room","house_id",string="rooms")
    name = fields.Char("Name")

    @api.onchange("house_owner")
    def _onchange_name(self):
        year = datetime.datetime.now().year
        try:
            last = self.search([])[-1].id * 10
            last = int(last) + 10
        except :
            last = 10
        self.name =str(year)+"\\" +str(self.house_owner)+"\\" +str(last)


class Room(models.Model):
    _name = "library.room"
    _description = "House info"
    name = fields.Char("Name")
    num_of_walls = fields.Integer("Number of walls")
    walls_area = fields.Float("Total area of walls")
    total_cost = fields.Float("Total cost of walls")
    house_id = fields.Many2one("library.house")


    @api.onchange("num_of_walls")
    def _onchange_name(self):
        year = datetime.datetime.now().year
        try:
            last = self.search([])[-1].id * 10
            last = int(last) + 10
        except :
            last = 10
        self.name =str(year)+"\\" +str(self.house_id.house_owner)+"\\" +str(last)

class Color(models.Model):
    _name = "library.color"
    _description = "Color"
    name = fields.Char("Name")
    cost_per_meter = fields.Float("Cost of one Meter")    


class Wall(models.Model):
    _name= "library.wall"
    _description = "Wall"

    name = fields.Char("title")
    painter_id = fields.Many2one("res.users",string="painter id")
    length = fields.Float("Length of wall",default = 0)
    width = fields.Float("width of wall",default = 0)
    colors_id = fields.Many2one("library.color",string="Color ")
    total_cost = fields.Float("Cost of this wall")

    @api.onchange("colors_id")
    def _ochange_color(self):
        try:
            color_price = self.colors_id.cost_per_meter
        except :
            color_price = 0

        self.total_cost = self.length * self.width * color_price


