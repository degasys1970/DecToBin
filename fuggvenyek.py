def dec_to_binnary(num):
  bits = []
  while num > 0:
    bits.append(num % 2)
    num = num // 2
  bits.reverse()
  binary = ''
  for bit in bits:
    binary += str(bit)
  return binary