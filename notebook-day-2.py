import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return la, np, plt, sci, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4], 
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )    
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),                
                )
            )
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Équilibres du système

    On cherche les configurations dans lesquelles le booster peut rester immobile lorsque les entrées \(f\) et \(\phi\) sont constantes.

    Un équilibre correspond à une situation où, si le booster est placé dans cet état, il y reste sans bouger.
    Autrement dit, toutes les dérivées de l’état doivent être nulles :

    \[
    \dot{s}=0.
    \]

    L’état du booster est :

    \[
    s = (x, v_x, y, v_y, \theta, \omega),
    \]

    où :
    - \(x\) et \(y\) sont les coordonnées du centre de masse ;
    - \(v_x\) et \(v_y\) sont les vitesses du centre de masse ;
    - \(\theta\) est l’angle du booster par rapport à la verticale ;
    - \(\omega=\dot{\theta}\) est sa vitesse angulaire.

    Pour que le booster soit immobile, il faut d’abord que toutes les vitesses soient nulles :

    \[
    v_x=0,\qquad v_y=0,\qquad \omega=0.
    \]

    Mais cela ne suffit pas.
    Il faut aussi que les accélérations soient nulles, sinon le booster commencerait à bouger immédiatement après.

    Avec notre modèle, les accélérations sont :

    \[
    \ddot{x} = -\frac{f}{M}\sin(\theta+\phi),
    \]

    \[
    \ddot{y} = \frac{f}{M}\cos(\theta+\phi)-g,
    \]

    \[
    \ddot{\theta} = -\frac{\ell}{2J}f\sin(\phi).
    \]

    À l’équilibre, on impose donc :

    \[
    \ddot{x}=0,\qquad \ddot{y}=0,\qquad \ddot{\theta}=0.
    \]

    ---

    ### 1. Condition sur la rotation

    La condition \(\ddot{\theta}=0\) donne :

    \[
    -\frac{\ell}{2J}f\sin(\phi)=0.
    \]

    Comme on suppose :

    \[
    f>0,\qquad \ell>0,\qquad J>0,
    \]

    la seule possibilité est :

    \[
    \sin(\phi)=0.
    \]

    Or l’énoncé impose :

    \[
    |\phi|<\frac{\pi}{2}.
    \]

    Dans cet intervalle, la seule valeur qui annule le sinus est :

    \[
    \phi=0.
    \]

    Donc, à l’équilibre, la poussée doit être alignée avec l’axe du booster.
    Si \(\phi\neq 0\), la force serait désaxée et créerait un couple, ce qui ferait tourner le booster.

    ---

    ### 2. Condition sur le mouvement horizontal

    En remplaçant \(\phi=0\) dans l’équation horizontale, on obtient :

    \[
    \ddot{x} = -\frac{f}{M}\sin(\theta)=0.
    \]

    Comme \(f>0\), cela impose :

    \[
    \sin(\theta)=0.
    \]

    Or l’énoncé impose :

    \[
    |\theta|<\frac{\pi}{2}.
    \]

    Dans cet intervalle, la seule solution est :

    \[
    \theta=0.
    \]

    Donc, à l’équilibre, le booster doit être vertical.
    S’il était incliné, la poussée aurait une composante horizontale et le centre de masse commencerait à se déplacer latéralement.

    ---

    ### 3. Condition sur le mouvement vertical

    Avec \(\theta=0\) et \(\phi=0\), l’équation verticale devient :

    \[
    \ddot{y}=\frac{f}{M}-g.
    \]

    Pour avoir un équilibre, il faut :

    \[
    \ddot{y}=0.
    \]

    Donc :

    \[
    \frac{f}{M}-g=0,
    \]

    ce qui donne :

    \[
    f=Mg.
    \]

    La poussée doit donc compenser exactement le poids.
    Si \(f<Mg\), le booster descend.
    Si \(f>Mg\), le booster monte.

    ---

    ### Conclusion

    Les équilibres possibles sont donc :

    \[
    s_e=(x_e,0,y_e,0,0,0),
    \]

    avec les entrées constantes associées :

    \[
    f_e=Mg,\qquad \phi_e=0.
    \]

    Les positions \(x_e\) et \(y_e\) peuvent être quelconques, car le modèle ne dépend pas directement de la position absolue du booster.
    Autrement dit, le booster peut être en vol stationnaire à n’importe quelle position, tant qu’il est vertical, immobile, et que sa poussée compense exactement son poids.

    On peut donc résumer l’équilibre par :

    \[
    \theta=0,\qquad \phi=0,\qquad f=Mg,
    \]

    avec toutes les vitesses nulles.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modèle linéarisé autour de l’équilibre

    On considère l’équilibre générique :

    \[
    s_e=(x_e,0,y_e,0,0,0),
    \qquad
    f_e=Mg,
    \qquad
    \phi_e=0.
    \]

    On introduit les variables d’erreur suivantes :

    \[
    \Delta x = x-x_e,
    \qquad
    \Delta v_x = v_x,
    \]

    \[
    \Delta y = y-y_e,
    \qquad
    \Delta v_y = v_y,
    \]

    \[
    \Delta \theta = \theta,
    \qquad
    \Delta \omega = \omega,
    \]

    et les erreurs d’entrée :

    \[
    \Delta f = f-Mg,
    \qquad
    \Delta \phi = \phi.
    \]

    Le modèle non linéaire est donné par :

    \[
    \ddot{x} = -\frac{f}{M}\sin(\theta+\phi),
    \]

    \[
    \ddot{y} = \frac{f}{M}\cos(\theta+\phi)-g,
    \]

    \[
    \ddot{\theta} = -\frac{\ell}{2J}f\sin(\phi).
    \]

    Au voisinage de l’équilibre, on utilise les approximations :

    \[
    \sin(\theta+\phi) \simeq \Delta\theta+\Delta\phi,
    \qquad
    \sin(\phi) \simeq \Delta\phi,
    \qquad
    \cos(\theta+\phi) \simeq 1.
    \]

    En négligeant les termes d’ordre supérieur, on obtient les équations linéarisées :

    \[
    \Delta \dot{x} = \Delta v_x,
    \]

    \[
    \Delta \dot{v}_x = -g(\Delta\theta+\Delta\phi),
    \]

    \[
    \Delta \dot{y} = \Delta v_y,
    \]

    \[
    \Delta \dot{v}_y = \frac{1}{M}\Delta f,
    \]

    \[
    \Delta \dot{\theta} = \Delta \omega,
    \]

    \[
    \Delta \dot{\omega} = -\frac{\ell Mg}{2J}\Delta\phi.
    \]

    Comme pour une tige de longueur \(\ell\),

    \[
    J=\frac{1}{12}M\ell^2,
    \]

    on peut aussi écrire :

    \[
    \Delta \dot{\omega} = -\frac{6g}{\ell}\Delta\phi.
    \]

    Ainsi, le modèle linéarisé est :

    \[
    \boxed{
    \begin{aligned}
    \Delta \dot{x} &= \Delta v_x,\\
    \Delta \dot{v}_x &= -g\Delta\theta - g\Delta\phi,\\
    \Delta \dot{y} &= \Delta v_y,\\
    \Delta \dot{v}_y &= \frac{1}{M}\Delta f,\\
    \Delta \dot{\theta} &= \Delta \omega,\\
    \Delta \dot{\omega} &= -\frac{6g}{\ell}\Delta\phi.
    \end{aligned}
    }
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On écrit le modèle linéarisé sous la forme standard :

    \[
    \dot{X}=AX+BU.
    \]

    Le vecteur d’état d’erreur est :

    \[
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta v_x \\
    \Delta y \\
    \Delta v_y \\
    \Delta \theta \\
    \Delta \omega
    \end{bmatrix}.
    \]

    Les entrées du système sont la poussée \(f\) et l’angle de la tuyère \(\phi\).
    À l’équilibre, on a :

    \[
    f_e=Mg,
    \qquad
    \phi_e=0.
    \]

    On définit donc le vecteur d’entrée d’erreur :

    \[
    U =
    \begin{bmatrix}
    \Delta f \\
    \Delta \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    f-Mg \\
    \phi
    \end{bmatrix}.
    \]

    À partir du modèle linéarisé, on obtient :

    \[
    \Delta \dot{x} = \Delta v_x,
    \]

    \[
    \Delta \dot{v}_x = -g\Delta\theta - g\Delta\phi,
    \]

    \[
    \Delta \dot{y} = \Delta v_y,
    \]

    \[
    \Delta \dot{v}_y = \frac{1}{M}\Delta f,
    \]

    \[
    \Delta \dot{\theta} = \Delta \omega,
    \]

    \[
    \Delta \dot{\omega}
    =
    -\frac{Mg\ell}{2J}\Delta\phi.
    \]

    Ainsi, avant application numérique, les matrices du modèle linéarisé sont :

    \[
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix},
    \]

    \[
    B =
    \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \frac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\frac{Mg\ell}{2J}
    \end{bmatrix}.
    \]

    Avec les valeurs numériques du projet :

    \[
    M=1,\qquad g=1,\qquad \ell=2,
    \]

    et pour une tige de longueur \(\ell\) :

    \[
    J=\frac{1}{12}M\ell^2=\frac{1}{3}.
    \]

    On obtient alors :

    \[
    -\frac{Mg\ell}{2J}
    =
    -\frac{1\times 1\times 2}{2\times \frac{1}{3}}
    =
    -3.
    \]

    Les matrices numériques deviennent donc :

    \[
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix},
    \]

    et :

    \[
    B =
    \begin{bmatrix}
    0 & 0 \\
    0 & -1 \\
    0 & 0 \\
    1 & 0 \\
    0 & 0 \\
    0 & -3
    \end{bmatrix}.
    \]

    La matrice \(A\) décrit l’évolution naturelle des erreurs d’état, tandis que la matrice \(B\) décrit l’effet des variations d’entrée \(\Delta f\) et \(\Delta \phi\) sur la dynamique du booster.

    On remarque notamment que :
    - \(\Delta f\) agit directement sur l’accélération verticale \(\Delta \dot{v}_y\) ;
    - \(\Delta \phi\) agit sur l’accélération horizontale \(\Delta \dot{v}_x\) ;
    - \(\Delta \phi\) agit aussi sur l’accélération angulaire \(\Delta \dot{\omega}\), ce qui traduit l’effet de rotation causé par une poussée désaxée.
    """)
    return


@app.cell
def _(J, M, g, l, np):
    A = np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, -g,  0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ])

    B = np.array([
        [0.0, 0.0],
        [0.0, -g],
        [0.0, 0.0],
        [1.0 / M, 0.0],
        [0.0, 0.0],
        [0.0, -M * g * l / (2.0 * J)],
    ])



    A, B
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell
def _(A, la):
    eigenvalues = la.eigvals(A)
    eigenvalues
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    L’équilibre générique du booster n’est pas asymptotiquement stable.

    En effet, les équilibres du système sont de la forme :

    \[
    s_e=(x_e,0,y_e,0,0,0),
    \]

    avec :

    \[
    f_e=Mg,
    \qquad
    \phi_e=0.
    \]

    Les positions \(x_e\) et \(y_e\) sont quelconques. Il existe donc une infinité d’équilibres, et non un équilibre isolé.
    Ainsi, si on perturbe légèrement la position du booster, il n’y a pas de mécanisme naturel qui le ramène vers la position initiale.

    Cette conclusion est confirmée par le modèle linéarisé. Les valeurs propres de la matrice \(A\) sont toutes nulles :

    \[
    \lambda_i = 0.
    \]

    Or, pour qu’un système linéaire soit asymptotiquement stable, toutes les valeurs propres de sa matrice dynamique doivent avoir une partie réelle strictement négative :

    \[
    \operatorname{Re}(\lambda_i)<0.
    \]

    Ici, les valeurs propres sont sur l’axe imaginaire, précisément en zéro.
    Le système n’est donc pas asymptotiquement stable.

    Physiquement, cela signifie que le booster peut rester en vol stationnaire s’il est exactement vertical, immobile et avec une poussée égale à son poids, mais il ne revient pas naturellement à cet état après une perturbation.
    Il faudra donc concevoir un contrôleur pour stabiliser le système.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell
def _(A, B, np):
    def controllability_matrix(A, B):
        n = A.shape[0]
        return np.column_stack([
            np.linalg.matrix_power(A, k) @ B
            for k in range(n)
        ])


    Kc = controllability_matrix(A, B)
    rank_Kc = np.linalg.matrix_rank(Kc)

    Kc, rank_Kc
    return (controllability_matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La commandabilité signifie que l’on peut amener le système de n’importe quel état initial vers n’importe quel état cible en temps fini, en choisissant correctement la commande.

    Dans notre cas, le modèle linéarisé s’écrit sous la forme :

    \[
    \dot{X}=AX+BU,
    \]

    où :

    \[
    X =
    \begin{bmatrix}
    \Delta x \\
    \Delta v_x \\
    \Delta y \\
    \Delta v_y \\
    \Delta \theta \\
    \Delta \omega
    \end{bmatrix}
    \]

    est le vecteur d’état d’erreur, et :

    \[
    U =
    \begin{bmatrix}
    \Delta f \\
    \Delta \phi
    \end{bmatrix}
    \]

    est le vecteur de commande d’erreur.

    Pour tester la commandabilité, on utilise le critère de Kalman.
    D’après ce critère, le système est commandable si et seulement si la matrice de commandabilité :

    \[
    \mathcal{C}
    =
    \begin{bmatrix}
    B & AB & A^2B & A^3B & A^4B & A^5B
    \end{bmatrix}
    \]

    est de rang plein.

    Comme notre état est de dimension \(6\), la condition à vérifier est :

    \[
    \operatorname{rank}(\mathcal{C}) = 6.
    \]

    Ici, la matrice \(B\) est de taille \(6\times 2\).
    Ainsi, chaque bloc \(A^kB\) est aussi de taille \(6\times 2\), et la matrice de commandabilité complète est de taille :

    \[
    \mathcal{C}\in\mathbb{R}^{6\times 12}.
    \]

    Après calcul numérique, on obtient :

    \[
    \operatorname{rank}(\mathcal{C})=6.
    \]

    Le modèle linéarisé est donc commandable.

    Physiquement, cela signifie qu’au voisinage de l’équilibre, les deux commandes disponibles permettent d’agir sur tous les degrés de liberté du booster.
    La variation de poussée \(\Delta f\) agit principalement sur le mouvement vertical, tandis que la variation d’angle de tuyère \(\Delta \phi\) influence à la fois le mouvement horizontal et la rotation.

    Ainsi, même si l’équilibre n’est pas naturellement stable, il est théoriquement possible de concevoir une commande capable de ramener le booster vers l’état désiré.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell
def _(J, M, g, l, np):
    A_lat = np.array([
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, -g,  0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0],
    ])

    B_lat = np.array([
        [0.0],
        [-g],
        [0.0],
        [-M * g * l / (2.0 * J)],
    ])

    A_lat, B_lat
    return A_lat, B_lat


@app.cell
def _(A_lat, B_lat, controllability_matrix, np):
    C_lat = controllability_matrix(A_lat, B_lat)
    rank_C_lat = np.linalg.matrix_rank(C_lat)

    C_lat, rank_C_lat
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dans cette partie, on se limite à la dynamique latérale du booster.
    On ne contrôle plus directement la hauteur \(y\) ni la vitesse verticale \(\dot{y}\). On s’intéresse seulement à la position horizontale \(x\), à l’inclinaison \(\theta\), ainsi qu’à leurs dérivées.

    Le vecteur d’état réduit est donc :

    \[
    X_{\text{lat}} =
    \begin{bmatrix}
    \Delta x \\
    \Delta v_x \\
    \Delta \theta \\
    \Delta \omega
    \end{bmatrix}.
    \]

    On impose également :

    \[
    f=Mg,
    \]

    ce qui signifie que la poussée compense le poids.
    La seule commande restante est alors l’angle de la tuyère :

    \[
    U_{\text{lat}}=\Delta\phi.
    \]

    Le modèle réduit s’écrit sous la forme :

    \[
    \dot{X}_{\text{lat}} = A_{\text{lat}}X_{\text{lat}} + B_{\text{lat}}U_{\text{lat}}.
    \]

    Les matrices obtenues sont :

    \[
    A_{\text{lat}} =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix},
    \]

    \[
    B_{\text{lat}} =
    \begin{bmatrix}
    0 \\
    -g \\
    0 \\
    -\frac{Mg\ell}{2J}
    \end{bmatrix}.
    \]

    Avec les constantes du projet, on obtient :

    \[
    A_{\text{lat}} =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -1 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix},
    \qquad
    B_{\text{lat}} =
    \begin{bmatrix}
    0 \\
    -1 \\
    0 \\
    -3
    \end{bmatrix}.
    \]

    Pour vérifier la commandabilité, on utilise le critère de Kalman.
    La matrice de commandabilité est :

    \[
    \mathcal{C}_{\text{lat}} =
    \begin{bmatrix}
    B_{\text{lat}} &
    A_{\text{lat}}B_{\text{lat}} &
    A_{\text{lat}}^2B_{\text{lat}} &
    A_{\text{lat}}^3B_{\text{lat}}
    \end{bmatrix}.
    \]

    Comme l’état réduit est de dimension \(4\), le système est commandable si :

    \[
    \operatorname{rank}(\mathcal{C}_{\text{lat}})=4.
    \]

    Le calcul numérique donne bien :

    \[
    \operatorname{rank}(\mathcal{C}_{\text{lat}})=4.
    \]

    Le système latéral réduit est donc commandable.

    Cela signifie qu’en agissant uniquement sur l’angle de tuyère \(\phi\), on peut contrôler la position latérale \(x\), la vitesse latérale \(v_x\), l’angle \(\theta\) et la vitesse angulaire \(\omega\), au moins au voisinage de l’équilibre.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, sci):
    def linear_lateral_free_fall():
        t_span = [0.0, 5.0]

        X0 = np.array([
            0.0,        # x(0) in m
            0.0,        # vx(0) in m/s
            np.pi / 4,  # theta(0) in rad
            0.0,        # omega(0) in rad/s
        ])

        def dynamics(t, X):
            U = np.array([0.0])  # phi(t) = 0
            return A_lat @ X + B_lat @ U

        result = sci.solve_ivp(
            dynamics,
            t_span,
            X0,
            dense_output=True,
            max_step=0.01,
            rtol=1e-9,
            atol=1e-9,
        )

        t = np.linspace(t_span[0], t_span[1], 1000)
        X_t = result.sol(t)

        x_t = X_t[0]
        theta_t = X_t[2]

        fig, ax = plt.subplots(2, 1, figsize=(8, 6))

        # x(t)
        ax[0].plot(t, x_t, label=r"$x(t)$")
        ax[0].axhline(0, color="grey", ls="--")
        ax[0].set_xlabel("time $t$ (s)")
        ax[0].set_ylabel(r"$x(t)$ (m)")
        ax[0].set_title("Lateral position")
        ax[0].grid(True)
        ax[0].legend()

        # theta(t)
        ax[1].plot(t, theta_t, label=r"$\theta(t)$")
        ax[1].axhline(np.pi / 4, color="grey", ls="--", label=r"$\pi/4$")
        ax[1].set_xlabel("time $t$ (s)")
        ax[1].set_ylabel(r"$\theta(t)$ (rad)")
        ax[1].set_title("Tilt angle")
        ax[1].grid(True)
        ax[1].legend()

        fig.suptitle(r"Linearized lateral model with $\phi(t)=0$", fontsize=14)
        fig.tight_layout()

        return fig

    linear_lateral_free_fall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On considère le modèle latéral linéarisé réduit :

    \[
    X_{\text{lat}} =
    \begin{bmatrix}
    \Delta x \\
    \Delta v_x \\
    \Delta \theta \\
    \Delta \omega
    \end{bmatrix},
    \qquad
    \dot{X}_{\text{lat}} = A_{\text{lat}}X_{\text{lat}} + B_{\text{lat}}\Delta\phi.
    \]

    Dans ce scénario, on impose :

    \[
    \phi(t)=0,
    \]

    donc :

    \[
    \Delta\phi(t)=0.
    \]

    Le système évolue alors librement selon :

    \[
    \dot{X}_{\text{lat}} = A_{\text{lat}}X_{\text{lat}}.
    \]

    Avec les équations du modèle réduit, on obtient :

    \[
    \dot{x}=v_x,
    \]

    \[
    \dot{v}_x=-g\theta,
    \]

    \[
    \dot{\theta}=\omega,
    \]

    \[
    \dot{\omega}=0.
    \]

    Les conditions initiales sont :

    \[
    x(0)=0,\qquad v_x(0)=0,
    \]

    \[
    \theta(0)=\frac{\pi}{4},\qquad \omega(0)=0.
    \]

    Comme :

    \[
    \dot{\omega}=0
    \]

    et que :

    \[
    \omega(0)=0,
    \]

    on obtient :

    \[
    \omega(t)=0.
    \]

    Donc :

    \[
    \dot{\theta}(t)=0.
    \]

    Ainsi, l’angle reste constant :

    \[
    \theta(t)=\frac{\pi}{4}.
    \]

    Ensuite, l’accélération latérale est donnée par :

    \[
    \ddot{x}(t)=\dot{v}_x(t)=-g\theta(t).
    \]

    Comme \(\theta(t)=\frac{\pi}{4}\), on a :

    \[
    \ddot{x}(t)=-g\frac{\pi}{4}.
    \]

    Avec \(g=1\), cela devient :

    \[
    \ddot{x}(t)=-\frac{\pi}{4}.
    \]

    En intégrant une première fois :

    \[
    \dot{x}(t)=v_x(t)=-\frac{\pi}{4}t+v_x(0).
    \]

    Comme \(v_x(0)=0\), on obtient :

    \[
    v_x(t)=-\frac{\pi}{4}t.
    \]

    En intégrant une deuxième fois :

    \[
    x(t)=-\frac{1}{2}\frac{\pi}{4}t^2+x(0).
    \]

    Comme \(x(0)=0\), la solution analytique est :

    \[
    x(t)=-\frac{\pi}{8}t^2.
    \]

    Ainsi, les courbes obtenues sont cohérentes avec les solutions analytiques :

    \[
    \boxed{\theta(t)=\frac{\pi}{4}}
    \]

    et :

    \[
    \boxed{x(t)=-\frac{\pi}{8}t^2}.
    \]

    Sur le graphique, on observe donc que :

    - \(\Delta\theta(t)\) reste constant à \(\pi/4\), c’est-à-dire à \(45^\circ\).
      L’inclinaison initiale ne change donc pas au cours du temps.

    - \(\Delta x(t)\) suit une trajectoire parabolique.
      Cela signifie que le booster subit une accélération latérale constante.

    Physiquement, cela s’explique par l’absence de commande sur \(\phi\).
    Comme \(\phi(t)=0\), aucun couple n’est généré pour ramener le booster à la verticale. L’angle \(\theta\) reste donc bloqué à sa valeur initiale.

    Cependant, comme le booster est incliné, la poussée alignée avec son axe n’est plus parfaitement verticale. Elle possède une composante horizontale permanente, ce qui entraîne une dérive latérale continue du centre de masse.

    À \(t=5\), on obtient :

    \[
    x(5)=-\frac{\pi}{8}\times 25 \approx -9.82\ \text{m}.
    \]

    Cette valeur correspond bien à la courbe numérique obtenue.

    Ce comportement montre que, sans contrôleur, le booster ne corrige pas naturellement son inclinaison initiale. C’est précisément cette dérive et cette absence de correction que l’on cherchera à compenser avec une loi de commande.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧩 Contrôleur réglé manuellement — Analyse théorique

    On cherche à stabiliser l’inclinaison du booster à l’aide d’un contrôleur réglé manuellement.

    On travaille avec le modèle latéral réduit :

    \[
    X_{\text{lat}} =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}
    \]

    et la seule commande disponible est l’angle de la tuyère :

    \[
    \Delta \phi.
    \]

    L’énoncé impose une matrice de gain de la forme :

    \[
    K =
    \begin{bmatrix}
    0 & 0 & k_3 & k_4
    \end{bmatrix}.
    \]

    Les deux premiers coefficients sont nuls, car on ne cherche pas encore à contrôler la position latérale \(\Delta x\).
    On cherche uniquement à corriger l’inclinaison \(\Delta \theta\) et la vitesse angulaire \(\Delta \dot{\theta}\).

    La loi de commande est donc :

    \[
    \Delta \phi(t)
    =
    -KX_{\text{lat}}(t).
    \]

    C’est-à-dire :

    \[
    \Delta \phi(t)
    =
    -k_3\Delta\theta(t)
    -
    k_4\Delta\dot{\theta}(t).
    \]

    Dans le modèle linéarisé, la dynamique angulaire est donnée par :

    \[
    \Delta \ddot{\theta}
    =
    -\frac{Mg\ell}{2J}\Delta\phi.
    \]

    On pose :

    \[
    c=\frac{Mg\ell}{2J}.
    \]

    Avec les valeurs du projet :

    \[
    M=1,\qquad g=1,\qquad \ell=2,\qquad J=\frac{1}{3},
    \]

    on obtient :

    \[
    c=3.
    \]

    En remplaçant la loi de commande dans l’équation angulaire :

    \[
    \Delta \ddot{\theta}
    =
    -c\Delta\phi,
    \]

    on obtient :

    \[
    \Delta \ddot{\theta}
    =
    c k_3\Delta\theta
    +
    c k_4\Delta\dot{\theta}.
    \]

    Le sous-système angulaire en boucle fermée est donc :

    \[
    \frac{d}{dt}
    \begin{bmatrix}
    \Delta\theta \\
    \Delta\dot{\theta}
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 1 \\
    c k_3 & c k_4
    \end{bmatrix}
    \begin{bmatrix}
    \Delta\theta \\
    \Delta\dot{\theta}
    \end{bmatrix}.
    \]

    Son équation caractéristique est :

    \[
    \lambda^2 - c k_4 \lambda - c k_3 = 0.
    \]

    Pour que l’inclinaison converge vers zéro, les deux racines de cette équation doivent avoir une partie réelle négative.

    En comparant avec :

    \[
    (\lambda-\lambda_1)(\lambda-\lambda_2)
    =
    \lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2,
    \]

    on obtient :

    \[
    \lambda_1+\lambda_2 = c k_4,
    \]

    et :

    \[
    \lambda_1\lambda_2 = -c k_3.
    \]

    Pour avoir deux racines avec une partie réelle négative, il faut que leur somme soit négative et que leur produit soit positif :

    \[
    \lambda_1+\lambda_2 = c k_4 < 0,
    \]

    donc, comme \(c>0\) :

    \[
    k_4<0.
    \]

    De même :

    \[
    \lambda_1\lambda_2 = -c k_3 > 0,
    \]

    donc, comme \(c>0\) :

    \[
    k_3<0.
    \]

    Ainsi, les deux coefficients \(k_3\) et \(k_4\) doivent être négatifs.

    Le coefficient \(k_3\) agit principalement comme une correction de position angulaire, tandis que \(k_4\) joue un rôle d’amortissement lié à la vitesse angulaire.
    """)
    return


@app.cell
def _(A_lat, B_lat, la, np, plt, sci):
    def simulate_manual_controller(K_manual, t_final=30.0):
        t_span = [0.0, t_final]

        X0 = np.array([
            0.0,        # Delta x(0)
            0.0,        # Delta x_dot(0)
            np.pi / 4,  # Delta theta(0)
            0.0,        # Delta theta_dot(0)
        ])

        def closed_loop_dynamics(t, X):
            delta_phi = -K_manual @ X
            return A_lat @ X + B_lat.flatten() * delta_phi

        result = sci.solve_ivp(
            closed_loop_dynamics,
            t_span,
            X0,
            dense_output=True,
            max_step=0.01,
            rtol=1e-9,
            atol=1e-9,
        )

        t = np.linspace(t_span[0], t_span[1], 2000)
        X_t = result.sol(t)

        delta_x = X_t[0]
        delta_x_dot = X_t[1]
        delta_theta = X_t[2]
        delta_theta_dot = X_t[3]

        delta_phi = np.array([
            -K_manual @ X_t[:, i]
            for i in range(X_t.shape[1])
        ])

        return t, delta_x, delta_x_dot, delta_theta, delta_theta_dot, delta_phi


    K_tests = [
        np.array([0.0, 0.0, -0.03, -0.15]),
        np.array([0.0, 0.0, -0.05, -0.25]),
        np.array([0.0, 0.0, -0.07, -0.30]),
    ]

    fig, ax = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

    results_manual = []

    for K_manual in K_tests:
        t, delta_x, delta_x_dot, delta_theta, delta_theta_dot, delta_phi = simulate_manual_controller(K_manual)

        A_cl_test = A_lat - B_lat @ K_manual.reshape(1, 4)
        eigvals_test = la.eigvals(A_cl_test)

        max_theta = np.max(np.abs(delta_theta))
        max_phi = np.max(np.abs(delta_phi))
        theta_at_20s = delta_theta[np.argmin(np.abs(t - 20.0))]

        constraints_ok = (max_theta < np.pi / 2) and (max_phi < np.pi / 2)

        results_manual.append({
            "K": K_manual,
            "max_theta": max_theta,
            "max_phi": max_phi,
            "theta_at_20s": theta_at_20s,
            "constraints_ok": constraints_ok,
            "eigvals_test": eigvals_test,
        })

        label = rf"$k_3={K_manual[2]:.2f},\ k_4={K_manual[3]:.2f}$"

        ax[0].plot(t, delta_theta, label=label)
        ax[1].plot(t, delta_phi, label=label)
        ax[2].plot(t, delta_x, label=label)


    ax[0].axhline(0, color="black", ls=":")
    ax[0].axhline(np.pi / 2, color="grey", ls="--", label=r"$\pm \pi/2$")
    ax[0].axhline(-np.pi / 2, color="grey", ls="--")
    ax[0].set_ylabel(r"$\Delta\theta(t)$ (rad)")
    ax[0].set_title("Essais manuels du contrôleur")
    ax[0].grid(True)
    ax[0].legend()

    ax[1].axhline(0, color="black", ls=":")
    ax[1].axhline(np.pi / 2, color="grey", ls="--", label=r"$\pm \pi/2$")
    ax[1].axhline(-np.pi / 2, color="grey", ls="--")
    ax[1].set_ylabel(r"$\Delta\phi(t)$ (rad)")
    ax[1].grid(True)
    ax[1].legend()

    ax[2].axhline(0, color="black", ls=":")
    ax[2].set_xlabel("time $t$ (s)")
    ax[2].set_ylabel(r"$\Delta x(t)$ (m)")
    ax[2].grid(True)
    ax[2].legend()

    fig.tight_layout()

    for i, res in enumerate(results_manual, start=1):
        print(f"Essai {i}")
        print("K =", res["K"])
        print("max |Delta theta| =", res["max_theta"])
        print("max |Delta phi| =", res["max_phi"])
        print("Delta theta at t=20s =", res["theta_at_20s"])
        print("Constraints OK:", res["constraints_ok"])
        print("Eigenvalues:", res["eigvals_test"])
        print("-" * 50)

    fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interprétation des essais manuels

    Les coefficients \(k_3\) et \(k_4\) sont choisis par réglage manuel progressif.
    L’analyse théorique montre qu’ils doivent être négatifs pour stabiliser le sous-système angulaire, mais elle ne donne pas directement les meilleures valeurs numériques.

    Nous testons donc plusieurs paires de gains négatifs afin de comparer :
    - la vitesse de convergence de \(\Delta\theta(t)\) vers zéro ;
    - le respect de la contrainte \(|\Delta\theta(t)|<\pi/2\) ;
    - le respect de la contrainte \(|\Delta\phi(t)|<\pi/2\) ;
    - le comportement de la position latérale \(\Delta x(t)\), même si elle n’est pas l’objectif principal ici.

    Les trois essais donnent des commandes admissibles, car dans tous les cas :

    \[
    \max|\Delta\theta(t)| < \frac{\pi}{2},
    \qquad
    \max|\Delta\phi(t)| < \frac{\pi}{2}.
    \]

    L’essai 1, avec :

    \[
    K=[0,0,-0.03,-0.15],
    \]

    stabilise l’angle, mais la convergence est plus lente. À \(t=20\) s, il reste encore :

    \[
    \Delta\theta(20)\approx -0.013 \text{ rad}.
    \]

    L’essai 2, avec :

    \[
    K=[0,0,-0.05,-0.25],
    \]

    donne une convergence plus rapide :

    \[
    \Delta\theta(20)\approx 0.0014 \text{ rad}.
    \]

    L’essai 3, avec :

    \[
    K=[0,0,-0.07,-0.30],
    \]

    donne la meilleure convergence parmi les trois essais :

    \[
    \Delta\theta(20)\approx 0.00048 \text{ rad}.
    \]

    La commande reste également très faible devant la limite imposée :

    \[
    \max|\Delta\phi(t)|\approx 0.055 \text{ rad} \ll \frac{\pi}{2}.
    \]

    On retient donc le troisième choix :

    \[
    K_{\text{manual}}=[0,0,-0.07,-0.30].
    \]

    Ce choix permet de redresser le booster en moins de 20 secondes tout en respectant les contraintes de l’énoncé.

    Cependant, on observe aussi que \(\Delta x(t)\) continue à dériver. Cela est normal, car les deux premiers coefficients de \(K\) sont nuls : le contrôleur agit uniquement sur l’angle \(\Delta\theta\) et la vitesse angulaire \(\Delta\dot{\theta}\), mais ne cherche pas encore à ramener le booster vers une position latérale donnée.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### résultat retenu ###
    """)
    return


@app.cell
def _(np):
    K_manual_final = np.array([0.0, 0.0, -0.07, -0.30])
    K_manual_final
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧩 Contrôleur par placement de pôles — Principe

    Dans la question précédente, on avait choisi un contrôleur manuel de la forme :

    \[
    K =
    \begin{bmatrix}
    0 & 0 & k_3 & k_4
    \end{bmatrix}.
    \]

    Ce contrôleur permettait de stabiliser l’angle \(\Delta\theta\), mais il ne contrôlait pas directement la position latérale \(\Delta x\).
    C’est pour cela que le booster pouvait encore dériver horizontalement.

    Dans cette question, on cherche un contrôleur plus complet :

    \[
    K_{pp} =
    \begin{bmatrix}
    k_1 & k_2 & k_3 & k_4
    \end{bmatrix}.
    \]

    La loi de commande devient :

    \[
    \Delta\phi(t)
    =
    -K_{pp}
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix}.
    \]

    Cette fois-ci, la commande dépend aussi de \(\Delta x\) et \(\Delta \dot{x}\).
    L’objectif est donc double :

    1. ramener l’inclinaison \(\Delta\theta(t)\) vers zéro ;
    2. ramener aussi la position latérale \(\Delta x(t)\) vers zéro.

    Le système en boucle fermée s’écrit :

    \[
    \dot{X}_{\text{lat}}
    =
    (A_{\text{lat}} - B_{\text{lat}}K_{pp})X_{\text{lat}}.
    \]

    Pour que le système soit asymptotiquement stable, toutes les valeurs propres de la matrice :

    \[
    A_{\text{cl}} = A_{\text{lat}} - B_{\text{lat}}K_{pp}
    \]

    doivent avoir une partie réelle strictement négative.

    La méthode du placement de pôles consiste à choisir à l’avance les valeurs propres souhaitées du système bouclé, puis à calculer automatiquement le gain \(K_{pp}\) correspondant.

    Ici, on choisit par exemple les pôles :

    \[
    p_1=-0.4,\qquad
    p_2=-0.4+0.3i,\qquad
    p_3=-0.4-0.3i,\qquad
    p_4=-0.8.
    \]

    Ces pôles sont tous dans le demi-plan gauche, donc ils assurent la stabilité asymptotique.
    Leur partie réelle est de l’ordre de \(-0.4\), ce qui donne une convergence compatible avec l’objectif d’environ 20 secondes.

    Les pôles complexes conjugués permettent d’obtenir une réponse légèrement oscillante mais amortie, tandis que le pôle \(-0.8\) apporte une dynamique plus rapide.
    """)
    return


@app.cell
def _(A_lat, B_lat, la, np, plt, sci, scipy):
    def run_pole_placement_controller():
        desired_poles = np.array([
            -0.4,
            -0.4 + 0.3j,
            -0.4 - 0.3j,
            -0.8,
        ])

        pole_result = scipy.signal.place_poles(A_lat, B_lat, desired_poles)
        K_pp = pole_result.gain_matrix

        A_cl_pp = A_lat - B_lat @ K_pp
        eigvals_pp = la.eigvals(A_cl_pp)

        t_span = [0.0, 30.0]

        X0 = np.array([
            0.0,        # Delta x(0)
            0.0,        # Delta x_dot(0)
            np.pi / 4,  # Delta theta(0)
            0.0,        # Delta theta_dot(0)
        ])

        def closed_loop_dynamics(t, X):
            delta_phi_value = -(K_pp @ X)[0]
            return A_lat @ X + B_lat.flatten() * delta_phi_value

        result = sci.solve_ivp(
            closed_loop_dynamics,
            t_span,
            X0,
            dense_output=True,
            max_step=0.01,
            rtol=1e-9,
            atol=1e-9,
        )

        t_values = np.linspace(t_span[0], t_span[1], 3000)
        X_values = result.sol(t_values)

        delta_x_values = X_values[0]
        delta_x_dot_values = X_values[1]
        delta_theta_values = X_values[2]
        delta_theta_dot_values = X_values[3]

        delta_phi_values = np.array([
            -(K_pp @ X_values[:, i])[0]
            for i in range(X_values.shape[1])
        ])

        max_theta = np.max(np.abs(delta_theta_values))
        max_phi = np.max(np.abs(delta_phi_values))
        x_at_20s = delta_x_values[np.argmin(np.abs(t_values - 20.0))]
        theta_at_20s = delta_theta_values[np.argmin(np.abs(t_values - 20.0))]

        fig_pp, ax_pp = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

        ax_pp[0].plot(t_values, delta_theta_values, label=r"$\Delta\theta(t)$")
        ax_pp[0].axhline(0, color="black", ls=":")
        ax_pp[0].axhline(np.pi / 2, color="grey", ls="--", label=r"$\pm\pi/2$")
        ax_pp[0].axhline(-np.pi / 2, color="grey", ls="--")
        ax_pp[0].set_ylabel(r"$\Delta\theta(t)$ (rad)")
        ax_pp[0].grid(True)
        ax_pp[0].legend()

        ax_pp[1].plot(t_values, delta_phi_values, label=r"$\Delta\phi(t)$")
        ax_pp[1].axhline(0, color="black", ls=":")
        ax_pp[1].axhline(np.pi / 2, color="grey", ls="--", label=r"$\pm\pi/2$")
        ax_pp[1].axhline(-np.pi / 2, color="grey", ls="--")
        ax_pp[1].set_ylabel(r"$\Delta\phi(t)$ (rad)")
        ax_pp[1].grid(True)
        ax_pp[1].legend()

        ax_pp[2].plot(t_values, delta_x_values, label=r"$\Delta x(t)$")
        ax_pp[2].axhline(0, color="black", ls=":")
        ax_pp[2].set_xlabel("time $t$ (s)")
        ax_pp[2].set_ylabel(r"$\Delta x(t)$ (m)")
        ax_pp[2].grid(True)
        ax_pp[2].legend()

        fig_pp.suptitle("Contrôleur par placement de pôles")
        fig_pp.tight_layout()

        print("Desired poles:", desired_poles)
        print("K_pp =", K_pp)
        print("Closed-loop eigenvalues:", eigvals_pp)
        print("max |Delta theta| =", max_theta)
        print("max |Delta phi| =", max_phi)
        print("Delta theta at t=20s =", theta_at_20s)
        print("Delta x at t=20s =", x_at_20s)
        print("Constraints OK:", (max_theta < np.pi / 2) and (max_phi < np.pi / 2))
        print("Asymptotically stable:", np.all(np.real(eigvals_pp) < 0))

        return fig_pp, K_pp, eigvals_pp


    pole_placement_fig, K_pp, eigvals_pp = run_pole_placement_controller()
    pole_placement_fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Les graphes confirment ce résultat.
    L’inclinaison \(\Delta\theta(t)\) converge vers zéro après une réponse légèrement oscillante. Cette oscillation est cohérente avec la présence des pôles complexes conjugués :

    \[
    -0.4 \pm 0.3i.
    \]

    La commande \(\Delta\phi(t)\) reste toujours dans les limites autorisées. En effet, on obtient :

    \[
    \max |\Delta\phi(t)| \approx 0.408 \text{ rad}
    \]

    ce qui est largement inférieur à :

    \[
    \frac{\pi}{2} \approx 1.57 \text{ rad}.
    \]

    La contrainte sur l’inclinaison est également respectée :

    \[
    \max |\Delta\theta(t)| = \frac{\pi}{4} < \frac{\pi}{2}.
    \]

    On observe aussi que la position latérale \(\Delta x(t)\), contrairement au cas du contrôleur manuel, revient vers zéro.
    Elle présente d’abord une dérive transitoire, atteignant environ \(-3\) m, puis elle est progressivement corrigée par le contrôleur.

    À \(t=20\) s, les valeurs obtenues sont :

    \[
    \Delta\theta(20) \approx 0.0030 \text{ rad},
    \]

    et :

    \[
    \Delta x(20) \approx -0.0039 \text{ m}.
    \]

    Ces valeurs sont très proches de zéro, ce qui montre que l’objectif de convergence en moins de 20 secondes est atteint.

    Ainsi, le placement de pôles permet d’améliorer le contrôleur manuel :
    le booster ne se contente plus de se redresser, il revient également vers sa position latérale d’équilibre.
    Le système latéral en boucle fermée est donc asymptotiquement stable et respecte les contraintes imposées sur \(\Delta\theta(t)\) et \(\Delta\phi(t)\).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧩 Contrôleur par contrôle optimal — Principe

    On cherche maintenant à construire un contrôleur à l’aide du contrôle optimal, plus précisément avec une approche de type LQR.

    Le modèle latéral réduit s’écrit :

    \[
    \dot{X}_{\text{lat}} = A_{\text{lat}}X_{\text{lat}} + B_{\text{lat}}\Delta\phi,
    \]

    avec :

    \[
    X_{\text{lat}} =
    \begin{bmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{bmatrix}.
    \]

    La loi de commande est encore un retour d’état :

    \[
    \Delta\phi(t)=-K_{oc}X_{\text{lat}}(t).
    \]

    En contrôle optimal, le gain \(K_{oc}\) n’est pas choisi directement.
    On choisit plutôt deux matrices de pondération \(Q\) et \(R\), puis le gain est calculé automatiquement.

    La matrice \(Q\) pénalise les erreurs d’état :

    \[
    X_{\text{lat}}^TQX_{\text{lat}},
    \]

    tandis que la matrice \(R\) pénalise l’amplitude de la commande :

    \[
    \Delta\phi(t)^TR\Delta\phi(t).
    \]

    Le critère à minimiser est donc :

    \[
    J =
    \int_0^{+\infty}
    \left(
    X_{\text{lat}}(t)^T Q X_{\text{lat}}(t)
    +
    \Delta\phi(t)^T R \Delta\phi(t)
    \right)dt.
    \]

    Le choix de \(Q\) et \(R\) traduit un compromis :
    - si on augmente les coefficients de \(Q\), on demande au système de corriger plus fortement certaines erreurs d’état ;
    - si on augmente \(R\), on pénalise davantage la commande, ce qui évite d’avoir une valeur trop grande de \(\Delta\phi(t)\).

    Comme l’énoncé impose :

    \[
    |\Delta\phi(t)|<\frac{\pi}{2},
    \]

    il faut éviter une commande trop agressive.
    On teste donc plusieurs choix de \(Q\) et \(R\), puis on garde un réglage qui assure :
    - la convergence de \(\Delta\theta(t)\) vers zéro ;
    - la convergence de \(\Delta x(t)\) vers zéro ;
    - une convergence en moins de 20 secondes ;
    - le respect de la contrainte sur \(\Delta\phi(t)\).
    """)
    return


@app.cell
def _(A_lat, B_lat, la, np, plt, sci, scipy):
    def run_optimal_control_tests():
        def lqr_gain_local(A, B, Q, R):
            P = scipy.linalg.solve_continuous_are(A, B, Q, R)
            K = np.linalg.solve(R, B.T @ P)
            return K

        def simulate_lqr_local(K_oc, t_final=30.0):
            t_span = [0.0, t_final]

            X0 = np.array([
                0.0,        # Delta x(0)
                0.0,        # Delta x_dot(0)
                np.pi / 4,  # Delta theta(0)
                0.0,        # Delta theta_dot(0)
            ])

            def closed_loop_dynamics(t, X):
                delta_phi_value = -(K_oc @ X)[0]
                return A_lat @ X + B_lat.flatten() * delta_phi_value

            result = sci.solve_ivp(
                closed_loop_dynamics,
                t_span,
                X0,
                dense_output=True,
                max_step=0.01,
                rtol=1e-9,
                atol=1e-9,
            )

            t_values = np.linspace(t_span[0], t_span[1], 3000)
            X_values = result.sol(t_values)

            delta_x_values = X_values[0]
            delta_x_dot_values = X_values[1]
            delta_theta_values = X_values[2]
            delta_theta_dot_values = X_values[3]

            delta_phi_values = np.array([
                -(K_oc @ X_values[:, i])[0]
                for i in range(X_values.shape[1])
            ])

            return (
                t_values,
                delta_x_values,
                delta_x_dot_values,
                delta_theta_values,
                delta_theta_dot_values,
                delta_phi_values,
            )

        test_parameters = [
            {
                "name": "Essai 1",
                "Q": np.diag([0.25, 0.10, 1.62, 1.0]),
                "R": np.array([[2.0]]),
            },
            {
                "name": "Essai 2",
                "Q": np.diag([0.25, 0.10, 1.62, 1.0]),
                "R": np.array([[5.0]]),
            },
            {
                "name": "Essai 3",
                "Q": np.diag([0.50, 0.10, 8.00, 1.0]),
                "R": np.array([[10.0]]),
            },
        ]

        fig_oc, ax_oc = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

        oc_results = []

        for test in test_parameters:
            Q = test["Q"]
            R = test["R"]

            K_oc = lqr_gain_local(A_lat, B_lat, Q, R)

            A_cl_oc = A_lat - B_lat @ K_oc
            eigvals_oc = la.eigvals(A_cl_oc)

            (
                t_values,
                delta_x_values,
                delta_x_dot_values,
                delta_theta_values,
                delta_theta_dot_values,
                delta_phi_values,
            ) = simulate_lqr_local(K_oc)

            max_theta = np.max(np.abs(delta_theta_values))
            max_phi = np.max(np.abs(delta_phi_values))
            theta_at_20s = delta_theta_values[np.argmin(np.abs(t_values - 20.0))]
            x_at_20s = delta_x_values[np.argmin(np.abs(t_values - 20.0))]

            constraints_ok = (max_theta < np.pi / 2) and (max_phi < np.pi / 2)
            stable = np.all(np.real(eigvals_oc) < 0)

            oc_results.append({
                "name": test["name"],
                "Q": Q,
                "R": R,
                "K_oc": K_oc,
                "eigvals_oc": eigvals_oc,
                "max_theta": max_theta,
                "max_phi": max_phi,
                "theta_at_20s": theta_at_20s,
                "x_at_20s": x_at_20s,
                "constraints_ok": constraints_ok,
                "stable": stable,
            })

            label = test["name"]

            ax_oc[0].plot(t_values, delta_theta_values, label=label)
            ax_oc[1].plot(t_values, delta_phi_values, label=label)
            ax_oc[2].plot(t_values, delta_x_values, label=label)

        ax_oc[0].axhline(0, color="black", ls=":")
        ax_oc[0].axhline(np.pi / 2, color="grey", ls="--", label=r"$\pm\pi/2$")
        ax_oc[0].axhline(-np.pi / 2, color="grey", ls="--")
        ax_oc[0].set_ylabel(r"$\Delta\theta(t)$ (rad)")
        ax_oc[0].set_title("Essais du contrôleur optimal LQR")
        ax_oc[0].grid(True)
        ax_oc[0].legend()

        ax_oc[1].axhline(0, color="black", ls=":")
        ax_oc[1].axhline(np.pi / 2, color="grey", ls="--", label=r"$\pm\pi/2$")
        ax_oc[1].axhline(-np.pi / 2, color="grey", ls="--")
        ax_oc[1].set_ylabel(r"$\Delta\phi(t)$ (rad)")
        ax_oc[1].grid(True)
        ax_oc[1].legend()

        ax_oc[2].axhline(0, color="black", ls=":")
        ax_oc[2].set_xlabel("time $t$ (s)")
        ax_oc[2].set_ylabel(r"$\Delta x(t)$ (m)")
        ax_oc[2].grid(True)
        ax_oc[2].legend()

        fig_oc.tight_layout()

        for res in oc_results:
            print(res["name"])
            print("Q =")
            print(res["Q"])
            print("R =")
            print(res["R"])
            print("K_oc =", res["K_oc"])
            print("Closed-loop eigenvalues:", res["eigvals_oc"])
            print("max |Delta theta| =", res["max_theta"])
            print("max |Delta phi| =", res["max_phi"])
            print("Delta theta at t=20s =", res["theta_at_20s"])
            print("Delta x at t=20s =", res["x_at_20s"])
            print("Constraints OK:", res["constraints_ok"])
            print("Asymptotically stable:", res["stable"])
            print("-" * 50)

        return fig_oc, oc_results


    optimal_control_fig, optimal_control_results = run_optimal_control_tests()
    optimal_control_fig
    return (optimal_control_results,)


@app.cell
def _(optimal_control_results):
    K_oc_final = optimal_control_results[2]["K_oc"]
    eigvals_oc_final = optimal_control_results[2]["eigvals_oc"]

    K_oc_final, eigvals_oc_final
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interprétation

    ### Essai 1

    Pour le premier essai, on utilise :

    \[
    Q=\operatorname{diag}(0.25,\ 0.1,\ 1.62,\ 1),
    \qquad
    R=2.
    \]

    Le gain obtenu est :

    \[
    K_{oc}
    =
    \begin{bmatrix}
    0.354 & 1.244 & -2.116 & -1.770
    \end{bmatrix}.
    \]

    Les valeurs propres de la boucle fermée ont toutes une partie réelle négative :

    \[
    -1.57 \pm 0.48i,
    \qquad
    -0.46 \pm 0.42i.
    \]

    Le système est donc asymptotiquement stable.
    Cependant, la commande maximale vaut :

    \[
    \max |\Delta\phi(t)| \approx 1.66 \text{ rad}.
    \]

    Or :

    \[
    \frac{\pi}{2}\approx 1.57 \text{ rad}.
    \]

    La contrainte sur la commande n’est donc pas respectée.
    Cet essai est trop agressif : la commande corrige très rapidement le système, mais elle dépasse la limite autorisée.



    ### Essai 2

    Pour limiter la commande, on augmente \(R\) :

    \[
    Q=\operatorname{diag}(0.25,\ 0.1,\ 1.62,\ 1),
    \qquad
    R=5.
    \]

    Le gain devient :

    \[
    K_{oc}
    =
    \begin{bmatrix}
    0.224 & 0.823 & -1.469 & -1.338
    \end{bmatrix}.
    \]

    La commande maximale est maintenant :

    \[
    \max |\Delta\phi(t)| \approx 1.15 \text{ rad},
    \]

    ce qui respecte bien la contrainte :

    \[
    |\Delta\phi(t)|<\frac{\pi}{2}.
    \]

    Les valeurs propres ont toujours une partie réelle strictement négative :

    \[
    -1.13 \pm 0.63i,
    \qquad
    -0.47 \pm 0.43i.
    \]

    Le système reste donc asymptotiquement stable.
    À \(t=20\) s, on obtient :

    \[
    \Delta\theta(20) \approx 6.5\times 10^{-5} \text{ rad},
    \]

    et :

    \[
    \Delta x(20) \approx -5.4\times 10^{-4} \text{ m}.
    \]

    Ces deux valeurs sont pratiquement nulles, donc l’objectif de convergence en moins de 20 s est atteint.



    ### Essai 3

    Dans le troisième essai, on augmente la pénalisation sur \(\Delta\theta\) :

    \[
    Q=\operatorname{diag}(0.5,\ 0.1,\ 8,\ 1),
    \qquad
    R=10.
    \]

    Le gain obtenu est :

    \[
    K_{oc}
    =
    \begin{bmatrix}
    0.224 & 0.869 & -1.668 & -1.368
    \end{bmatrix}.
    \]

    Ce choix pénalise davantage l’inclinaison du booster, tout en gardant un \(R\) suffisamment grand pour limiter la commande.

    La commande maximale vaut :

    \[
    \max |\Delta\phi(t)| \approx 1.31 \text{ rad},
    \]

    ce qui reste inférieur à :

    \[
    \frac{\pi}{2}\approx 1.57 \text{ rad}.
    \]

    Les valeurs propres sont :

    \[
    -1.25 \pm 1.06i,
    \qquad
    -0.37 \pm 0.34i.
    \]

    Toutes leurs parties réelles sont négatives, donc le système est asymptotiquement stable.

    À \(t=20\) s :

    \[
    \Delta\theta(20) \approx -5.7\times 10^{-4} \text{ rad},
    \]

    et :

    \[
    \Delta x(20) \approx -9.8\times 10^{-4} \text{ m}.
    \]

    Ces valeurs sont très proches de zéro.
    Le système revient donc bien vers l’équilibre en moins de 20 secondes.



    ### Choix retenu

    L’essai 1 est rejeté parce que la commande dépasse la limite autorisée :

    \[
    \max|\Delta\phi(t)| > \frac{\pi}{2}.
    \]

    Les essais 2 et 3 respectent les contraintes et stabilisent le système.
    On retient l’essai 3 car il pénalise davantage l’inclinaison \(\Delta\theta\), qui est une variable critique pour le redressement du booster, tout en gardant une commande admissible.

    Le contrôleur retenu est donc :

    \[
    K_{oc}
    =
    \begin{bmatrix}
    0.224 & 0.869 & -1.668 & -1.368
    \end{bmatrix}.
    \]

    Les graphes confirment que :
    - \(\Delta\theta(t)\) converge vers zéro ;
    - \(\Delta x(t)\) converge vers zéro ;
    - \(\Delta\phi(t)\) reste dans les limites autorisées ;
    - la dynamique en boucle fermée est asymptotiquement stable.

    Ainsi, le contrôleur optimal LQR permet de stabiliser le booster latéralement, tout en respectant les contraintes imposées sur l’angle du booster et l’angle de la tuyère.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
