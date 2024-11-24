from bwt import *

inp_str = "banananananas"
compressed = compress(inp_str)
decompressed = decompress(compressed)

print("ORIGINAL STRING: " + inp_str)
print("COMPRESSED STRING: " + compressed)
print("UNCOMPRESSED STRING: " + decompressed)
print()
print("Do both the original and the uncompressed strings match? " + str("yes" if inp_str == decompressed else "no"))