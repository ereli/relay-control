
#define RELAY_PIN  8 // Some damn problem when i use 13, switched to 8 which works!


void setup(){
  
   /* Setup Serial */
   Serial.begin(9600);
   pinMode(RELAY_PIN, OUTPUT); 
   digitalWrite(RELAY_PIN, 0);  // switch on LED
   delay(10);

}

void loop(){

 if (Serial.available()) {

    //read serial as ascii integer
    int ser = Serial.read();
    //Print the value in the serial monitor
    Serial.println(ser);

     if(ser == 49){    
      //The ascii equivilent of numbers 0 - 9 are 48 - 57
      // sending 1 on serial will toggle between states.
      triggerState();
     }

  }

}

void triggerState(){
  if (digitalRead(RELAY_PIN) == LOW)
  {
    digitalWrite(RELAY_PIN, 1);
  } else {
    digitalWrite(RELAY_PIN, 0);
  } 
}

