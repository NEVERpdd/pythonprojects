import subprocess
#comand controll

try:
    output = subprocess.Popen('ifconfig', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = output.communicate()
    saida = stdout.decode(encoding='latin-1')
    
    if not saida:  
        raise ValueError("Saída vazia")    
    
    print(saida)

except:
    output = subprocess.Popen('ipconfig', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = output.communicate()
    saida = stdout.decode(encoding='latin-1')
    print(saida)