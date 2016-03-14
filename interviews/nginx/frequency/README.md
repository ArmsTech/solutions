# Frequency

Print the top ten most frequently logged IP addresses from a standard NGINX
access.log file.

### Assumptions

This commandline script assumes that the specified access-logfile uses the 
NGINX default (specifically leading with the IP address). To support all access 
logfile formats and/or validate IP addresses we could use a compiled regular 
expression.

### Usage Example

```console
brenj$ ./frequency -h
usage: frequency [-h] PATH

Print top ten most frequently logged IP addresses.

positional arguments:
  PATH        path to NGINX log file

optional arguments:
  -h, --help  show this help message and exit

brenj$ ./frequency access.nginx.log 
621 192.151.151.202
354 142.54.174.178
324 192.187.100.154
292 198.204.235.26
219 162.244.13.12
203 198.204.230.130
171 173.208.203.138
158 46.4.120.3
157 92.222.99.8
152 46.4.116.197
```
