#(Using Trivy):
def check_cluster_vulnerabilities():
    command = "trivy kubectl --all-namespaces"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Failed to retrieve cluster vulnerability information.")
