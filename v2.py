import subprocess

# ISO Standards
ISO_STANDARDS = {
    "ISO/IEC 27001": "Information Security Management System (ISMS)",
    "ISO/IEC 27017": "Cloud Security",
    "ISO/IEC 27018": "Protection of Personally Identifiable Information (PII) in the Cloud",
    "ISO/IEC 27701": "Privacy Information Management System (PIMS)",
}

def check_kubernetes_version():
    command = "kubectl version --short"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip().split("\n")
        client_version = output[0].split(":")[1].strip()
        server_version = output[1].split(":")[1].strip()
        print(f"Kubernetes Client Version: {client_version}")
        print(f"Kubernetes Server Version: {server_version}")
    else:
        print("Failed to retrieve Kubernetes version.")

def check_cluster_status():
    command = "kubectl cluster-info"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        print("Cluster is running and accessible.")
    else:
        print("Failed to retrieve cluster information.")

def check_pods_status():
    command = "kubectl get pods --all-namespaces"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip().split("\n")
        print(f"Number of Pods: {len(output) - 1}")  # Subtracting header row
        for line in output[1:]:
            fields = line.split()
            namespace = fields[0]
            pod_name = fields[1]
            status = fields[2]
            print(f"Namespace: {namespace}, Pod: {pod_name}, Status: {status}")
    else:
        print("Failed to retrieve pod information.")

def check_node_status():
    command = "kubectl get nodes"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip().split("\n")
        print(f"Number of Nodes: {len(output) - 1}")  # Subtracting header row
        for line in output[1:]:
            fields = line.split()
            node_name = fields[0]
            status = fields[1]
            print(f"Node: {node_name}, Status: {status}")
    else:
        print("Failed to retrieve node information.")

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

def check_cluster_vulnerabilities():
    command = "trivy kubectl --all-namespaces"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Failed to retrieve cluster vulnerability information.")

def check_pod_resource_usage():
    command = "kubectl top pods --all-namespaces"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Failed to retrieve pod resource usage information.")

# Main function
def main():
    print("Kubernetes Security Check:")
    print("-------------------------")
    print("ISO Standards:")
    for standard, description in ISO_STANDARDS.items():
        print(f"{standard}: {description}")
    print("-------------------------\n")
    
    print("Kubernetes Information:")
    print("-----------------------")
    check_kubernetes_version()
    print()
    check_cluster_status()
    print()
    check_pods_status()
    print()
    check_node_status()
    print()
    check_service_status()
    print()
    check_deployment_status()
    print()
    check_cluster_vulnerabilities()
    print()
    check_pod_resource_usage()

if __name__ == "__main__":
    main()
