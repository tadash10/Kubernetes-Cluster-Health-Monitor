# Kubernetes-Cluster-Health-Monitor
# Kubernetes Security Check Script

This Python script allows you to perform a security check on a Kubernetes cluster. It retrieves important information about the cluster, such as Kubernetes version, cluster status, pod status, node status, service status, deployment status, cluster vulnerabilities, and pod resource usage. Additionally, it displays ISO standards related to cloud security.

## Prerequisites

- Python 3.x
- kubectl: Kubernetes command-line tool
- Trivy: Vulnerability scanner (optional, for cluster vulnerability checks)

## Usage

1. Clone the repository or download the script.
2. Ensure that Python 3.x and the required dependencies (kubectl, Trivy) are installed on your system.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using the following command:

   ```shell
   python kubernetes_security_check.py
