{
    "name": "Flet vehicles maintenance",
    "summary": "Management of fleet vehicles maintenance plans.",
    "version": "14.0.1.0.0",
    "author": "Javier L. de los Mozos",
    "website": "",
    "license": "AGPL-3",
    "category": "Fleet",
    "depends": ["fleet","web_domain_field","fleet_vehicle_log_fuel", "uom"],
    "data": [
        "data/res_partner_data.xml",
        "views/fleet_vehicle_views.xml",
        "views/fleet_vehicle_model_views.xml",
        "views/fleet_maintenance_plan_views.xml",
        "views/fleet_log_services_views.xml",
        "views/fleet_service_type_views.xml",
        "security/ir.model.access.csv",
#        "security/security.xml",
        "data/unit_data.xml",
        "data/service_type_data.xml",
        "data/scheduler.xml",
        "data/activity_data.xml"
    ],
    "installable": True,
}
