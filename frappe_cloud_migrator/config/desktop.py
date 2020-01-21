# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Frappe Cloud Migrator",
			"color": "grey",
			"icon": "octicon octicon-cloud-upload",
			"type": "module",
			"label": _("Frappe Cloud Migrator")
		}
	]
