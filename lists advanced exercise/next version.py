initial_version = list(input().split('.'))
version_number = int(''.join(initial_version))
version_number += 1
new_version = '.'.join(str(version_number))
print(new_version)