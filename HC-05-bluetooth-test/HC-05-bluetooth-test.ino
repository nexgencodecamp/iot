/*
AUTHOR: Hazim Bitar (techbitar)
DATE: Aug 29, 2013
LICENSE: Public domain (use at your own risk)
CONTACT: techbitar at gmail dot com (techbitar.com)
*/

/*
  MODIFICATIONS & COMMENTS: Pete Januarius

  Serial Port Bluetooth Module (Master/Slave) : HC-05
  https://www.itead.cc/wiki/Serial_Port_Bluetooth_Module_(Master/Slave)_:_HC-05

  Arduino and HC-05 Bluetooth Module Tutorial
  https://howtomechatronics.com/tutorials/arduino/arduino-and-hc-05-bluetooth-module-tutorial/

  Arduino With HC-05 Bluetooth Module in Slave Mode
  http://www.martyncurrey.com/arduino-with-hc-05-bluetooth-module-in-slave-mode/

  

  Useful Commands

   *** NOTE: I have found that sometimes the below commands will not work without leaving off the ? ****
   
   DESC                           Command               Respond                                           Param
   Test                             AT                    OK
   Reset                            AT+RESET              OK
   Get Firmware version             AT+VERSION?           +VERSION:hc01.comV2.1  (+VERSION:<Param> OK)
   Restore Default                  AT+ORGL               OK
   Set/Check Module mode            AT+ROLE?              0- Slave 1-Master 2-Slave-Loop 
   Get Module Address               AT+ADDR?              +ADDR:2017:10:95001, (+ADDR:<Param> OK)
    The module address comes up as the Bluetooth device on your machine. It may also change to: hc01.com HC-05 or something
  
*/

#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11); // RX | TX

void setup() {
  pinMode(9, OUTPUT);  // this pin will pull the HC-05 pin 34 (key pin) HIGH to switch module to AT mode
  digitalWrite(9, HIGH);
  Serial.begin(9600);
  Serial.println("Enter AT commands:");
  BTSerial.begin(38400);  // HC-05 default speed in AT command more
}

void loop() {
  // Keep reading from HC-05 and send to Arduino Serial Monitor
  if (BTSerial.available())
    Serial.write(BTSerial.read());

  // Keep reading from Arduino Serial Monitor and send to HC-05
  if (Serial.available())
    BTSerial.write(Serial.read());
}
