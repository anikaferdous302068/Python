def shutdown():
 intent=input("Are you sure you want to shut down the system? (yes/no): ")
 if intent == 'yes':
    print("Shutting down the system...")
    # Add actual shutdown code here

 else:
    print("Shutdown canceled.")
shutdown()