import platform
import psutil

print("nama sistem operasi: ", platform.system())
print("Versi Sistem Operasi:", platform.version())
print("Arsitektur:", platform.architecture())
print("Nama Host:", platform.node())
print("Versi Python:", platform.python_version())

# Informasi CPU
print("Jumlah CPU:", psutil.cpu_count(logical=True))
print("Frekuensi CPU (MHz):", psutil.cpu_freq().current)

# Informasi RAM
ram = psutil.virtual_memory()
print("Total RAM:", ram.total / (1024 ** 3), "GB")
print("RAM Terpakai:", ram.used / (1024 ** 3), "GB")

# Informasi Disk
disk = psutil.disk_usage('/')
print("Total Disk:", disk.total / (1024 ** 3), "GB")
print("Disk Terpakai:", disk.used / (1024 ** 3), "GB")