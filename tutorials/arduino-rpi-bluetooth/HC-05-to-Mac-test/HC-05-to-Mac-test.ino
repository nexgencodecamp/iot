#include <SoftwareSerial.h>

SoftwareSerial btSerial(10, 11); // RX, TX
                                                                                                                                                                                                                                                                                                                                                                                                                                                          
float degreesC;
unsigned long timer = 0;

void setup() {  
  //Setup and flush the serials to begin
  btSerial.begin(9600);
  Serial.begin(9600);
  btSerial.flush();
  Serial.flush();
}

void loop() {  
  //Non-blocking every 1 second
  if ((timer == 0 || millis() >= timer)){
    
    //Grab the current temperature in celsius
    float degreesC = 18.5;
    
    //Send the current temperature. Didn't use readline to avoid blocking problem
    String sendDegrees = "<" + String(degreesC, 2) + ">";
    Serial.println(sendDegrees);
    
    //Convert to byte array
    char charArray[sendDegrees.length() + 1];
    sendDegrees.toCharArray(charArray, sendDegrees.length()+1);

    // Send to Bluetooth
    btSerial.write(charArray);
    
    //Reset the timer for another 1 second.
    timer = millis() + 1000;      
  }
}

