# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		# Modules
		{
			"module_name": "Case Management",
			"color": "grey",
			"icon": "icon case-blue",
			"type": "module",
			"label": _("Case Management")
		}
	]
