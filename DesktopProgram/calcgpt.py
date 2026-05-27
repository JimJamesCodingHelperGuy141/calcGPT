import openai
import serial
import sys
import glob

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

print("Available serial ports: ")
for x in range(0, len(serial_ports())):
    print(x, serial_ports()[x])

port = input("Enter your selection: ")
ser = serial.Serial(serial_ports()[int(port)], 9600)
ser.write(b'ack')

client = openai.OpenAI(api_key="PASTE_YOUR_GROQ_CLOUD_KEY_HERE", base_url="https://api.groq.com/openai/v1")
messages = [{"role": "system", "content": "You are an intelligent assistant."}]

while True:
    message = ser.readline()
    message = message.decode('utf-8')
    print(message)
    if message:
        messages.append({"role": "user", "content": message})
        chat = client.chat.completions.create(
            model="llama-3.3-70b-versatile", messages=messages
        )
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
        chunk_size = 63
        for i in range(0, len(reply), chunk_size):
            chunk = reply[i:i+chunk_size]
            ser.write(bytes(chunk, 'utf-8'))
