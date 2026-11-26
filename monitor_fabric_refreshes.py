import random
import datetime
import time

# Simulate a list of datasets that need refreshing in a Fabric-like environment
DATASETS = [
    "Sales_Dashboard_Data",
    "Inventory_Report_Data",
    "Customer_Analytics_Data",
    "Marketing_Campaign_Data",
    "Financial_Statements_Data",
    "HR_Payroll_Data"
]

# Simulate different types of errors that might occur during a refresh
ERROR_TYPES = [
    "Authentication Failure",
    "Data Source Unavailable",
    "Network Timeout",
    "Processing Error",
    "Gateway Issue",
    "Schema Mismatch"
]

def simulate_refresh(dataset_name):
    """Simulates a single data refresh operation with a chance of failure."""
    timestamp = datetime.datetime.now()
    print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] Attempting refresh for: {dataset_name}...")
    time.sleep(random.uniform(0.5, 2.0)) # Simulate refresh duration

    # Simulate a random chance of failure (e.g., 30% chance)
    if random.random() < 0.3:
        error_type = random.choice(ERROR_TYPES)
        error_message = f"Refresh failed due to: {error_type}"
        return {"status": "FAILED", "error": error_message, "dataset": dataset_name, "timestamp": timestamp}
    else:
        return {"status": "SUCCESS", "dataset": dataset_name, "timestamp": timestamp}

def main():
    print("--- Starting Simulated Fabric Data Refresh Monitoring ---")
    refresh_results = []

    for dataset in DATASETS:
        result = simulate_refresh(dataset)
        refresh_results.append(result)

        # --- This section demonstrates the core monitoring concept --- 
        # In a real Fabric scenario, you would query logs, use Fabric APIs,
        # or integrate with Azure Monitor/Log Analytics to get this status.
        if result["status"] == "FAILED":
            print(f"  !!! ERROR DETECTED for {result['dataset']}: {result['error']}")
            # This is where you'd typically trigger an alert, send a notification,
            # or log to a persistent monitoring system.
        else:
            print(f"  Refresh successful for {result['dataset']}.")
        print("-" * 30)

    print("\n--- Refresh Summary ---")
    successful_refreshes = [r for r in refresh_results if r["status"] == "SUCCESS"]
    failed_refreshes = [r for r in refresh_results if r["status"] == "FAILED"]

    print(f"Total datasets processed: {len(DATASETS)}")
    print(f"Successful refreshes: {len(successful_refreshes)}")
    print(f"Failed refreshes: {len(failed_refreshes)}")

    if failed_refreshes:
        print("\nDetails of Failed Refreshes:")
        for failure in failed_refreshes:
            print(f"- Dataset: {failure['dataset']}")
            print(f"  Error: {failure['error']}")
            print(f"  Timestamp: {failure['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print("  ---")
    else:
        print("\nNo refresh failures detected!")

    print("\n--- Monitoring Complete ---")

if __name__ == "__main__":
    main()
