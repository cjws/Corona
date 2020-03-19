// #include "/home/chris/Arduino/libraries/LedControl-1.0.6/src/LedControl.h"
#include "LedControl.h"

LedControl lc=LedControl(12,11,10,1);
// pin 12 is connected to the DIN pin
// pin 11 is connected to the CLK pin
// pin 10 is connected to the CS pin
// 1 as we are only using 1 MAX7219
long int deathCount = 8970;
long int casesCount = 219351;



void setup()
{
  // the zero refers to the MAX7219 number, it is zero for 1 chip
  lc.shutdown(0,false);// turn off power saving, enables display
  lc.setIntensity(0,1);// sets brightness (0~15 possible values)
  lc.clearDisplay(0);// clear screen
}

void displayBatSoup()
{
  lc.clearDisplay(0);// clear screen
  lc.setRow(0,7,0x1F);// b
  lc.setRow(0,6,0x77);// A
  lc.setRow(0,5,0x0F);// t

  lc.setRow(0,3,0x5B);// S
  lc.setRow(0,2,0x7E);// O
  lc.setRow(0,1,0x3E);// U
  lc.setRow(0,0,0x67);// P
}

void displayNumber(long int count)
{
  lc.clearDisplay(0);// clear screen
  int i;
  int numberArray[i];
  i = 0;

  /* extract and write each digit */
  while (count != 0)
  {
      numberArray[i] = count % 10;
      lc.setDigit(0,i,numberArray[i],false);
      count /= 10;
      i++;
  }
}

void loop()
{
  displayBatSoup();
  delay(2500);
  // displayNumber(casesCount);
  // delay(4000);
  // displayNumber(deathCount);
  // delay(4000);
}
