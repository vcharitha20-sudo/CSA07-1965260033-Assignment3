# Q4 — Analysis and worked answers

## DNS TTL load
One continuously requesting resolver: TTL 60 s -> 60 upstream queries/hour; TTL 20 s -> 180/hour. For 400 resolvers: 24,000 and 72,000/hour respectively.

## Resolver behaviour
The phone normally asks a recursive resolver. On a cache miss, the resolver contacts root, TLD and authoritative servers as needed. Cached answers reduce authoritative load. DNS typically uses UDP, with TCP for truncation or other transport needs.

## DNS design
Publish A/AAAA records for services, MX for mail, NS for delegation, and appropriate TXT for security policy; CNAME is optional. A short TTL aids migration but increases query load.

## Alternative DoH
Ignoring reuse: with 30 ms RTT, TCP handshake 30 ms + TLS 1.3 30 ms + DNS exchange 30 ms = approximately 90 ms; on a reused connection approximately 30 ms. Plain DNS UDP typically requires one 30 ms RTT, excluding cache and server delays.

## Reproducibility
Figures labelled as calculations are derived from the question data. Python outputs are from local execution. Wireshark/iperf/browser/Packet Tracer measurements are not included without a corresponding capture.
