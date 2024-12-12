const int pinLED = 7;
const int pinled = 8;

void setup() 
{
  Serial.begin(9600);
  pinMode(pinLED, OUTPUT);
  pinMode(pinled, OUTPUT);
  digitalWrite(pinLED, HIGH);
  digitalWrite(pinled, HIGH);

}

void loop()
{
  
  if (Serial.available()>0) 
  {
    char option = Serial.read();
    
    if (option == '1')
    {
      
      
      digitalWrite(pinLED, LOW);
      digitalWrite(pinled, LOW);
      delay(1500);
      digitalWrite(pinLED,HIGH);
      digitalWrite(pinled,HIGH);
      
    }
    else{
      digitalWrite(pinLED,HIGH);
      digitalWrite(pinled,HIGH);
    }
    
  }
}