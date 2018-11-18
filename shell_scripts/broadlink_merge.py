#!/usr/bin/python

import sys
import struct

def hexy(byte):
 return hex(byte)[2:].zfill(2)

def tohex(bytes):
  r = ''
  for b in bytes:
    r += hexy(b)
  return r

def reconstruct(protocol, repeats, payload):
  s_protocol = hexy(protocol)
  s_repeats = hexy(repeats)
  length = len(payload)
  s = struct.pack('<H', length)
  first, second = struct.unpack('<BB', s)
  s_length = hexy(first) + hexy(second)
  return '%s%s%s%s' % (s_protocol, s_repeats, s_length, tohex(payload))


packets=sys.argv[1].split(',')

cross_packet_protocol=None
first_repeats=None

unified_payload = []

for packet in packets:
  packet_bytes = []
  for index in range(0, len(packet)/2):
    byte = int(packet[index*2:index*2+2], 16)
    packet_bytes.append(byte)

  protocol = packet_bytes[0]

  if cross_packet_protocol:
    if protocol != cross_packet_protocol:
      print 'Protocol mismatch across packets, exiting'
      exit(-1)
  cross_packet_protocol = protocol

  repeats = packet_bytes[1]

  if not first_repeats:
    first_repeats = repeats

  length_str = packet_bytes[2:4]

  print length_str[1], length_str[0]
  length = (length_str[1]<<8) + length_str[0]

  print 'protocol', protocol
  print 'repeats', repeats
  print 'length', length


  payload = packet_bytes[4:]

  unified_payload += payload
  print payload, unified_payload

print reconstruct(cross_packet_protocol, first_repeats, unified_payload)

