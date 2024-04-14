import smtplib

def testS(smtp_server, port):
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        print(f"Success {smtp_server} Port {port}")
    except Exception as e:
        print(f"Fail {smtp_server} Port {port} Error {e}")
    finally:
        server.close()

# Usage
testS('smtp.jomaa.tn', 587)