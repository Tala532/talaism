import time
import random

def detect_fire():
    # Simulate fire detection (True for fire detected, False for no fire)
    return random.choice([True, False])

def additional_verification():
    # Simulate additional verification sources (True for fire confirmed, False for false alarm)
    return random.choice([True, False])

def activate_sprinklers():
    print("Water sprinklers activated!")

def fire_alarm_system():
    print("Monitoring for fire...")
    if detect_fire():
        print("Potential fire detected. Pre-state alarm triggered.")
        verification_time = 60  # Time in seconds for two-step verification

        for remaining in range(verification_time, 0, -1):
            print(f"Waiting for additional verification... ({remaining} seconds left)", end="\r")
            time.sleep(1)

            # Check for additional verification
            if additional_verification():
                print("\nFire confirmed. Activating full alarm and sprinklers.")
                activate_sprinklers()
                break
        else:
            print("\nNo additional verification received. Activating full alarm and sprinklers.")
            activate_sprinklers()
    else:
        print("No fire detected.")

fire_alarm_system()