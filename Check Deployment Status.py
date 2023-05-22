def check_deployment_status():
    command = "kubectl get deployments --all-namespaces"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip().split("\n")
        print(f"Number of Deployments: {len(output) - 1}")  # Subtracting header row
        for line in output[1:]:
            fields = line.split()
            namespace = fields[0]
            deployment_name = fields[1]
            replicas = fields[2]
            available_replicas = fields[3]
            ready_replicas = fields[4]
            print(f"Namespace: {namespace}, Deployment: {deployment_name}, Replicas: {replicas}, Available: {available_replicas}, Ready: {ready_replicas}")
    else:
        print("Failed to retrieve deployment information.")
