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
