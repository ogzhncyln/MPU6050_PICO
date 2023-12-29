from MPU6050Lib import MPU6050

mpu = MPU6050(9,8,0.165,3.974,1.0,496.9,0.923,0.091)
    
while True:
    ax,ay,az,gx,gy,gz,temp = mpu.read()
    print("Ax:", ax, "m/s^2", "Ay:", ay, "m/s^2", "Az:", az, "m/s^2")
    print("Gx:", gx, "°/s", "Gy:", gy, "°/s", "Gz:", gz, "°/s")
    print("Temperature:", temp, "°C")
    time.sleep(1)