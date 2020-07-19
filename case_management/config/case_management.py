from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Case Managmement"),
			"items": [
				{
					"type": "doctype",
					"name": "Cases",
					"onboard": 1,
				},
				
			]
		}
		
	]
