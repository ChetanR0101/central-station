from email.policy import default
from xmlrpc.client import Boolean
from odoo import models,fields,api
from odoo.exceptions import ValidationError

class CentralStation_substation(models.Model):
    _name= "central.substation"
    _description="Central Station - SubStation"
    name= fields.Char("SubStation Name")
    price=fields.Float("Fuel Price")


class CentralStation_transection_in(models.Model):
    _name= "central.transection_in"
    name= fields.Char("Recived By")
    date= fields.Datetime("Date")
    fuel_type= fields.Many2one(string="Fuel Type", comodel_name="central.data")
    sub_station=fields.Many2one(string="SubStation Name", comodel_name="central.substation")
    instock_qut=fields.Float("InStock Qut")

class CentralStation_transection_out(models.Model):
    _name= "central.transection_out"
    name=fields.Char("Customer Name")
    date=fields.Datetime("Date")
    fuel_type=fields.Many2one(string="Fuel Type", comodel_name="central.data")
    sub_station=fields.Many2one(string="SubStation Name", comodel_name="central.substation")
    order_qut=fields.Float("Fuel Quantity")
    price=fields.Float("Fuel Price")
    total_price=fields.Float("Total Cost")

    

class CentralStation_data(models.Model):
    _name= "central.data"
    name=fields.Char("Fuel Type")
    substation_name=fields.Many2one(string="SubStation Name", comodel_name="central.substation")
    fuel_qut= fields.Float("Fuel Quantity")
    price=fields.Float("Fuel Price")

class CentralStation_tanker(models.Model):
    _name="central.tanker"
    name= fields.Char("Tanker No.")
    starting_pt= fields.Char(string="Source", default="Central Station")
    dest= fields.Many2one(string="Destination", comodel_name="central.substation")
    fuel_type= fields.Many2one(string="Fuel Type", comodel_name="central.data")
    vol=fields.Float("Volume Carried")
    status=fields.Selection([("dispatch", "Dispatched"),("on_way","On the Way"),("delivered","Delivered"),("late","Delayed")] ,string="Tanker Status", default="dispatch" ,required=True)


#  SubStation Models
class CentralStation_substation1(models.Model):
    _name= "central.substation1"
    name= fields.Char("Manager Name")


class CentralStation_substation1(models.Model):
    _name= "central.substation2"
    name= fields.Char("Manager Name")


class CentralStation_substation1(models.Model):
    _name= "central.substation3"
    name= fields.Char("Manager Name")
