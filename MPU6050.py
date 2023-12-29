from machine import I2C, Pin

class MPU6050:
    
    def __init__(self,scl,sda,offset_ax,offset_ay,offset_az,offset_gx,offset_gy,offset_gz,acceleration_sensitivity=16384.0,gyro_sensitivity=131.0,mpu_addr = 0x68):
        self.scl = scl
        self.sda = sda
        self.acceleration_senstivity = acceleration_sensitivity
        self.gyro_sensitivity = gyro_sensitivity
        self.offset_ax = offset_ax
        self.offset_ay = offset_ay
        self.offset_az = offset_az
        self.offset_gx = offset_gx
        self.offset_gy = offset_gy
        self.offset_gz = offset_gz
        self.mpu_addr = mpu_addr
        
        self.i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
        self.i2c.writeto_mem(self.mpu_addr, 0x6B, bytes([0]))
        
    def read(self):
        data = self.i2c.readfrom_mem(self.mpu_addr, 0x3B, 14)
    
        ax = ((data[0] << 8 | data[1])) / self.acceleration_senstivity
        ay = ((data[2] << 8 | data[3])) / self.acceleration_senstivity
        az = ((data[4] << 8 | data[5])) / self.acceleration_senstivity
        
        ax -= self.offset_ax
        ay -= self.offset_ay
        az -= self.offset_az
        
        gx = ((data[8] << 8 |  data[9])) / self.gyro_sensitivity
        gy = ((data[10] << 8 | data[11])) / self.gyro_sensitivity
        gz = ((data[12] << 8 | data[13])) / self.gyro_sensitivity
        
        gx -= self.offset_gx
        gy -= self.offset_gy
        gz -= self.offset_gz
        
        temp_raw = data[6] << 8 | data[7]
        temp = ((temp_raw / 340.0) + 36.53)/10.0
        
        return (ax,ay,az,gx,gy,gz,temp)
