# Q1 — Analysis and worked answers

## Socket demultiplexing
TCP established connections are selected by the four-tuple (source IP, source port, destination IP, destination port). Incoming 49.205.3.9:40001 and 106.200.7.4:40000 match their respective ESTABLISHED sockets. A new SYN from 157.48.9.1:52100 is handled by the LISTEN socket; UDP to port 5060 goes to the shared UDP socket; an unmatched TCP segment without SYN normally causes a reset.

## Overhead
For 80 bytes of application data: UDP 8 + IPv4 20 = 28 bytes, overhead 28/108 = 25.93% of packet bytes. TCP 20 + IPv4 20 = 40 bytes, overhead 40/120 = 33.33%.

## Protocol choice
Login, payment, chat and answer uploads require reliable authenticated transport (TCP/TLS or QUIC). Real-time proctoring video benefits from UDP-based WebRTC with jitter buffering and loss recovery.

## Alternative
60 new TCP connections × 50 ms RTT = 3.0 seconds of handshake latency, with 180 handshake segments instead of 3 for one persistent connection; the additional 177 handshake segments exclude connection-close packets.

## Reproducibility
Figures labelled as calculations are derived from the question data. Python outputs are from local execution. Wireshark/iperf/browser/Packet Tracer measurements are not included without a corresponding capture.
