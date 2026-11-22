# Q2 — Analysis and worked answers

## Congestion-window interpretation
Initial slow start threshold is at least 32 segments (the transition is after 32). The decrease from 35 to 17 near RTT 10 indicates multiplicative decrease / fast loss recovery, characteristic of Reno rather than Tahoe. The drop from 20 to 1 near RTT 14 suggests a timeout. Approximate new thresholds: 17 or 18 after the first loss and 10 after the second.

## Throughput
At RTT 7, cwnd = 33 segments. 33 × 1460 × 8 / 0.080 = 4,818,000 bps ≈ 4.82 Mbps.

## Fairness
Additive increase raises both windows equally; multiplicative decrease reduces their absolute gap. Repeated cycles approach equal sharing.

## Alternative
ECN signals congestion before a drop; the sender reduces its window without waiting for a loss-driven retransmission. ECN does not prevent corruption or physical-link losses.

## Reproducibility
Figures labelled as calculations are derived from the question data. Python outputs are from local execution. Wireshark/iperf/browser/Packet Tracer measurements are not included without a corresponding capture.
