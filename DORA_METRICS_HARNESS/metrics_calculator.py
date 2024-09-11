from datetime import datetime

def calculate_lead_time(deployments):
    lead_times = []
    for deployment in deployments:
        build_time = deployment['build_start_time']  # Epoch timestamp
        deploy_time = deployment['deploy_end_time']  # Epoch timestamp
        lead_time = (deploy_time - build_time) / 1000  # Convert to seconds
        lead_times.append(lead_time)
    average_lead_time = sum(lead_times) / len(lead_times) if lead_times else 0
    return average_lead_time

def calculate_mttr(deployments):
    recovery_times = []
    for deployment in deployments:
        if deployment['status'] == 'failed':  # If the deployment failed
            failure_time = deployment['failure_time']
            recovery_time = deployment['recovery_time']
            mttr = (recovery_time - failure_time) / 1000  # Convert to seconds
            recovery_times.append(mttr)
    average_mttr = sum(recovery_times) / len(recovery_times) if recovery_times else 0
    return average_mttr

def calculate_failure_rate(deployments):
    failed_deployments = [d for d in deployments if d['status'] == 'failed']
    failure_rate = (len(failed_deployments) / len(deployments)) * 100
    return failure_rate

def calculate_deployment_frequency(deployments):
    return len(deployments)

def calculate_metrics(deployments):
    metrics = {}
    metrics['Deployment Frequency'] = calculate_deployment_frequency(deployments)
    metrics['Average Lead Time for Changes (seconds)'] = calculate_lead_time(deployments)
    metrics['MTTR (seconds)'] = calculate_mttr(deployments)
    metrics['Change Failure Rate (%)'] = calculate_failure_rate(deployments)
    return metrics
