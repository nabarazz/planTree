
import string
from odoo import fields, models, _, api
from odoo.exceptions import ValidationError

class MyModel(models.Model):
   _name = "my.model"
   # _inherit = 'res.users'
   _description = "My model example"
   reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))

   form_id = fields.Integer('सामाजिक परिचालकको नम्बर')
   nam = fields.Char('सामाजिक परिचालिकको नाम')
   district = fields.Char("district")
   village_municipated = fields.Char('गाउँपालिकाको नाम')

   president= fields.Char('वडा अध्यक्षको नाम')
   mobile_number= fields.Char('फोन नम्बर')
   emp_postion = fields.Char('पद')
   
   description= fields.Char('सहभागी प्रतिक्रिया बिवरण')
   training_group_name= fields.Char('तालिम प्राप्त समुहको नाम')
  
   date= fields.Date('मिति')
   total_soap = fields.Integer('उत्पादन साबुनको संख्या')
   lunch_expenses = fields.Float('खाजा खर्च')
   related_field_president = fields.Char('परियोजना समूहको अध्यक्षको नाम')
   mobile_number_1= fields.Char('फोन नम्बर')
   treasurer_name = fields.Char('कोषाध्यक्षको नाम')
   treasurer_mobile = fields.Char('कोषाध्यक्षको फोन नम्बर')
   secretary_name = fields.Char('सचिबको नाम')
   codinator_name = fields.Char('उत्पादन संयोजक नाम')
   machine = fields.Boolean('तालिम प्राप्त समूहलाई मेशिन')
   not_machine = fields.Boolean('तालिम प्राप्त समूहलाई मेशिन छैन')
   
   total_fee = fields.Float('total fee', compute='_amount_all')
   
   line_ids = fields.One2many('my.model.line', 'my_id', 'Lines')

  
   @api.depends('line_ids.price_total')
   def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            total_fee  = 0.0
            for line in order.line_ids:
                total_fee += line.price_total
                
            order.update({
                
                'total_fee': total_fee,
            })
   
      
   
   
   @api.model
   def create(self, vals):
      if vals.get('reference', _('New')) == _('New'):
         vals['reference'] = self.env['ir.sequence'].next_by_code('my.model') or _('New')
      res = super(MyModel, self).create(vals)
      return res

   def name_get(self):
        result = []
        for rec in self:
            name = rec.reference 
            result.append((rec.id, name))
        return result


   
   
      
   @api.constrains('mobile_number')

   def _check_mobile_number(self):

      for rec in self:

         if rec.mobile_number and len(rec.mobile_number) != 10:

             raise ValidationError(_("mobile number validation error"))

      return True


class MyModelLine(models.Model):

   _name = "my.model.line"
   
   _rec_name = 'name'
   

   
   _description = "My model line example"

  
   name = fields.Many2one('res.partner', 'सीप प्राप्त सदस्यको नाम')
   
   tole_name = fields.Char('पालिकाकोनाम/वडा.नम्बर/टोल')
   phone_num = fields.Char('फोन नम्बर')
   physically_disable = fields.Boolean('अपाङ्ग संख्या')
   form_fee = fields.Float('फारम शुल्क')
   sum_assured = fields.Char('Sum Assured')
   term = fields.Integer('Term')
   total_amount = fields.Float('Total Amount', compute='_total_amount')
   insurance_policy_no = fields.Integer('Insurance No')
   next_program_join_member = fields.Char('अर्को तालिम लिने इच्छुक')
   certificate = fields.Boolean('Certificate')
   display_type = fields.Char(string="Insurance Type")
   term = fields.Selection(
       [
        ('1','1'),
        ('2','2'), 
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'), 
        ('13','13'),
        ('14','14'),
        ('15','15'),
        ('16','16'),
        ('17','17'),
        ('18','18'),
        ('19','19'),
        ('20','20'),
        ], default='1', string='Term')
   insurance_type = fields.Many2many('insurance.type', 'display_type', string="insurance_type")
   premium_acount = fields.Float('Premium Amount')
   sum_assort = fields.Float('Sum Assort')
   price_total = fields.Float(compute='_compute_amount', string='Total', store=True)

   my_id = fields.Many2one('my.model', 'Lines Model')
   sequence = fields.Integer()

   
   @api.depends('form_fee', 'premium_acount')
   def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            total = line.form_fee 
            line.update({
                
                'price_total': total,
                
            })


   @api.constrains('phone_num')

   def _check_phone_num(self):

      for rec in self:

         if rec.phone_num and len(rec.phone_num) != 10:

             raise ValidationError(_("mobile number vaidation error"))

      return True

   
         


class insuranceType(models.Model):
   _name = "insurance.type"
   _rec_name = 'display_type'
   display_type = fields.Char(string="Insurance Type")
   
   

   
  
    