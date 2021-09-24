int Button1 = 2;
int Button2 = 3;
int Button3 = 4;
int Button4 = 5;
int Button5 = 6;
int Button6 = 7;
int Button7 = 8;
int Button8 = 9;
int Button9 = 10;
int Button10 = 11;
 
 
int buttonState1;
int buttonState2;  
int buttonState3;
int buttonState4;
int buttonState5;
int buttonState6;
int buttonState7;
int buttonState8;
int buttonState9;
int buttonState10;




void setup() {
  Serial.begin(9600); 
  pinMode(Button1, INPUT);
  pinMode(Button2, INPUT);
  pinMode(Button3, INPUT);
  pinMode(Button4, INPUT);
  pinMode(Button5, INPUT);
  pinMode(Button6, INPUT);
  pinMode(Button7, INPUT);
  pinMode(Button8, INPUT);
  pinMode(Button9, INPUT);
  pinMode(Button10, INPUT);
}
 
 
void loop() {
 buttonState1 = digitalRead(Button1);
 buttonState2 = digitalRead(Button2); 
 buttonState3 = digitalRead(Button3); 
 buttonState4 = digitalRead(Button4); 
 buttonState5 = digitalRead(Button5); 
 buttonState6 = digitalRead(Button6);
 buttonState7 = digitalRead(Button7); 
 buttonState8 = digitalRead(Button8);
 buttonState9 = digitalRead(Button9);
 buttonState10 = digitalRead(Button10);
 
   
  
         
     if (buttonState1 || buttonState2 || buttonState3 || buttonState4 || buttonState5 || buttonState6)
         {
                if (!buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("4");         
               } 
               
               else if (buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("14");         
               } 
                else if (!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("24");         
               } 
                else if (!buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("5");         
               } 
                else if (buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("15");         
               } 
                else if (!buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("45");         
               } 
                else if (!buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("6");         
               } 
                else if (buttonState1 && buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("1245");         
               }  
               else if (!buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("46");         
               } 
               else if (!buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && buttonState5 &&buttonState6)
               {
                     Serial.println("56");         
               } 
               else if (buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("125");         
               } 
              else if (!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("245");         
               } 
              else if (!buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("6");         
               } 
               if (buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("1");         
               }
                else if (!buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("25");         
               } 
                else if (!buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("35");         
               } 
               else if (!buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("2");         
               } 
               else if (!buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("26");         
               } 
               else if (buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("12");         
               } 
               else if (!buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("3");         
               } 
               else if (!buttonState1 && buttonState2 && buttonState3 && !buttonState4 && buttonState5 && buttonState6)
               {
                     Serial.println("2356");         
               } 
               else if (buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("13");         
               } 
               else if (!buttonState1 && buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("23");         
               } 
               else if (!buttonState1 && buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("235");         
               } 
               else if (!buttonState1 && buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("236");         
               } 
               else if (!buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && buttonState6)
               {
                     Serial.println("256");         
               } 
               else if (!buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && buttonState5 && buttonState6)
               {
                     Serial.println("356");         
               } 
               if (buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("126");         
               } 
               else if (!buttonState1 && !buttonState2 && buttonState3 && buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("345");         
                     if(buttonState1 && buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                       Serial.println("1235");
                     }
               } 
               else if(!buttonState1 && buttonState2 && buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("234");         
               } 
               else if(buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && buttonState6)
               {
                     Serial.println("156");         
               } 
               else if(buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("136");         
               } 
               else if(!buttonState1 && !buttonState2 && buttonState3 && buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("346");         
               } 
               else if(buttonState1 && !buttonState2 && buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("134");    
                     if(buttonState1 && buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                       Serial.println("1235");
                     }
               } 
               else if(buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("146");         
               }
 
               else if(!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("246");         
               } 
               else if (buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("135");         
               } 
               else if (!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && buttonState5 && buttonState6)
               {
                     Serial.println("2456");         
               } 
               else if(buttonState1 && !buttonState2 && buttonState3 && buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("1345");         
               } 
               else if (buttonState1 && buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
               {
                     Serial.println("1235");         
               } 
               else if (!buttonState1 && !buttonState2 && buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("34");         
               } 
               else if (buttonState1 && buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
               {
                     Serial.println("1236");
                     if(buttonState1 && buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                       Serial.println("1235");
                     }         
               } 
               else if (buttonState1 && buttonState2 && buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
               {
                     Serial.println("1234");         
                     if(buttonState1 && buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                       Serial.println("1235");
                     }
               } 
               else if (buttonState1 && !buttonState2 && buttonState3 && buttonState4 && buttonState5 && buttonState6)
               {
                     Serial.println("13456");         
               } 
               if (!buttonState1 && !buttonState2 && buttonState3 && buttonState4 && buttonState5 && buttonState6)
               {
                     Serial.println("3456");         
                     if (buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("1");         
                     } 
                     else if (buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("12");         
                     } 
                     else if (buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("14");         
                     } 
                     else if (buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("145");         
                     } 
                     else if (buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("15");         
                     } 
                     else if (buttonState1 && buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("124");         
                     } 
                     else if (buttonState1 && buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("1245");         
                     } 
                     else if (buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("125");         
                     } 
                     else if (!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("24");         
                     } 
                     else if (!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("245");         
                     } 
               } 
               if (!buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && buttonState5 && buttonState6)
               {
                     Serial.println("356");         
                     if (buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("1");         
                     } 
                     else if (buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("12");         
                     } 
                     else if (buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("14");         
                     } 
                     else if (buttonState1 && !buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("145");         
                     } 
                     else if (buttonState1 && !buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("15");         
                     } 
                     else if (buttonState1 && buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("124");         
                     } 
                     else if (buttonState1 && buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("1245");         
                     } 
                     else if (buttonState1 && buttonState2 && !buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("125");         
                     } 
                     else if (!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("24");         
                     } 
                     else if (!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("245");         
                     } 
                     else if (buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("13");         
                     } 
                     else if (buttonState1 && buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("123");         
                     } 
                     else if (buttonState1 && !buttonState2 && buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("134");         
                     } 
                     else if (buttonState1 && !buttonState2 && buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("1345");         
                     } 
                     else if (buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("135");         
                     } 
                     else if (buttonState1 && buttonState2 && buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("1234");         
                     } 
                     else if (buttonState1 && buttonState2 && buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("12345");         
                     } 
                     else if (buttonState1 && buttonState2 && buttonState3 && !buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("1235");         
                     } 
                     else if (!buttonState1 && buttonState2 && buttonState3 && buttonState4 && !buttonState5 && !buttonState6)
                     {
                           Serial.println("234");         
                     } 
                     else if (!buttonState1 && buttonState2 && buttonState3 && buttonState4 && buttonState5 && !buttonState6)
                     {
                           Serial.println("2345");         
                     } 
                     else if (buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
                     {
                           Serial.println("136");         
                     } 
                     else if (buttonState1 && buttonState2 && buttonState3 && !buttonState4 && !buttonState5 && buttonState6)
                     {
                           Serial.println("1236");         
                     } 
                     else if (!buttonState1 && buttonState2 && !buttonState3 && buttonState4 && buttonState5 && buttonState6)
                     {
                           Serial.println("2456");         
                     } 
                     else if (buttonState1 && !buttonState2 && buttonState3 && buttonState4 && !buttonState5 && buttonState6)
                     {
                           Serial.println("1346");         
                     } 
                     else if (buttonState1 && !buttonState2 && buttonState3 && buttonState4 && buttonState5 && buttonState6)
                     {
                           Serial.println("13456");         
                     } 
                     else if (buttonState1 && !buttonState2 && buttonState3 && !buttonState4 && buttonState5 && buttonState6)
                     {
                           Serial.println("1356");         
                     } 
               }
         }
         
         if(buttonState7){
             Serial.println("7");
         }
         else if (buttonState8){
             Serial.println("8");
         }
         else if(buttonState9){
             Serial.println("9");
         }
         else if(buttonState10){
             Serial.println("10");
         }
  delay(300);
}

