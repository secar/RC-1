#!/usr/bin/env python3
import registry

registry.add_user('81513', 'NTC0394')
registry.add_file('81513', 'porn', '88.58.10.1', '80') 
print(registry.get_bs_addrinfo('81513', 'porn'))
registry.del_file('81513', 'porn')
registry.add_user('daniel', 'gayzolas')
print(registry.auth_user('daniel', 'gayzolass'))
print(registry.auth_user('81513', 'NTC0394'))
