## Abstraction
class emailServer:

    def _connectToServer(self):
        print("Connecting to server...")
        print("Done.")


    def _authenticateConnection(self):
        print("Authenticating...")
        print("Done.")


    def sendEmail(self):
        self._connectToServer
        self._authenticateConnection
        print("Email sent!")
email = emailServer()
email.sendEmail()