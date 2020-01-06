
import java.net.Socket;
import java.net.InetSocketAddress;
import java.io.IOException;


/*
   Run :
     - Method :
        - javac Portscan.java
        - java Portscan (name of the class )
        - for this code :
           - java Portscan <host>(www.google.com or 192.168.224.1)
           - time java Portscan <host>(www.gmail.com or 4.4.4.4)
     - Other method :
       - alias run='javac Portscan.java; java Portscan';
       - run
       - for this code :
          - run <host>(www.youtube.com or 8.8.8.8)
          - time run <host>(www.facebook.com or 157.548.123.2)
*/
class Portscan {

    private static void printUsage(){
      System.out.println("Usages : ");
      System.out.println("  Java Portscan <host>>");
      System.out.println("Examples : ");
      System.out.println("  Java Portscan 127.0.0.1");
      System.out.println("  Java Portscan www.google.com");

    }

    private static void checkPort(String host, Integer portNumber){
      //open a socket,
     // connect to host/post
     //()->
     Integer timeout = 3000;
     Thread thread = new Thread(()->{
       Socket clientSocket = new Socket();
       try {
          clientSocket.connect(new InetSocketAddress(host, portNumber), timeout);
          System.out.printf("[-] %d connected %s ",portNumber,host);
          clientSocket.close();
       }catch (IOException e) {

       }
     });
     thread.start();

    }

    // public static void main function
    public static void main(String [] args){
        // args.length == 0 display printUsage() info
        if (args.length == 0){
          System.out.println("No arguments received.");
          printUsage();
          System.exit(1);
        }
        // else display this info
        String host = args[0];
        System.out.println(args);
        System.out.println(host);
        System.out.printf("Scanning %s now ... \n", host);

        //port 1-65535
        // open TCP connection
        for(Integer portNumber=0; portNumber<=65535; portNumber++){
           checkPort(host, portNumber);
        }
    }
}

// alias run='javac Portscan.java; java Portscan'
// echo $?
// 41:11
