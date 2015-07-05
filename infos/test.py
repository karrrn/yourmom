# steps (1) and (2) before reading GPIOs
self.__preRead()
# (3) scan rows for pushed key/button
rowHi=1
while rowHi==1:
for i in range(len(self.row)):
tmpRead=wiringpi.digitalRead(self.row[i])
if tmpRead==0:
rowHi=0
rowVal=i
# (4) after finding which key/button from the row scans, convert columns to input
for j in range(len(self.col)):
wiringpi.pinMode(self.col[j],INPUT)
# (5) switch the i-th row found from scan to output
wiringpi.pinMode(self.row[rowVal],OUTPUT)
wiringpi.digitalWrite(self.row[rowVal],HIGH)
# (6) scan columns for still-pushed key/button
colLo=0
while colLo==0:
for j in range(len(self.col)):
tmpRead=wiringpi.digitalRead(self.col[j])
if tmpRead==1:
colLo=1
colVal=j
# reinitialize used GPIOs
self.__postRead()
# (7) return the symbol of pressed key from keyPad mapping
return self.keyPad[rowVal][colVal]