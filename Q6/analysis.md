# Q6 — Analysis and worked answers

## Handshake estimates at 120 ms RTT
Assuming TLS 1.2 full handshake 2 RTT after TCP and one RTT for the request: TCP + TLS 1.2 = 4 RTT = 480 ms; TCP + TLS 1.3 = 3 RTT = 360 ms; QUIC first connection = 2 RTT = 240 ms; QUIC 0-RTT resumption can deliver an eligible request sooner, approximately 1 RTT = 120 ms.

## Security
TLS 1.3 removes obsolete key exchanges and uses forward-secret ephemeral key agreement. QUIC 0-RTT requests may be replayed, so state-changing operations such as purchasing a course must not use 0-RTT.

## Protocol decision
HTTP/3 can improve startup and reduce cross-stream blocking, with HTTPS over TCP fallback where UDP/443 is blocked.

## Loss comparison
At 100 packets/s over 10 s, 1000 packets are sent. A 2% independent loss rate yields approximately 20 lost packets on average. Exact stall durations depend on RTT, detection, retransmission and stream scheduling, so they cannot be uniquely calculated from the supplied loss rate alone.

## Reproducibility
Figures labelled as calculations are derived from the question data. Python outputs are from local execution. Wireshark/iperf/browser/Packet Tracer measurements are not included without a corresponding capture.
