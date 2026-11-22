# Q3 — Analysis and worked answers

## HTTP timing at 80 ms RTT
Assume DNS and TLS are excluded, a TCP setup takes 1 RTT, each request-response takes 1 RTT, and HTML is fetched before objects. 61 objects total. Sequential nonpersistent: 61×2×80 = 9760 ms. Persistent without pipelining: (1+61)×80 = 4960 ms. Persistent with pipelining: (1+1+1)×80 = 240 ms. Six parallel nonpersistent: HTML 160 ms + ceil(60/6)×160 = 1760 ms.

## HTTP/2 versus HTTP/3
HTTP/2 multiplexes streams but one lost TCP segment stalls all streams on that connection; HTTP/3 uses QUIC stream-level loss recovery to avoid cross-stream transport head-of-line blocking.

## Cache
Fresh cached objects may avoid the 60 object requests, leaving approximately the HTML fetch time. ETag permits conditional requests with 304 responses, which still incur RTTs.

## Alternative 15 ms edge RTT
Sequential nonpersistent: 1830 ms; persistent without pipeline: 930 ms; pipelined: 45 ms; six parallel: 330 ms. These are idealised protocol timing calculations, not browser measurements.

## Reproducibility
Figures labelled as calculations are derived from the question data. Python outputs are from local execution. Wireshark/iperf/browser/Packet Tracer measurements are not included without a corresponding capture.
