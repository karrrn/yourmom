/*
  Simple script to see how the board works
 */
 
 int C0=2;
 int C1=3;
 int C2=4;
 int C3=5;
 int C4=6;
 int C5=7;
 int C6=8;
 
 int R0=9;
 int R1=10;
 int R2=11;
 int R3=12;
 
// the setup routine runs once when you press reset:
void setup() {
  Serial.begin(9600);  
  // initialize the digital pin as an output.
  // read all rows all the time
 
  pinMode(R0, INPUT);digitalWrite(R0, HIGH);     
  pinMode(R1, INPUT);digitalWrite(R1, HIGH);     
  pinMode(R2, INPUT);digitalWrite(R2, HIGH);          
  pinMode(R3, INPUT);digitalWrite(R3, HIGH);     

  // collms will be activated layer, so read only first  
  pinMode(C0, INPUT);digitalWrite(C0, LOW);     
  pinMode(C1, INPUT);digitalWrite(C1, LOW);    
  pinMode(C2, INPUT);digitalWrite(C2, LOW);     
  pinMode(C3, INPUT);digitalWrite(C3, LOW);     
  pinMode(C4, INPUT);digitalWrite(C4, LOW);    
  pinMode(C5, INPUT);digitalWrite(C5, LOW);     
  pinMode(C6, INPUT);digitalWrite(C6, LOW);          
}

// the loop routine runs over and over again forever:
void loop() {
  //Serial.println("telefon buttons");
  digitalWrite(C4,HIGH);
  Serial.print(digitalRead(C0)); 
  Serial.print(digitalRead(C1)); 
  Serial.print(digitalRead(C2)); 
  
  Serial.print(digitalRead(C3));
  Serial.print(digitalRead(C4)); 
  Serial.print(digitalRead(C5)); 
  Serial.print(digitalRead(C6));
  
  Serial.print(digitalRead(R0));
  Serial.print(digitalRead(R1));
  Serial.print(digitalRead(R2));
  Serial.println(digitalRead(R3));
}
