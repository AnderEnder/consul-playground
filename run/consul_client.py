#!/usr/bin/python
import consul
import time
import json

c = consul.Consul()

service = 'example'
service_id = '123'
c.agent.service.register(service,
                         service_id=service_id,
                         port=80,
                         tags=['cool', 'awesome'],
                        )

print(json.dumps(c.agent.services(), indent=True))

# List all registered Services
for x in c.agent.services():
    print(x)

raw_input('Press enter to continue: ')

c.agent.service.deregister(service_id=service_id)
