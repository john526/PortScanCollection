package main

import (
	//"fmt"
	"log"
	"net"
	"os"
	"strconv"
	"time"
)

func printUsage() {
	log.Println("Usage : ")
	log.Println("  go run fileName.go <host>")
	log.Println("Example : ")
	log.Println("  go run portScan.go www.google.com")
	log.Println("  go run portScan.go 8.8.8.8")
}

func testTcpConnect(host string, port int, doneChannel chan bool) {

	timeoutLength := 5 * time.Second
	conn, err := net.DialTimeout("tcp ", host+": "+strconv.Itoa(port), timeoutLength)

	if err != nil {
		doneChannel <- false
		return
	}
	conn.Close()
	log.Printf("[+] %d connected ", port)
	doneChannel <- true
}

func main() {

	if len(os.Args) == 1 {
		log.Println("No arguments received.")
		printUsage()
		os.Exit(1)
	}
	// Take a host from args1
	// if no args provided, print usage
	// host = args1

	// for ports 1-65535
	//   go testTcpConnect()

	doneChannel := make(chan bool)
	activeThreadCount := 0
	log.Println("Scanning host : " + os.Args[1])
	for portNumber := 1; portNumber <= 65535; portNumber++ {
		activeThreadCount++
		go testTcpConnect(os.Args[1], portNumber, doneChannel)
	}

	for {
		<-doneChannel
		activeThreadCount--
		// log.Printf("Reducing threadAcount %d ", activeThreadCount)
		if activeThreadCount == 0 {
			break
		}
	}
	log.Println("Done.")
	// until activeThreadCount == 0 keep checking
	//

}
