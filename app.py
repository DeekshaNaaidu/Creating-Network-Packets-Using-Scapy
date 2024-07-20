from flask import Flask, render_template, request
import scapy.all as scapy

app = Flask(__name__)

# Main home page
@app.route('/')
def home():
    return render_template('home.html')


# ICMP packet creator page
@app.route('/icmp')
def icmp_page():
    return render_template('icmp.html')

@app.route('/send-icmp-packet', methods=['POST'])
def send_icmp_packet():
    target_ip = request.form['target_ip']
    fake_ip = request.form['fake_ip']
    packet = scapy.IP(src=fake_ip, dst=target_ip) / scapy.ICMP()
    scapy.send(packet, verbose=False)
    return f"<div style='color: green; font-size: 40px; font-family: Arial, sans-serif; background-color: black; text-align: center; padding: 10px; display: flex; justify-content: center; align-items: center; height: 100vh;'>ICMP packet sent from ( <strong>{ fake_ip }</strong>  )  to    ( <strong>{target_ip}</strong>).</div>"
    #return f"<div style='color: green; font-size: 18px; font-family: Arial, sans-serif; background-image: linear-gradient(to bottom right, #00b4db, #0083b0); text-align: center; padding: 10px;'>ICMP packet sent from <strong>{fake_ip}</strong> to <strong>{target_ip}</strong>.</div>"
    #return f"<div style='color: green; font-size: 18px; font-family: Arial, sans-serif;'>ICMP packet sent from <strong>{fake_ip}</strong> to <strong>{target_ip}</strong>.</div>"
    #return f"<div class='message'>ICMP packet sent from {fake_ip} to {target_ip}.</div>"
    #return f"ICMP packet sent from {fake_ip} to {target_ip}."

# IP packet creator page
@app.route('/ip')
def ip_page():
    return render_template('ip.html')

@app.route('/send-ip-packet', methods=['POST'])
def send_ip_packet():
    target_ip = request.form['target_ip']
    fake_ip = request.form['fake_ip']
    message = request.form['message']
    packet = scapy.IP(src=fake_ip, dst=target_ip) / scapy.Raw(load=message)
    scapy.send(packet, verbose=False)
    # return f"IP packet sent from {fake_ip} to {target_ip} with message: {message}."
    return f"<div style='color: green; font-size: 40px; font-family: Arial, sans-serif; background-color: black; text-align: center; padding: 10px; display: flex; justify-content: center; align-items: center; height: 100vh;'>IP packet sent from ( <strong>{fake_ip}</strong> ) to ( <strong>{target_ip}</strong> ) with message : </strong>{message}</strong>.</div>"
    # return f"<div style='color: green; font-size: 50px; font-family: Arial, sans-serif; background-color: black; text-align: center; padding: 10px; display: flex; justify-content: center; align-items: center; height: 100vh;'>ICMP packet sent from ( <strong>{ fake_ip }</strong>  )  to    ( <strong>{target_ip}</strong>).</div>"


# UDP packet creator page
@app.route('/udp')
def udp_page():
    return render_template('udp.html')

@app.route('/send-udp-packet', methods=['POST'])
def send_udp_packet():
    target_ip = request.form['target_ip']
    target_port = int(request.form['target_port'])
    fake_ip = request.form['fake_ip']
    fake_port = int(request.form['fake_port'])
    message = request.form['message']

    packet = (
        scapy.IP(src=fake_ip, dst=target_ip) /
        scapy.UDP(sport=fake_port, dport=target_port) /
        scapy.Raw(load=message)
    )
    scapy.send(packet, verbose=False)
    # return f"UDP packet sent from {fake_ip}:{fake_port} to {target_ip}:{target_port} with message: {message}."
    return f"<div style='color: green; font-size: 40px; font-family: Arial, sans-serif; background-color: black; text-align: center; padding: 10px; display: flex; justify-content: center; align-items: center; height: 100vh;'>UDP packet sent from ( <strong>{fake_ip}:{fake_port}</strong> ) to ( <strong>{target_ip}:{target_port}</strong> ) with message: </strong>{message}</strong>.</div>"
    # return f"<div style='color: green; font-size: 40px; font-family: Arial, sans-serif; background-color: black; text-align: center; padding: 10px; display: flex; justify-content: center; align-items: center; height: 100vh;'>IP packet sent from ( <strong>{fake_ip}</strong> ) to ( <strong>{target_ip}</strong> ) with message : </strong>{message}</strong>.</div>"


# TCP packet creator page
@app.route('/tcp')
def tcp_page():
    return render_template('tcp.html')

@app.route('/send-tcp-packet', methods=['POST'])
def send_tcp_packet():
    target_ip = request.form['target_ip']
    target_port = int(request.form['target_port'])
    fake_ip = request.form['fake_ip']
    fake_port = int(request.form['fake_port'])
    message = request.form['message']

    packet = (
        scapy.IP(src=fake_ip, dst=target_ip) /
        scapy.TCP(sport=fake_port, dport=target_port) /
        scapy.Raw(load=message)
    )
    scapy.send(packet, verbose=False)
    # return f"TCP packet sent from {fake_ip}:{fake_port} to {target_ip}:{target_port} with message: {message}."
    return f"<div style='color: green; font-size: 40px; font-family: Arial, sans-serif; background-color: black; text-align: center; padding: 10px; display: flex; justify-content: center; align-items: center; height: 100vh;'>TCP packet sent from ( <strong>{fake_ip}:{fake_port}</strong> ) to ( <strong>{target_ip}:{target_port}</strong> ) with message: </strong>{message}</strong>.</div>"


if __name__ == '__main__':
    app.run(debug=True)
