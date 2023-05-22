import subprocess

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

# Main function
def main():
    print("Kubernetes Security Check:")
    check_kubernetes_version()
    print()
    check_cluster_status()
    print()
    check_pods_status()

if __name__ == "__main__":
    main()
