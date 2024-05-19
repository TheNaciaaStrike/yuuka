import os, subprocess

class OSUtils:
    @staticmethod
    def get_cpu_temperature():
        res = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
        return float(res.replace("temp=","").replace("'C\n",""))
    
    @staticmethod
    def get_hostname():
        return os.uname()[1]
    
    @staticmethod
    def get_ip_address():
        return subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True).decode('utf-8').strip()
    
    @staticmethod
    def get_distribution():
        return subprocess.check_output("cat /etc/*-release | grep \"PRETTY_NAME\"", shell=True).decode('utf-8').strip().replace("PRETTY_NAME=","").replace("\"","")
    
    @staticmethod
    def get_cpu_information():
        return subprocess.check_output("lscpu | grep \"Model name:\"", shell=True).decode('utf-8').strip().replace("Model name:","").replace("  ","")

    @staticmethod
    def get_memory():
        return subprocess.check_output("free -m | awk 'NR==2{printf \"Memory: %sMB/%sMB (%.2f%%)\", $3,$2,$3*100/$2 }'", shell=True).decode('utf-8').strip().replace("Memory: ","")

    @staticmethod
    def get_service_status(service):
        status = subprocess.call(['systemctl', 'is-active', service, '--quiet'])
        if status == 0:
            return 'Active'
        else:
            return 'Down'

    @staticmethod
    def get_uptime():
        return subprocess.check_output("uptime -p", shell=True).decode('utf-8').strip().replace('up ','').replace('weeks','W').replace('days','D').replace('hours','H').replace('minutes','M').replace('seconds','S')