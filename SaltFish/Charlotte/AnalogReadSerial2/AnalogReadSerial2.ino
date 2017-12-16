/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/
/*int out1 = 8;
int j=0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  //pinMode(8,OUTPUT);
  analogWrite(7,0);
  
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(0);
  if (j<1000){
    j++;
    }
   else{
    j=0;
   }
   delay(10);
  analogWrite(7,j);
  // print out the value you read:
  Serial.print(j);
  Serial.print(", ");
  Serial.println(sensorValue);
  delay(1);        // delay in between reads for stability
  
}
*/
int out1 = 8;
int j=0;
int sensorValue=0;
int val = 0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(13,INPUT);
}
// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  //sensorValue = analogRead(7);
  if (j<1000){
    j++;
    analogWrite(8,j);
    val=analogRead(13);
  }
else{
    j=0;
    analogWrite(8,0);
    val=analogRead(13);
   }
  delay(10);
  Serial.print(j);
  Serial.print(", ");
  Serial.println(val);
  //delay(1);      
}

