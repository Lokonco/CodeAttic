import java.io.BufferedReader; //Used to read data from request
import java.io.IOException; // Error handling
import java.io.InputStreamReader; //Allows us to turn bytes into chars
import java.net.ServerSocket; //Used to receive connections
import java.net.Socket; //Used to send & receive data from client
import java.util.Date; //Used to send simple request data

public class HttpServer {
    public static void main(String[] args) throws IOException {
        //Create const Socket to port 8080
        final ServerSocket server = new ServerSocket(8080);
        System.out.println("Listening for Connection on Port:8080");

        //Continue webserver
        while (true){

            //Socket clientSocket = server.accept()
            //will allow us to accept connection using a blocking method
            //to make sure connection is made first before starting something else
            Socket clientSocket = server.accept();

            try {
                //1- Read HTTP request from client socket
                InputStreamReader isr = new InputStreamReader(clientSocket.getInputStream());
                BufferedReader reader = new BufferedReader(isr);
                String line = reader.readLine();

                //Print headers
                while (!line.isEmpty()) {
                    System.out.print(line);
                    line = reader.readLine();
                }
                //Create a simple request / today's date for example
                Date today = new Date();
                String httpResponse = "HTTP/1.1 200 OK\r\n" +
                        "Content-type: text/plain\r\n" +
                        "\r\n" + today;

                //Send the request to the client
                clientSocket.getOutputStream().write(httpResponse.getBytes("UTF-8"));

            } finally { //Close the socket
                clientSocket.close();
            }
        }
    }
}
