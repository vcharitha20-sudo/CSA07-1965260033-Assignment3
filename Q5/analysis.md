# Q5 — Analysis and worked answers

## Voice load and Erlang B
120 calls/hour × 3/60 hours = 6 Erlangs. Erlang B for 6, 8, 10, 12 lines: 26.49%, 12.19%, 4.31%, 1.14%. 13 lines achieve at most 1% blocking.

## Queue comparison
For an M/M/1 queue at λ=80/s and μ=100/s, mean system time = 1/(100−80) = 0.05 s. For two M/M/1 queues each at λ=40/s and μ=50/s, mean = 0.10 s, assuming even splitting. A shared M/M/2 system differs and requires Erlang C.

## Token bucket
Bucket 500 KB ≈ 4 Mb; net drain while sending at 8 Mbps against a 1 Mbps token rate is 7 Mbps, so burst lasts ≈4/7=0.571 s. Data transmitted in that interval ≈8×0.571/8=0.571 MB.

## QoS
Voice: EF; video lectures: AF; booking database: AF; backup and e-mail: best effort. Priority queues protect delay-sensitive traffic if configured with safeguards.

## Alternative queue
For Erlang C with 8 lines and offered load 6 Erlangs, callers may wait instead of being blocked; this trades blocked calls for queue delay and requires a finite waiting policy.

## Reproducibility
Figures labelled as calculations are derived from the question data. Python outputs are from local execution. Wireshark/iperf/browser/Packet Tracer measurements are not included without a corresponding capture.
