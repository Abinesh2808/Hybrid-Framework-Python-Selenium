import subprocess
from datetime import datetime

d = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

path = r"D:\Users\Abinesh\PycharmProjects\SeleniumFrameworks\DemoWebShop\Reports"

run_command = f"pytest -vs --template=html1/index.html --report={path}/Test_Report_{d}.html --disable-warnings"
subprocess.run(run_command, shell=True)


