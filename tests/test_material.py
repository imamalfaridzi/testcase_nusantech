# -*- coding: utf-8 -*-

from odoo.tests import common


class TestMaterial(common.TransactionCase):
    def test_data(self):
        Material = self.env['material']
        partner_id = self.env.ref('base.main_partner')
        test_material_fabric_id = Material.create({
            'code': '101',
            'name': 'Fabric 1',
            'type': 'fabric',
            'buy_price': 200,
            'partner_id': partner_id.id
            })
        test_material_jeans_id = Material.create({
            'code': '201',
            'name': 'Jeans 1',
            'type': 'jeans',
            'buy_price': 300,
            'partner_id': partner_id.id
            })

        test_material_cotton_id = Material.create({
            'code': '301',
            'name': 'Cotton 1',
            'type': 'cotton',
            'buy_price': 150,
            'partner_id': partner_id.id
            })
        self.assertTrue(test_material_fabric_id)
        self.assertTrue(test_material_jeans_id)
        self.assertTrue(test_material_cotton_id)