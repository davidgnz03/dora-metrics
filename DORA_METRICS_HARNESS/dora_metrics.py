from harness_api import get_deployments
from metrics_calculator import calculate_metrics

def main():
    print("Starting DORA metrics extraction from Harness...")

    # Fetch deployments from the Harness API
    deployments = get_deployments()

    if deployments:
        # Calculate DORA metrics
        dora_metrics = calculate_metrics(deployments)
        print("\nCalculated DORA Metrics:")
        for key, value in dora_metrics.items():
            print(f"{key}: {value}")
    else:
        print("No deployments found.")

if __name__ == "__main__":
    main()
