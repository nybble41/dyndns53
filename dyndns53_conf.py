region = 'us-east-1'

conf = {
   '<username>:<password>': {
      'hosts': {
         '<host.example.com.>': {  # FQDN (don't forget trailing `.`)
            'aws_region': region,  # not actually important
            'zone_id': '<MY_ZONE_ID>',  # same zone ID as in `iam_policy`
            'record': {
               'ttl': 60,  # TTL in seconds; should be low for DDNS
            },
            'last_update': None,  # not currently used
         },
      },
   },
}
