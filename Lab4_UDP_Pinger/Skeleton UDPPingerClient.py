# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments
host = input('Input hostname: \n') # FILL IN START		# FILL IN END
port = int(input('Input port: \n'))# FILL IN START		# FILL IN END
timeout = 1 # in seconds

# Create UDP client socket
# FILL IN START
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)
# FILL IN END


# Sequence number of the ping message
ptime = 0

# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description
    data = input('Input lowercase sentence: \n')# FILL IN START		# FILL IN END

    try:
    	# FILL IN START

    	# Record the "sent time"
        sent_time = time.time()
    	# Send the UDP packet with the ping message
        clientSocket.sendto(data.encode(), (host, port))
    	# Receive the server response
        modifiedData, ServerAddress = clientSocket.recvfrom(2048)
    	# Record the "received time"
        rec_time = time.time()
    	# Display the server response as an output
        print("Server Response: ", modifiedData.decode())
    	# Round trip time is the difference between sent and received time
        RTT = rec_time - sent_time
        print("RTT: ", RTT)

        # FILL IN END
    except:
        # Server does not response
	# Assume the packet is lost
        print("Request timed out.")
        continue

# Close the client socket
clientsocket.close()
