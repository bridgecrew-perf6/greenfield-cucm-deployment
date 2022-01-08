
gateway = {
    'domainName': 'jlr.test.local',
    'description': 'jlr gateway',
    'product': 'Cisco ISR 4321',
    'protocol': 'MGCP',
    'callManagerGroupName': 'Default',
    'units': {
        'unit': []
    }
}

# Create a relatedRegion sub object
unit_name = {
    'index': '0',
    'product': 'ISR-2NIM-MBRD',
    'subunits': {
        'subunit': []
    }
}

subunit_name= {
    'index' : '1',
    'product' : 'NIM-1MFT-T1E1-E1',
    'beginPort': '0'
    }
unit_name['subunits']['subunit'].append( subunit_name )
gateway['units']['unit'].append( unit_name )


# Execute the addRegion request
try:
    resp = service.addGateway( gateway )
except Fault as err:
    print( f'Zeep error: addGateway: { err }' )
    sys.exit( 1 )

print( '\naddRegion response:\n' )
print( resp,'\n' )

input( 'Press Enter to continue...' )