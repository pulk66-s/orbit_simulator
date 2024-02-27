# Quantum gravity simulator

This is taking some real physics equations that we can give to a computer and simulate thanks to a quantum computer the behavior of gravity.

## Equations

### Newton's law of universal gravitation

Equation:
$$
F = G \frac{m_1 m_2}{r^2}
$$
---
$$
\begin{split}
    F &= G \frac{m_1 m_2}{r^2} \\
    &= (m^3*kg^{-1}*s^{-2}) \frac{kg * kg}{m^2} \\
    &= \frac{m^3*s^{-2}*kg}{m^2} \\
    &= \frac{m^3}{m^2}*s^{-2}*kg \\
    &= m*s^{-2}*kg \\
    &= \frac{kg*m}{s^2} \\
    &= N \\
\end{split}
$$
    
    Where:
    - F is the force between the masses
    - G is the gravitational constant = 6.67430 * 10^-11 m^3 kg^-1 s^-2
    - m1 is the first mass
    - m2 is the second mass
    - r is the distance between the centers of the masses

#### How to apply this force to the Earth and the Moon?

We can use Newton's second law of motion to calculate the acceleration of the Earth and the Moon.

$$
\begin{split}
    F &= m a \\
    a &= \frac{F}{m}
\end{split}
$$
---
$$
    a = \frac{F}{m} = \frac{N}{kg} = \frac{kg*m}{s^2} * \frac{1}{kg} = m/s^2 \\
$$
    Where:
    - F is the force between the Earth and the Moon
    - m is the mass of the Earth or the Moon
    - a is the acceleration of the Earth or the Moon

We can use the following equation to calculate the speed of the Earth and the Moon.

$$
\begin{split}
    v &= a t
\end{split}
$$

    Where:
    - v is the speed of the Earth or the Moon
    - a is the acceleration of the Earth or the Moon
    - t is the time

# Real world simulation

This is taking some real physics equations that we can give to a computer and simulate thanks to a quantum computer the behavior of gravity.

## Equations Applicaiton

### Newton's law of universal gravitation

#### Apply the equation for a earth / moon system

    - m1 = 5.972 * 10^24 kg, the mass of the Earth
    - m2 = 7.342 * 10^22 kg, the mass of the Moon
    - r = 384,400 km, the distance between the Earth and the Moon, 384,400 km = 384,400 * 10^3 m

Let's say there is no other force than gravity between the Earth and the Moon. We can calculate the force between the Earth and the Moon.

$$
\begin{split}
    F &= G \frac{m_1 m_2}{r^2} \\
    &= 6.67430 * 10^{-11}\frac{5.972*10^{24}*7.342*10^{22}}{(384,400*10^3)^2} \\
    &= 6.67430 * 10^{-11}\frac{5.972*10^{24}*7.342*10^{22}}{(384,400*10^3)^2} \\
    &= 6.67430 * 10^{-11}\frac{5.972*7.342*10^{46}}{384,400^2*10^6} \\
    &= 6.67430 * \frac{5.972*7.342}{384,400^2}*\frac{10^{46}}{10^6} * 10^{-11} \\
    &= 6.67430 * \frac{5.972*7.342}{384,400^2}*10^{29} \\
    &\approx 2 * 10^{-9} * 10^{29} \\
    &\approx 2 * 10^{20} \\
\end{split}
$$

This is the force between the Earth and the Moon.

#### How to apply this force to the Earth and the Moon?

We can use Newton's second law of motion to calculate the acceleration of the Earth and the Moon.

$$
\begin{split}
    F &= m a \\
    a &= \frac{F}{m}
\end{split}
$$
---
$$
    a = \frac{F}{m} = \frac{N}{kg} = \frac{kg*m}{s^2} * \frac{1}{kg} = m/s^2 \\
$$
    Where:
    - F is the force between the Earth and the Moon
    - m is the mass of the Earth or the Moon
    - a is the acceleration of the Earth or the Moon

#### Apply the equation for the Earth

    - m = 5.972 * 10^24 kg, the mass of the Earth

$$
\begin{split}
    a &= \frac{1.98 * 10^{20}}{5.972 * 10^{24}} \\
    &= \frac{1.98}{5.972} * \frac{10^{20}}{10^{24}} \\
    &= \frac{1.98}{5.972} * 10^{-4} \\
    &= 0.000033155 = 3.3155 * 10^{-5} m/s^2 \\
\end{split}
$$

This is the acceleration of the Earth.

#### Apply the equation for the Moon

    - m = 7.342 * 10^22 kg, the mass of the Moon

$$
\begin{split}
    a &= \frac{1.98 * 10^{20}}{7.342 * 10^{22}} \\
    &= \frac{1.98}{7.342} * \frac{10^{20}}{10^{22}} \\
    &= \frac{1.98}{7.342} * 10^{-2} \\
    &= 27.0 m/s^2
\end{split}
$$

This is the acceleration of the Moon.

#### Change the speed of the Earth and the Moon

We can use the following equation to calculate the speed of the Earth and the Moon.

$$
\begin{split}
    v &= a t
\end{split}
$$

    Where:
    - v is the speed of the Earth or the Moon
    - a is the acceleration of the Earth or the Moon
    - t is the time

$$
\begin{split}
    v &= a t \\
    &= 3.3155 * 10^{-5} * 1 \\
    &= 3.3155 * 10^{-5} m/s
\end{split}
$$

This is the speed of the Earth. The speed of the Moon is 27.0 m/s.

## 2D Simulation of the earth and the moon

We can use the following equation to calculate the 2D position of the Earth and the Moon at a given time

let's say the Earth is at the position (0, 0) and the Moon is at the position (384,400, 0).
384,400 km = is the distance between the Earth and the Moon, 384,400 km = 384,400 * 10^3 m

The simulation will be a python program so we must think in term of vectors

### The force between the Earth and the Moon

$$
    F = G \frac{m_1 m_2}{r^2} = 2 * 10^{20} N
$$

#### Calculate the x force

$$
    F_x = F * \frac{x}{r} = 2 * 10^{20} * \frac{384,400}{384,400} = 2 * 10^{20} N
$$

#### Calculate the y force

$$
    F_y = F * \frac{y}{r} = 2 * 10^{20} * \frac{0}{384,400} = 0 N
$$

### The acceleration of the Earth and the Moon

#### Calculate the x acceleration

$$
    a_x = \frac{F_x}{m} = \frac{2 * 10^{20}}{5.972 * 10^{24}} = 3.3155 * 10^{-5} m/s^2
$$

#### Calculate the y acceleration

$$
    a_y = \frac{F_y}{m} = \frac{0}{5.972 * 10^{24}} = 0 m/s^2
$$

### The speed of the Earth and the Moon

#### Calculate the x speed

$$
    v_x = a_x * t = 3.3155 * 10^{-5} * 1 = 3.3155 * 10^{-5} m/s
$$

#### Calculate the y speed

$$
    v_y = a_y * t = 0 * 1 = 0 m/s
$$

### The position of the Earth and the Moon

#### Calculate the x position

$$
    x = v_x * t = 3.3155 * 10^{-5} * 1 = 3.3155 * 10^{-5} m
$$

#### Calculate the y position

$$
    y = v_y * t = 0 * 1 = 0 m
$$

This is the position of the Earth and the Moon at a given time.
)