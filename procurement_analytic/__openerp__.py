# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#             <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    "name": "Procurement Analytic Account link",
    "version": "1.0",
    "author": "Eficent",
    "website": "www.eficent.com",
    "category": "Purchase Management",
    "depends": ["analytic", "procurement", "stock_analytic_account"],
    "description": """
Procurement Analytic Account link
====================================
    Stores the analytic account in the procurement order.

    """,
    "init_xml": [],
    "update_xml": [    
        "view/procurement_view.xml",
        "view/analytic_account_view.xml",
    ],
    'demo_xml': [

    ],
    'test':[
    ],
    'installable': True,
    'active': False,
    'certificate': '',
    'application': True,
}
