#  Agricultural Robot Using Raspberry Pi

**An automated agricultural robot for timed movement and irrigation using Raspberry Pi 4 and Python.**

## 🎥 Project Demonstration

Watch the agricultural robot in action!

▶️ **[Click here to watch the project demo](https://drive.google.com/file/d/19N7_srpPK_Fq8kNpn35ZQk15F-6zbTag/view?usp=sharing))**

---

##  About the Project

Agriculture relies heavily on efficient water management and timely irrigation. Traditional watering methods can require considerable manual effort and may lead to inefficient water distribution.

The **Agricultural Robot** is a Raspberry Pi-based project developed to automate robot movement and water distribution. It uses Python programming and GPIO control to coordinate DC motors and a water pump, demonstrating a simple approach to agricultural automation.

The robot follows a programmed sequence: it moves forward for a fixed duration, stops to activate the water pump, and then repeats the movement and irrigation cycle.

## Project Objectives

- Develop a mobile robot capable of controlled movement.
- Automate water pump operation using a relay module.
- Coordinate robot movement and irrigation through Python.
- Explore an affordable approach to small-scale agricultural automation.
- Establish a foundation for future sensor-based smart irrigation systems.

##  Key Features

- 🤖 **Automated Movement:** Controls two DC motors through a motor driver.
- 💧 **Automated Watering:** Operates a DC water pump through a relay module.
- ⏱️ **Timed Irrigation:** Uses programmed delays to coordinate movement and watering.
- 🐍 **Python-Based Control:** Uses Raspberry Pi GPIO pins for hardware interfacing.
- 🔌 **Hardware Integration:** Combines a Raspberry Pi, motor driver, relay and pump in one system.
- 🌿 **Expandable Design:** Can be extended with soil-moisture sensors, obstacle detection and remote monitoring.

##  How It Works

1. **Initialization:** The Raspberry Pi configures the GPIO pins for motor and relay control.
2. **Forward Movement:** The motor driver receives signals that drive both motors forward for a programmed interval.
3. **Stopping:** The GPIO outputs are set to stop the motors.
4. **Irrigation:** The relay switches the water pump on for a specified duration.
5. **Pump Deactivation:** The relay switches the pump off.
6. **Cycle Repetition:** The robot moves forward again and performs a second watering cycle.
7. **Cleanup:** When the program is interrupted or finishes, the code stops the motors, switches off the pump and cleans up GPIO resources.

The current implementation uses fixed timing for movement and irrigation. It does not yet incorporate soil-moisture feedback or autonomous navigation.

## Hardware Components

| Component | Purpose |
|---|---|
| Raspberry Pi 4 | Main controller for executing the Python program |
| L298N motor driver | Controls the DC motors |
| DC motors | Provide movement to the robot |
| Robot chassis and wheels | Mechanical platform for mobility |
| DC water pump | Distributes water during irrigation |
| Relay module | Switches the water pump |
| Battery pack | Supplies power to the robot hardware |
| Jumper wires | Provide electrical connections |

## Software and Technologies

- **Programming Language:** Python 3
- **Hardware Platform:** Raspberry Pi 4
- **GPIO Control:** `RPi.GPIO`
- **Time Management:** Python `time` module
- **Development Environment:** Thonny IDE

## GPIO Pin Configuration

The program uses BCM GPIO numbering.

| Function | GPIO Pin |
|---|---|
| Motor 1 — IN1 | GPIO 17 |
| Motor 1 — IN2 | GPIO 27 |
| Motor 2 — IN3 | GPIO 22 |
| Motor 2 — IN4 | GPIO 23 |
| Water pump relay | GPIO 13 |

##  Applications

- Small-scale irrigation prototypes
- Home and kitchen garden watering
- Educational robotics and embedded systems projects
- Demonstrations of agricultural automation
- Learning GPIO-based motor and relay control

These are potential applications; the current prototype has not been established as a field-ready agricultural product.

##  Current Limitations

- Movement is controlled using fixed time delays rather than position feedback.
- Irrigation is time-based and does not measure soil moisture.
- Obstacle detection is not implemented.
- The robot does not currently support remote monitoring or autonomous route planning.
- Irrigation performance depends on the pump, power supply and physical setup.

## Future Enhancements

- **Soil-Moisture Monitoring:** Water plants according to measured soil conditions.
- **Obstacle Detection:** Add sensors to identify and avoid obstacles.
- **Smart Irrigation:** Adjust watering duration according to environmental conditions.
- **Remote Monitoring:** Introduce a web or mobile interface for status monitoring and control.
- **GPS or Route Planning:** Explore navigation methods for larger agricultural areas.
- **Camera Integration:** Investigate crop monitoring using computer vision.

## 📚 What This Project Demonstrates

This project provided practical exposure to:

- Raspberry Pi GPIO programming
- Python-based hardware control
- DC motor interfacing
- Relay-based pump control
- Integration of software and electronic hardware
- Sequencing and timing in embedded applications

## 👩‍💻 Contributors

- **Faheemah M**
- Akshiitha V
- Ananya V Shahapur

**Institution:** B.N.M. Institute of Technology (BNMIT), Bengaluru  
**Course:** Advanced Python Programming on Raspberry Pi (23ECE136)  
**Academic Year:** 2024–2025

---

⭐ *An academic project exploring the fundamentals of robotics, embedded systems and agricultural automation.*
