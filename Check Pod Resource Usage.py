def check_pod_resource_usage():
    command = "kubectl top pods --all-namespaces"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Failed to retrieve pod resource usage information.")
