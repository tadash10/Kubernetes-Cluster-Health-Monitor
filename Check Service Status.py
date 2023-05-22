def check_service_status():
    command = "kubectl get services --all-namespaces"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip().split("\n")
        print(f"Number of Services: {len(output) - 1}")  # Subtracting header row
        for line in output[1:]:
            fields = line.split()
            namespace = fields[0]
            service_name = fields[1]
            cluster_ip = fields[2]
            external_ip = fields[3]
            print(f"Namespace: {namespace}, Service: {service_name}, Cluster IP: {cluster_ip}, External IP: {external_ip}")
    else:
        print("Failed to retrieve service information.")
