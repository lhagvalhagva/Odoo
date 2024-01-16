
from odoo import http


class AaCustomSaleOrderModule(http.Controller):
    @http.route('/aa_custom_sale_order_module/aa_custom_sale_order_module', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/aa_custom_sale_order_module/aa_custom_sale_order_module/objects', auth='public')
    def list(self, **kw):
        return http.request.render('aa_custom_sale_order_module.listing', {
            'root': '/aa_custom_sale_order_module/aa_custom_sale_order_module',
            'objects': http.request.env['aa_custom_sale_order_module.aa_custom_sale_order_module'].search([]),
        })

    @http.route('/aa_custom_sale_order_module/aa_custom_sale_order_module/objects/<model("aa_custom_sale_order_module.aa_custom_sale_order_module"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('aa_custom_sale_order_module.object', {
            'object': obj
        })
