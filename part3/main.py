from socket import *  # it is not same as import socket, if you use import socket you need to add a prefex to the function you want to use (socket.function)

host = '0.0.0.0'  # (no particular adress place holder)special ip address that means "any" or "all available interfaces." and also means I want to listen on all available IP addresses//all adresses on local network can accses server including the local machine// It makes the server accessible from any network interface.
# A network interface is a connection point for connecting the computer to a network, and a machine can have multiple network interfaces (such as Ethernet, Wi-Fi,llopback,
# interface: a point of connection between computer and network
# 127.0.0.1(loopback adress) it is used to connect to aserver running on a local machine and accept connection from local machine. it only listen to loopback interface
serverPort = 9966  # Port number
serverSocket = socket(AF_INET, SOCK_STREAM)  # TCP socket for incoming request
serverSocket.bind(("",
                   serverPort))  # the server port number "serverPort" with this socket//empty ip address has the same meaning as 0.0.0.0
serverSocket.listen(
    1)  # The server listen for TCP connection requests  with 1 queued connections.//1 is the number of connections the socket can handle#bind=address is created
print("The web server is ready to receive")  # Print a message to tell  server is ready.

while True:
    connectionSocket, addr = serverSocket.accept()  # When a client sends a TCP connection request create "connectionSocket"
    sentence = connectionSocket.recv(
        1024).decode()  # the method .recv(1024) reseves a msg from client and the argument declares the max amount of data reseved ,but client can send less than that
    print(
        addr)  # client address and it is made of two pats:client ip address,port number used by the client for this connection
    print(sentence)  # the msg reseved from client
    # how did you split it?
    ip = addr[0]  # htos will be the client ip address
    port = addr[1]  # this is the port number that the client is usin for connection
    # how did you know that the object will be at [1]?
    object = sentence.split()[
        1]  # Get the reqested object from client//the object requested is the second word of the scentence
    print("\nThe HTTP request is:\n", object)  # print the HTTP request//this messag will apear on server side only

    if (
            object == '/' or object == '/index.html' or object == '/main_en.html' or object == '/en'):  # if statement checks what is the requested object
        # this is an http status line it is a common response when a requested resource is found, and the server is able to successfully fulfill the request
        # Status codes are three-digit numbers that indicate the result of the HTTP request
        connectionSocket.send(
            "HTTP/1.1 200 OK \r\n".encode())  # 1.1 is used http protocol vs //it sends an HTTP response with a "200 OK" wich is a status code that means:received, understood, and processed successfully
        # http msg header that sets the content type to HTML with a character set of UTF-8// character set of UTF-8 covers almost all characters and symbols in the world
        connectionSocket.send(
            "Content-Type: text/html;charset=UTF-8\r\n".encode())  # send the HTML file// \r\n is used as a line ending sequence and  is used to delimit lines in HTTP messages, including the HTTP request and response headers and  to ensure compatibility between systems and they make it easier to interpret the message correctly.
        connectionSocket.send(
            "\r\n".encode())  # and an additional \r\n sequence indicates the end of the headers section in the HTTP response
        file1 = open("main_en.html",
                     "rb")  # server should send main_en.html file//this function will open the html file in binary mode so the content will be red in bytes
        connectionSocket.send(
            file1.read())  # read the file that was open//read the file then send its content in a binary stream


    elif (object == '/ar'):  # If object '/ar', it will send the same HTTP status code and content type,
        # but will serve the contents of the file "main_ar.html" instead. --> (sending a similar HTTP response with a different HTML file as the body).
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file2 = open("main_ar.html", "rb")
        connectionSocket.send(file2.read())

    elif (object.endswith(
            '.html')):  # If the object ends with '.html', the server sends an HTTP response with a 200 OK status and a Content-Type
        # The server then opens the file "l1.html" and sends its contents as the response body.
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=UTF-8 \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file3 = open("l1.html", "rb")
        connectionSocket.send(file3.read())

    elif (object.endswith('.css')):  # If the object ends with '.css', the server sends a similar HTTP response with
        # The server then opens the file "styles.css" and sends its contents as the response body.
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/css; charset=UTF-8 \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file4 = open("style.css", "rb")
        connectionSocket.send(file4.read())



    elif (object == "/images/p1.png"):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/jpg; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        f1 = open("images/p1.png", "rb")  # this is the way used to open non text files like imgs and html files
        data = f1.read()
        connectionSocket.send(data)

    elif (object == "/images/p2.jpg"):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/jpg; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        f1 = open("images/p2.jpg", "rb")
        data = f1.read()
        connectionSocket.send(data)

    elif (object == "/images/flag.png"):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/jpg; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        f1 = open("images/flag.png", "rb")
        data = f1.read()
        connectionSocket.send(data)

    elif (object.endswith('.png')):  # files with the extensions '.png'
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file5 = open("images/birzeit.png", "rb")
        connectionSocket.send(file5.read())

    elif (object.endswith('.jpg')):  # The same process occurs for '.jpg' files,
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file6 = open("images/aqsa.jpg", "rb")
        connectionSocket.send(file6.read())

    elif (object == '/cr'):  # status code 307 Temporary Redirect: If the request is for '/cr',
        # the Location header set to cornell
        connectionSocket.send(
            "HTTP/1.1 307 Temporary Redirect \r\n".encode())  # http respons status line//307: represent a temprary redict , telling the client that the requested resource has been temporarily moved to another location, and the client should follow the redirection to access the resource.
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://cornell.edu \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (object == '/so'):  # if the request is for '/so', the server sends a 307 Temporary Redirect
        # instructing the client to make a new request to Stack Overflow.
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (object == '/rt'):  # HTTP request that includes the string "/bzu" in the URL. If this string is present.
        connectionSocket.send(
            "HTTP/1.1 307 Temporary Redirect \r\n".encode())  # HTTP response to the client with a "307 Temporary Redirect" status code
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send(
            "Location: https://ritaj.birzeit.edu \r\n".encode())  # HTTP response with the Location header set to birzeit edu
        connectionSocket.send("\r\n".encode())


    else:  # where a requested resource is not found .
        connectionSocket.send(
            "HTTP/1.1 404 Not Found \r\n".encode())  # the server sends a 404 Not Found HTTP response to the client
        connectionSocket.send("Content-Type: text/html \r\n".encode())  # type text HTML
        connectionSocket.send("\r\n".encode())
        notFoundHtmlString = "<html>" \
                             "<head>" \
                             "<title>Error 404</title>" \
                             "</head>" \
                             "<body style='background-color: white;'>" \
                             "<div>" \
                             "HTTP/1.1 404 Not Found <hr>" \
                             "<p style='font-size: 30px; background-color: black; color:white; text-align: center; border-style: ridge;border-color: white; border-width: thick; text-align: center;padding-bottom:8px'>" \
                             "Sorry The request is WRONG !!!!</p> <hr>" \
                             "<p style ='font-size: 45px; font-family: georgia;text-align:center; color:Red'>" \
                             "<strong>" \
                             "The file is not found </strong> </p>" \
                             "<pre style ='font-size: 25px; font-family: arial ;text-align:center; color:Black'> <br>" \
                             "<b>     Name: Mujahed Abuali #121107 <br/>" \
                             "Name: Ziad masalma #1202199<br/>" \
                             "Name: manal nidal #1221098<br/><br/><br/>" \
                             "</b>" \
                             "</pre>" \
                             "<pre style='font-size: 40px; font-family: arial;text-align:center; color:Black'><br>" \
                             f"IP: {ip}     " \
                             f"Port: {port}" \
                             "</pre>" \
                             "</div>" \
                             "</body>" \
                             "</html>"
        # if the request is wrong or the file doesnt exist the server should return a simple HTML webpage that contains with
        # some design and color needed
        notFoundHtmlBytes = bytes(notFoundHtmlString, "UTF-8")
        connectionSocket.send(notFoundHtmlBytes)

    connectionSocket.close()  # close the connection
