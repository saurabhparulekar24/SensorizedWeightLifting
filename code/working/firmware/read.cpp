//#include "ICM20948.h"
#include <string.h>
#include "stdio.h"
#include <string.h>
#include <pico/stdlib.h>
#include <hardware/gpio.h>
//#include "accelerometer_handler.h"
#include <ICM42622.h>
#include <pico/stdio.h>

int main(){
  stdio_init_all();
  i2c_init(I2C_PORT, 400 * 1000);
  gpio_set_function(4, GPIO_FUNC_I2C);
  gpio_set_function(5, GPIO_FUNC_I2C);
  gpio_pull_up(4);
  gpio_pull_up(5);
  sleep_ms(1000);
  ICM42622::Icm42622Init();
  while(1){
    float x, y, z;
    //printf("Wow");
    ICM42622::Icm42622ReadGyro(&x,&y,&z);
    const float norm_x = -y;
    const float norm_y = x;
    const float norm_z = -z;
    printf("%f\n",x);
  }
}





