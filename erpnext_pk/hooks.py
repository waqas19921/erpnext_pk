from . import __version__ as app_version

app_name = "erpnext_pk"
app_title = "Pakistan Workspace"
app_publisher = "ParaLogic"
app_description = "Sales tax reporting and compliance for Pakistan"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@paralogic.io"
app_license = "GNU General Public License (v3)"

before_install = "erpnext_pk.install.before_install"
after_install = "erpnext_pk.install.after_install"
setup_wizard_stages = "erpnext_pk.setup.get_setup_stages"

app_include_js = ["erpnext_pk.bundle.js"]

doctype_js = {
	"Customer": "public/js/customer.js",
	"Supplier": "public/js/supplier.js",
	"Employee": "public/js/employee.js",
	"Company": "public/js/company.js"
}


doc_events = {
	"Customer": {
		"validate": "erpnext_pk.events.validate_ntn_nic_strn_in_document",
	},
	"Supplier": {
		"validate": "erpnext_pk.events.validate_ntn_nic_strn_in_document",
	},
	"Company": {
		"validate": "erpnext_pk.events.validate_ntn_nic_strn_in_document",
	},
	"Employee": {
		"validate": "erpnext_pk.events.validate_ntn_nic_strn_in_document",
	}
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_pk/css/erpnext_pk.css"
# app_include_js = "/assets/erpnext_pk/js/erpnext_pk.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_pk/css/erpnext_pk.css"
# web_include_js = "/assets/erpnext_pk/js/erpnext_pk.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_pk/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_pk.install.before_install"
# after_install = "erpnext_pk.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpnext_pk.uninstall.before_uninstall"
# after_uninstall = "erpnext_pk.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_pk.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"erpnext_pk.tasks.all"
#	],
#	"daily": [
#		"erpnext_pk.tasks.daily"
#	],
#	"hourly": [
#		"erpnext_pk.tasks.hourly"
#	],
#	"weekly": [
#		"erpnext_pk.tasks.weekly"
#	]
#	"monthly": [
#		"erpnext_pk.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "erpnext_pk.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "erpnext_pk.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "erpnext_pk.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"erpnext_pk.auth.validate"
# ]

