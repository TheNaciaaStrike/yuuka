import OSUtils

test = OSUtils.OSUtils()

print(test.get_cpu_temperature())
print(test.get_hostname())
print(test.get_ip_address())
print(test.get_distribution())
print(test.get_memory())
print(test.get_service_status("sshd"))
print(test.get_service_status("postgresql"))
print(test.get_cpu_information())