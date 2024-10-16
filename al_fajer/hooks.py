from . import __version__ as app_version

app_name = "al_fajer"
app_title = "Al Fajer"
app_publisher = "Asil Gharbia"
app_description = "custom app "
app_email = "aseel.gharbia@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/al_fajer/imgs/1.png"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/al_fajer/css/al_fajer.css"
# app_include_js = "/assets/al_fajer/js/al_fajer.js"
app_include_js = [
    "/assets/al_fajer/js/map_defaults.js",
]


# include js, css files in header of web template
# web_include_css = "/assets/al_fajer/css/al_fajer.css"
# web_include_js = "/assets/al_fajer/js/al_fajer.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "al_fajer/public/scss/website"

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

# Jinja
# ----------


# add methods and filters to jinja environment
# jinja = {
#	"methods": "al_fajer.utils.jinja_methods",
#	"filters": "al_fajer.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "al_fajer.install.before_install"
# after_install = "al_fajer.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "al_fajer.uninstall.before_uninstall"
# after_uninstall = "al_fajer.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "al_fajer.utils.before_app_install"
# after_app_install = "al_fajer.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "al_fajer.utils.before_app_uninstall"
# after_app_uninstall = "al_fajer.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "al_fajer.notifications.get_notification_config"

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
#		"al_fajer.tasks.all"
#	],
#	"daily": [
#		"al_fajer.tasks.daily"
#	],
#	"hourly": [
#		"al_fajer.tasks.hourly"
#	],
#	"weekly": [
#		"al_fajer.tasks.weekly"
#	],
#	"monthly": [
#		"al_fajer.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "al_fajer.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "al_fajer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "al_fajer.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["al_fajer.utils.before_request"]
# after_request = ["al_fajer.utils.after_request"]

# Job Events
# ----------
# before_job = ["al_fajer.utils.before_job"]
# after_job = ["al_fajer.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"al_fajer.auth.validate"
# ]
fixtures = [
    {"dt": "Translation"},
    # {"dt": "Kanban Board"},
    # {"dt": "Custom Field",
    #     "filters": [
    #         [
    #             "name",
    #             "in",
    #             [
                   
    #             ],
    #         ]
    #     ],
    # },
    # {"dt": "Letter Head",
    #     "filters": [
    #         [
    #             "name",
    #             "in",
    #             ["al_fajer"],
    #         ]
    #     ],
    # },
    
   
    # {"dt": "Workflow",
    #     "filters": [
    #         [
    #             "name",
    #             "in",
    #             [
                    
    #             ],
    #         ]
    #     ],
    # },
    # {"dt": "Role",
    #     "filters": [
    #         [
    #             "name",
    #             "in",
    #             [   
                   
                    
    #             ],
    #         ]
    #     ],
    # },    

]

website_context = {
"favicon": "/assets/al_fajer/imgs/1.png",
"splash_image": "/assets/al_fajer/imgs/3.png",}