{
    'name': 'Fleet Vehicle Print Barcode label',
    'version': '10.0.1.0',
    'category': 'Managing vehicles and contracts',
    'sequence': 110,
    'summary': "Print barcode label for fleet vehicle",
    'description':"Print barcode label for fleet vehicle, this works for v10, v9, v8. You find the print button beside Action button on the top of fleet vehicle form. In the system parameter, you shall add key report.url  and value is http://localhost:8069, key webkit.path and value is http://localhost:8069",
    'author': 'Stella Fredö in Sweden',
    'website': 'http://se.linkedin.com/in/stella-fredö-94401014',
    'depends': ['fleet'],
    'data': [
        'views/fleet_report.xml',
        'fleet_vehicle_report.xml',
    ],
    'installable': True,
    'auto_install': False,
}


