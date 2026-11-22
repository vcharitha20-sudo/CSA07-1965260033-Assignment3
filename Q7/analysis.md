# Q7 — Analysis and worked answers

## Requirements
Remote examination centres have RTT 150–350 ms and up to 4% packet loss. Answers and uploads require reliable, authenticated, ordered delivery; live proctoring needs low-latency adaptive video; chat needs reliable delivery and timely acknowledgement.

## Throughput bounds
64 KiB window at 350 ms: 65536×8/0.35 ≈ 1.50 Mbps. Loss-limited MSS/(RTT×sqrt(p)): 1460/(0.35×0.2) ≈ 20,857 bytes/s ≈ 0.167 Mbps at 4% loss. These are simplified upper-bound models.

## Design
Use HTTPS/TLS 1.3 with resumable, integrity-checked uploads and acknowledgements for answers. Use WebRTC over UDP for proctoring, with TURN fallback and end-to-end access controls. Use HTTPS for chat, DNS caching and differentiated QoS. Test delay and loss in a reproducible simulator.

## Validation
The included design and calculations are a reference implementation plan. Actual loss/delay measurements require running the client/server and impairment tests.

## Alternative vendor
Evaluate measured end-to-end latency, loss recovery, TURN use, encryption, data retention, access control, residency and independent security assessment before choosing a WebRTC vendor.

## Reproducibility
Figures labelled as calculations are derived from the question data. Python outputs are from local execution. Wireshark/iperf/browser/Packet Tracer measurements are not included without a corresponding capture.
