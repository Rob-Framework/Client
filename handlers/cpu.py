import psutil
from tcpServer import getTCPServer as getServer

def getCPUUsage():
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    cpu = str(cpu)
    
    data = {
        "cpu": cpu
    }
    getServer().sendSensorData("cpu_usage", data)