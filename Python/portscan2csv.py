"""

"""
#import
import concurrent
import csv
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from socket import socket

MAX_TRHEADS = 128
TIME_OUT_SECONDS = 5.0
def printUsage():
    print("""
    Usage : 
       - Python3 fileName.py <host> <output_file>
     example :     
       - python3 portscan2csv.py www.google.com file.csv
       - python3 portscan2csv.py 8.8.8.8 file.csv
    """)

#Check arguments
def check_args():
    if len(sys.argv) < 3:
        print("\n[-] No enough arguments receive.")
        printUsage()
        sys.exit(1)

def tcp_connect(host,port):

    sock = socket()
    sock.settimeout(TIME_OUT_SECONDS)

    try:
        sock.connect((host, port))
        connected = True
        sock.close()

    except:
        connected = False
    return connected




if __name__ == '__main__':

    check_args()
    host = sys.argv[1] #Given a host

    output_file = sys.argv[2]
    scan_results = {} #dict

    # Open CSV file for writing, output headers
    spreadsheet = csv.writer(open(output_file, 'w'), delimiter=',')

    # Scan all ports 1-65535 TCP connect
    # Multithreaded
    #Scan all ports 1-65535 TCP connect
    with ThreadPoolExecutor(max_workers = MAX_TRHEADS) as executor:

        future_result = {executor.submit(tcp_connect, host, port): port for port in range(1,65535+1)}
        for future in concurrent.futures.as_completed(future_result):
            port = future_result[future]
            try:
                did_connect = future.result()
                #scan_results[port]=did_connect
                # add_csv row(host,post,did_connect)
                try :
                    spreadsheet.writerow([
                        host,
                        str(port),
                        str(did_connect),
                        str(datetime.now())
                    ])
                except Exception as e:
                    print("[-] error writing to spreadsheet %s." %e)
                if did_connect:
                    print("[+] %d connected " % port)
            except Exception as e:
                print("Error pulling result from future %s " % e)





        #for port, result in scan_results.items() :


        #close csv





   # Output results to a CSV









   #https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html