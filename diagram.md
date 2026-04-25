```mermaid
graph TD
   %% Power System
   Batt[Battery Pack]
   PiPower[Pi USB Power] --> Pi
   Batt -->|12V| D1
   Batt -->|12V| D2
  
   %% Ground Bridge
   GND_Bus[Common Ground Rail]
   Pi -->|GND Pin 9| GND_Bus
   GND_Bus -->|GND| D1
   GND_Bus -->|GND| D2
   Batt -->|GND| GND_Bus


   %% Controllers
   subgraph Pi [Raspberry Pi 4]
       GPIO17[GPIO 17 - IN1]
       GPIO27[GPIO 27 - IN2]
       GPIO22[GPIO 22 - IN3]
       GPIO23[GPIO 23 - IN4]
   end


   %% Driver 1: LEFT SIDE
   subgraph D1 [Left L298N Driver]
       IN1_D1[IN1]
       IN2_D1[IN2]
       OUT1_D1[OUT1/OUT2]
   end
  
   %% Driver 2: RIGHT SIDE
   subgraph D2 [Right L298N Driver]
       IN3_D2[IN1]
       IN4_D2[IN2]
       OUT3_D2[OUT1/OUT2]
   end


   %% Motor Connections
   M_Left[Front-Left & Back-Left Motors]
   M_Right[Front-Right & Back-Right Motors]


   %% Signal Links
   GPIO17 --> IN1_D1
   GPIO27 --> IN2_D1
   GPIO22 --> IN3_D2
   GPIO23 --> IN4_D2


   %% Motor Power Links
   OUT1_D1 --> M_Left
   OUT3_D2 --> M_Right





