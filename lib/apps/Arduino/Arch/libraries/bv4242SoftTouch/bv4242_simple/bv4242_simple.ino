// Demo program simple key test
#include <bv4242Soft.h>

// 8 bit adddress is used for soft I2C
BV4242 ui(0x7a);

void setup()
{
  // allow a delay to get device up and running
  delay(1500);

  // turn down contrast
  ui.lcd_contrast(20);

  // For running on batteries time base needs increasing, bit
  // slower response but works for most conditions the default
  // is 25 - okay to keep writing as library will ignore if
  // already set to requested value
  ui.timebase(35);

  // start up message
  ui.lcd_mode(0); // single hight
  ui.clear();
  ui.print("Arduino");
  ui.setCursor(1,2);
  ui.print("Touch");
  delay(2500);
  ui.lcd_mode(1); // dual hight
  ui.clear();
  ui.print("Key>");
  ui.cursor();
  ui.clrBuf(); // clear keypad buffer
};

void loop()
{
char k, buf[10];  
  if((k = ui.key())) { // get next key from buffer
    ui.setCursor(6,0);
    ui.print("  ");
    ui.setCursor(6,0);
    sprintf(buf,"%d",k);
    ui.print(buf);
  }
  delay(50);
}

