import threading
import speedtest


def download_speed(speed, value_download):
    # Measure the download speed using the Speedtest module
    speed.download()

    # Convert download speed to megabits per second (Mbps)
    download = int(speed.download() / 800000)
    print(f"Downloading speed: {download} Mbps")

    # Update the first element of the 'value_download' list with the download speed
    value_download[0] = download


def upload_speed(speed, value_upload):
    # Measure the upload speed using the Speedtest module
    speed.upload()

    # Convert upload speed to megabits per second (Mbps)
    upload = int(speed.upload() / 800000)
    print(f"Uploading speed: {upload} Mbps")

    # Update the first element of the 'value_upload' list with the upload speed
    value_upload[0] = upload


def testSpeed():
    print("Checking internet speed...")

    # Create an instance of the Speedtest class from the speedtest module
    speed = speedtest.Speedtest()

    # Initialize a list to store the download speed
    value_download = [0]

    # Initialize a list to store the upload speed
    value_upload = [0]

    # Create two threads for download and upload speed tests
    download_thread = threading.Thread(target=download_speed, args=(speed, value_download))
    upload_thread = threading.Thread(target=upload_speed, args=(speed, value_upload))

    # Start both threads
    download_thread.start()
    upload_thread.start()

    # Wait for both threads to finish
    download_thread.join()
    upload_thread.join()

    # Return the download and upload values stored in the list
    return value_download[0], value_upload[0]


# Example usage
testSpeed()
