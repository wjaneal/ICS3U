/*Arduino Control Program - Automated RC FLight*/
#include "WProgram.h"
void setup();
void loop();
int read1 = 0;
int val = 0;         // variable to store the read value
int val1 = 0;        // variable to store the ones column of the circuit power
int val2 = 0;        // variable to store the tens column of the circuit power
int val3 = 0;
int ledPin2 = 2;      // 
int ledPin3 = 3;      // 
int ledPin4 = 4;      // 
int ledPin5= 5;      // 
int ledPin6 = 6;      // 
int ledPin7 = 7;      // 
int ledPin8 = 8;      // 
int ledPin9 = 9;      // 
int ledPin10 = 10;      // 
int ledPin11 = 11;      // 
int ledPin12 = 12;      // 
int ledPin13 = 13;      // 

//The Arduino control is being rewritten for four helicopter functions - August 9, 2009

void setup() {
	Serial.begin(9600);	// opens serial port, sets data rate to 9600 bps
         //Set Pins 2-4 as reference and 5-7 as throttle
         analogWrite(ledPin2, 200);//Set the pins high to mimic the potentiometer
         analogWrite(ledPin3, 200);//reference voltage
         analogWrite(ledPin4, 200);
         //Set the drive pins to 0 - 5,6,7: Throttle 
         analogWrite(ledPin5, 0);
         analogWrite(ledPin6, 0);
         analogWrite(ledPin7, 0);
         //Set Pins 8 and 9 for Reference and Forward / Backward
         //Forward / Backvard Reference Voltage
         analogWrite(ledPin8, 200);
         analogWrite(ledPin9, 100); //Default: about 100 for neutral setting
         //Set pins 10 and 11 for Reference and Directional Change
         analogWrite(ledPin10, 200);
         analogWrite(ledPin11, 100); //Default: about 100 for neutral setting
         //Set pins 12 and 13 for Reference and Side to Side Control
         analogWrite(ledPin12, 200);
         analogWrite(ledPin13, 100);//Default: about 100 for neutral setting
         
     
     

}
void loop() {
        //A==65; B==66; C==67; D==68; these are for Throttle, Forward/Backward, Directional and
        //Side to side
       
	// send data only when you receive data:
        if (Serial.available() > 0) {
                read1 = (Serial.read());

             if (read1 == 65){
                  Serial.print("Received Data Point");
		  // read the incoming byte:
		  val1 = (Serial.read()-48);
                  //if(val1 < 0) val1 = 0;
                  val2 = (Serial.read()-48);
                  if(val2 < 0) val2 = 0;
                  val3 = (Serial.read()-48);
                  if(val3<0) val3 = 0;
                  val = 100*val1+ 10*val2+val3;
                  //Adjust the throttle accordingly
                  analogWrite(ledPin5, val);
                  analogWrite(ledPin6,val);
                  analogWrite(ledPin7,val);
		  // say what you got:
		  
                  Serial.println(val, DEC);
                  //Serial.print(val1,DEC);
		  //Serial.println(val2, DEC);
	          }
             if (read1 == 66){
                  Serial.print("Forward / Backwards");
		  // read the incoming byte:
		  val1 = (Serial.read()-48);
                  //if(val1 < 0) val1 = 0;
                  val2 = (Serial.read()-48);
                  if(val2 < 0) val2 = 0;
                  val3 = (Serial.read()-48);
                  if(val3<0) val3 = 0;
                  val = 100*val1+ 10*val2+val3;
                  //Set Forward/Backward Value
                  analogWrite(ledPin9, val);
		  // say what you got:
		  
                  Serial.println(val, DEC);
                  //Serial.print(val1,DEC);
		  //Serial.println(val2, DEC);
	          }
              if (read1 == 67){
                  Serial.print("Forward / Backwards");
		  // read the incoming byte:
		  val1 = (Serial.read()-48);
                  //if(val1 < 0) val1 = 0;
                  val2 = (Serial.read()-48);
                  if(val2 < 0) val2 = 0;
                  val3 = (Serial.read()-48);
                  if(val3<0) val3 = 0;
                  val = 100*val1+ 10*val2+val3;
                  //Set Directional Value:
                  analogWrite(ledPin11, val);
                  
		  // say what you got:
		  
                  Serial.println(val, DEC);
                  //Serial.print(val1,DEC);
		  //Serial.println(val2, DEC);
	          }
             if (read1 == 68){
                    
                  Serial.print("Forward / Backwards");
		  // read the incoming byte:
		  val1 = (Serial.read()-48);
                  //if(val1 < 0) val1 = 0;
                  val2 = (Serial.read()-48);
                  if(val2 < 0) val2 = 0;
                  val3 = (Serial.read()-48);
                  if(val3<0) val3 = 0;
                  val = 100*val1+ 10*val2+val3;
                  //Set side to side motion value:
                  analogWrite(ledPin13, val);
		  // say what you got:
		  
                  Serial.println(val, DEC);
                  //Serial.print(val1,DEC);
		  //Serial.println(val2, DEC);
	          }
	
        }


	

        }

int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

