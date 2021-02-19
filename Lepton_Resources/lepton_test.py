import numpy as np
import cv2
from pylepton.Lepton3 import Lepton3

while True:
    with Lepton3() as l:
      a,_ = l.capture()
    cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX) # extend contrast
    np.right_shift(a, 8, a) # fit data into 8 bits
    cv2.imshow("output", np.uint8(a)) # write it!
    if cv2.waitKey(20) & 0xFF == ord('d'):
      break

cv2.destroyAllWindows()
