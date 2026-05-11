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

    return np, plt, sci


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    g = 1.0
    M = 1.0
    l = 2.0
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La force de poussée $f$ s'applique à la base du booster. L'angle total de la poussée par rapport à la verticale est la somme de l'inclinaison du booster $\theta$ et de l'orientation de la tuyère $\phi$.

    En projetant cette force sur les axes cartésiens, et en respectant la convention trigonométrique — un angle positif $\theta$ penche le booster vers la gauche, ce qui oriente la force vers l'axe des abscisses négatives — on obtient :

    $$
    f_x = -f \sin(\theta + \phi)
    $$

    $$
    f_y = f \cos(\theta + \phi)
    $$
    """)
    return


@app.cell
def _(np):
    def force_components(f, theta, phi):
        fx = -f * np.sin(theta + phi)
        fy = f * np.cos(theta + phi)
        return fx, fy

    return (force_components,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    D'après la deuxième loi de Newton appliquée au centre de gravité ($\sum \vec{F} = M\vec{a}$), les accélérations dépendent des forces calculées précédemment et du poids de la fusée.

    * Sur l'axe horizontal, seule la composante $f_x$ intervient :
    $$M\ddot{x} = f_x \implies \ddot{x} = \frac{f_x}{M}$$

    * Sur l'axe vertical, la gravité s'oppose à la poussée :
    $$M\ddot{y} = f_y - Mg \implies \ddot{y} = \frac{f_y}{M} - g$$
    """)
    return


@app.cell
def _(M, force_components, g):
    def center_of_mass_acceleration(f, theta, phi):
        fx, fy = force_components(f, theta, phi)
        ax = fx / M
        ay = fy / M - g
        return ax, ay

    return (center_of_mass_acceleration,)


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
    Le booster est modélisé comme un tube rigide uniforme de longueur $\ell$ et de masse $M$. Le moment d'inertie pour un cylindre (ou une tige fine) tournant autour de son centre de masse (situé à $\ell/2$) est donné par la formule classique :

    $$J = \frac{1}{12} M \ell^2$$
    """)
    return


@app.cell
def _(M, l):
    J = M * l**2 / 12
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
    L'évolution de l'angle $\theta$ est régie par le principe fondamental de la dynamique en rotation ($\sum \tau = J\ddot{\theta}$).

    Le couple ($\tau$) est généré par la composante de la force perpendiculaire au booster, soit $f \sin(\phi)$, appliquée à une distance $\ell/2$ du centre de masse. Le signe négatif traduit le fait qu'un angle $\phi$ positif crée une rotation qui s'oppose à l'inclinaison positive $\theta$.

    $$J\ddot{\theta} = -f \sin(\phi) \cdot \frac{\ell}{2} \implies \ddot{\theta} = -\frac{f \ell \sin(\phi)}{2J}$$
    """)
    return


@app.cell
def _(J, l, np):
    def angular_acceleration(f, phi):
        return -(l / 2) * f * np.sin(phi) / J

    return (angular_acceleration,)


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
    * **Dimension de l'espace d'état :** $n = 6$. Nous avons besoin de la position et de la vitesse pour les 3 degrés de liberté ($x, y, \theta$).
    * **Vecteur d'état :** $s = \begin{bmatrix} x & v_x & y & v_y & \theta & \omega \end{bmatrix}^T$
    * **Fonction F (Équation d'état) :** Elle regroupe les dérivées du premier ordre calculées précédemment pour dicter l'évolution complète du système :

    $$\dot{s} = F(s, f, \phi) = \begin{bmatrix} v_x \\ \frac{1}{M}(-f \sin(\theta + \phi)) \\ v_y \\ \frac{1}{M}(f \cos(\theta + \phi)) - g \\ \omega \\ -\frac{f \ell \sin(\phi)}{2J} \end{bmatrix}$$
    """)
    return


@app.cell
def _(angular_acceleration, center_of_mass_acceleration, np):
    n = 6

    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s

        ax, ay = center_of_mass_acceleration(f, theta, phi)
        alpha = angular_acceleration(f, phi)

        return np.array([
            vx,
            ax,
            vy,
            ay,
            omega,
            alpha,
        ])

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


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    La fonction `redstart_solve` intègre numériquement le système d'équations différentielles
    en utilisant `scipy.integrate.solve_ivp` avec la méthode **Runge-Kutta RK45**.

    L'option `dense_output=True` permet de récupérer une solution **continue** interpolée,
    qu'on peut évaluer à n'importe quel instant $t$ (pas seulement aux points de grille).

    La fonction retournée `sol(t)` accepte :
    - un scalaire $t$ → retourne un vecteur de taille 6
    - un tableau 1D de temps → retourne une matrice $(6 \times N)$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    La fonction `redstart_solve` intègre numériquement le système d'équations différentielles
    en utilisant `scipy.integrate.solve_ivp` avec la méthode **Runge-Kutta RK45**.

    L'option `dense_output=True` permet de récupérer une solution **continue** interpolée,
    qu'on peut évaluer à n'importe quel instant $t$ (pas seulement aux points de grille).

    La fonction retournée `sol(t)` accepte :
    - un scalaire $t$ → retourne un vecteur de taille 6
    - un tableau 1D de temps → retourne une matrice $(6 \times N)$
    """)
    return


@app.cell
def _(J, M, g, l, np, sci):
    def redstart_solve(t_span, y0, f_phi):
        def dynamics(t, s):
            # Déballage du vecteur d'état
            x, vx, y, vy, theta, omega = s
        
            # Récupération de la commande à l'instant t
            f, phi = f_phi(t, s)
        
            # Projection des forces (avec le signe correct !)
            fx = -f * np.sin(theta + phi)
            fy = f * np.cos(theta + phi)
        
            # Application de la 2ème loi de Newton
            ax = fx / M
            ay = (fy / M) - g
        
            # Calcul du couple et accélération angulaire
            alpha = (-f * l * np.sin(phi)) / (2 * J)
        
            # Retourne les dérivées: [dx, dvx, dy, dvy, dtheta, domega]
            return [vx, ax, vy, ay, omega, alpha]

        # Résolution numérique du système
        res = sci.solve_ivp(dynamics, t_span, y0, dense_output=True)
        return res.sol

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


@app.cell
def _(g, l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]

        def f_phi(t, y):
            return np.array([0.0, 0.0])  # [f, phi]

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]

        t_cross = np.sqrt(2 * (10 - l) / g)

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.axvline(t_cross, color="grey", ls=":", label=rf"$t={t_cross:.2f}$ s")

        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.ylabel("height $y(t)$")
        plt.grid(True)
        plt.legend()

        return plt.gcf()

    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧩 Test de Chute Libre : Validation

    **1. Attente théorique :**
    En chute libre ($f=0$), l'équation du mouvement est $y(t) = y(0) - \frac{1}{2}gt^2$.
    Pour atteindre la hauteur $y = \ell$ (avec $y(0)=10$, $g=1$ et $\ell=2$), on trouve analytiquement $t = 4$ s.

    **2. Vérification numérique :**
    La simulation montre que la courbe numérique (bleue) croise bien la cible $y=2$ très exactement à l'abscisse $t = 4.00$ s.

    **Conclusion :** Cette correspondance parfaite valide l'exactitude de notre champ de vecteurs (matrice d'état) et la robustesse de notre intégration avec `solve_ivp`.
    """)
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


@app.cell
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0] 
    
        def f_phi(t, y):
            f = 0.384 * t + 0.44
            return np.array([f, 0.0])
        
        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
    
        y_t = sol(t)[2]
        vy_t = sol(t)[3]
        f_t = 0.384 * t + 0.44

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.plot(t, y_t, label=r"Position $y(t)$")
        ax.plot(t, vy_t, label=r"Vitesse $\dot{y}(t)$")
        ax.plot(t, f_t, label=r"Force $f(t)$")

        ax.axhline(l/2, color="grey", ls="--", label=r"$y=\ell/2$")
        ax.axhline(0, color="grey", ls=":", label=r"$\dot{y}=0$")

        ax.set_title("Controlled Landing")
        ax.set_xlabel("time $t$")
        ax.grid(True)
        ax.legend()

        final_state = sol(5.0)

        print("Final state at t=5:")
        print("x(5) =", final_state[0])
        print("vx(5) =", final_state[1])
        print("y(5) =", final_state[2])
        print("vy(5) =", final_state[3])
        print("theta(5) =", final_state[4])
        print("omega(5) =", final_state[5])

        return plt.gcf()

    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧩 Atterrissage Contrôlé : Validation

    *1. Attente théorique :*
    Notre loi de commande $f(t) = 0.384t + 0.44$ a été calculée analytiquement pour forcer le booster à atterrir en douceur en 5 secondes ($y(5)=1$ et $\dot{y}(5)=0$).

    *2. Vérification numérique :*
    Les courbes de la simulation confirment le succès total de la manœuvre :
    * *Position :* Atteint la cible $y=1$ sans jamais la dépasser (pas de crash).
    * *Vitesse :* S'annule parfaitement à l'instant terminal $t=5$ s.
    * *Force :* Reste strictement positive et croît linéairement (physiquement réalisable par un moteur).

    *Conclusion :* Notre modèle dynamique valide notre calcul de commande : le "soft landing" est parfaitement exécuté tout en respectant les limites physiques du système.
    """)
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

    return (svg,)


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


@app.function
def world(view_box, *objects):
    x_min, x_max, y_min, y_max = view_box

    width = x_max - x_min
    height = y_max - y_min

    objects_svg = "".join(str(obj) for obj in objects)

    return f"""
    <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="{x_min} {-y_max} {width} {height}"
        width="300"
        height="300"
        style="border: 1px solid black;"
    >
        <!-- Sky: cartesian y >= 0 -->
        <rect
            x="{x_min}"
            y="{-y_max}"
            width="{width}"
            height="{y_max}"
            fill="#87CEEB"
        />

        <!-- Ground: cartesian y <= 0 -->
        <rect
            x="{x_min}"
            y="0"
            width="{width}"
            height="{-y_min}"
            fill="#8B4513"
        />

        <!-- Cartesian objects: y-axis upwards -->
        <g transform="scale(1,-1)">
            <!-- Landing target: 2 meters wide, centered on (0,0) -->
            <rect
                x="-1"
                y="-0.04"
                width="2"
                height="0.08"
                fill="green"
            />

            {objects_svg}
        </g>
    </svg>
    """


@app.cell
def _(mo, svg):
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
    Les trois scènes de test permettent de vérifier que l’environnement affiche correctement :
    - un monde vide ;
    - un objet placé sur la zone d’atterrissage ;
    - des objets positionnés à différents endroits du repère cartésien.
    """)
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


@app.cell
def _(M, g, l, np):
    def booster(x, y, theta, f, phi):
        # Dimensions visuelles du booster
        body_width = 0.25
        flame_width = 0.18

        # Longueur de la flamme
        flame_length = (f / (M * g)) * (l / 2) if M * g != 0 else 0.0

        # Axe du booster (du centre vers le haut)
        ux = -np.sin(theta)
        uy =  np.cos(theta)

        # Vecteur perpendiculaire à l'axe
        nx =  np.cos(theta)
        ny =  np.sin(theta)

        # Centres du haut et du bas du booster
        top_x  = x + (l / 2) * ux
        top_y  = y + (l / 2) * uy
        base_x = x - (l / 2) * ux
        base_y = y - (l / 2) * uy

        # Coins du rectangle du corps
        p1 = (top_x  + (body_width / 2) * nx,  top_y  + (body_width / 2) * ny)
        p2 = (top_x  - (body_width / 2) * nx,  top_y  - (body_width / 2) * ny)
        p3 = (base_x - (body_width / 2) * nx, base_y - (body_width / 2) * ny)
        p4 = (base_x + (body_width / 2) * nx, base_y + (body_width / 2) * ny)

        body_points = " ".join(f"{px},{py}" for px, py in [p1, p2, p3, p4])

        # Direction de la flamme = opposée à la poussée
        dx =  np.sin(theta + phi)
        dy = -np.cos(theta + phi)

        # Perpendiculaire à la flamme
        px = np.cos(theta + phi)
        py = np.sin(theta + phi)

        # Triangle de la flamme
        flame_a = (base_x + (flame_width / 2) * px, base_y + (flame_width / 2) * py)
        flame_b = (base_x - (flame_width / 2) * px, base_y - (flame_width / 2) * py)
        flame_tip = (base_x + flame_length * dx, base_y + flame_length * dy)

        flame_points = " ".join(
            f"{qx},{qy}" for qx, qy in [flame_a, flame_b, flame_tip]
        )

        flame_svg = ""
        if f > 0:
            flame_svg = f'<polygon points="{flame_points}" fill="orange" />'

        return f"""
        <g>
            {flame_svg}
            <polygon points="{body_points}" fill="black" />
        </g>
        """

    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np):
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
    ### Interprétation — Booster Drawing

    La fonction `booster` représente le booster sous forme d’un corps rigide simplifié, dessiné comme un rectangle de longueur \(\ell\).
    Sa position est définie par les coordonnées \((x,y)\) de son centre de masse, et son orientation est donnée par l’angle \(\theta\), mesuré par rapport à l’axe vertical.


    Sa longueur est proportionnelle à l’intensité de la poussée \(f\). En particulier, lorsque \(f = Mg\), la longueur de la flamme est égale à \(\ell/2\), comme demandé dans l’énoncé.

    Les trois cas de test illustrent :
    1. un booster vertical sans poussée, donc sans flamme ;
    2. un booster vertical avec une poussée \(f=Mg\), ce qui produit une flamme alignée avec l’axe du booster ;
    3. un booster incliné avec un angle de réacteur non nul \(\phi\), ce qui modifie correctement l’orientation de la flamme.
    """)
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


@app.cell
def _(M, g, l, np):
    def booster_geometry(x, y, theta, f, phi):
        body_width = 0.25
        flame_width = 0.18

        flame_length = (f / (M * g)) * (l / 2) if M * g != 0 else 0.0

        ux = -np.sin(theta)
        uy = np.cos(theta)

        nx = np.cos(theta)
        ny = np.sin(theta)

        top_x = x + (l / 2) * ux
        top_y = y + (l / 2) * uy
        base_x = x - (l / 2) * ux
        base_y = y - (l / 2) * uy

        p1 = (top_x + (body_width / 2) * nx, top_y + (body_width / 2) * ny)
        p2 = (top_x - (body_width / 2) * nx, top_y - (body_width / 2) * ny)
        p3 = (base_x - (body_width / 2) * nx, base_y - (body_width / 2) * ny)
        p4 = (base_x + (body_width / 2) * nx, base_y + (body_width / 2) * ny)

        body_points = " ".join(f"{px},{py}" for px, py in [p1, p2, p3, p4])

        dx = np.sin(theta + phi)
        dy = -np.cos(theta + phi)

        px = np.cos(theta + phi)
        py = np.sin(theta + phi)

        flame_a = (base_x + (flame_width / 2) * px, base_y + (flame_width / 2) * py)
        flame_b = (base_x - (flame_width / 2) * px, base_y - (flame_width / 2) * py)
        flame_tip = (base_x + flame_length * dx, base_y + flame_length * dy)

        flame_points = " ".join(
            f"{qx},{qy}" for qx, qy in [flame_a, flame_b, flame_tip]
        )

        return body_points, flame_points


    def booster_anim(x, y, theta, f, phi, T, n_frames=60):
        ts = np.linspace(0, T, n_frames, endpoint=True)

        body_values = []
        flame_values = []

        for t in ts:
            body_points, flame_points = booster_geometry(
                x(t), y(t), theta(t), f(t), phi(t)
            )
            body_values.append(body_points)
            flame_values.append(flame_points)

        body_values_str = ";".join(body_values)
        flame_values_str = ";".join(flame_values)

        return f"""
        <g>
            <polygon points="{flame_values[0]}" fill="orange">
                <animate
                    attributeName="points"
                    values="{flame_values_str}"
                    dur="{T}s"
                    repeatCount="indefinite"
                />
            </polygon>

            <polygon points="{body_values[0]}" fill="black">
                <animate
                    attributeName="points"
                    values="{body_values_str}"
                    dur="{T}s"
                    repeatCount="indefinite"
                />
            </polygon>
        </g>
        """

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np):
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

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interprétation — Booster Animation

    La fonction `booster_anim` permet de passer d’un dessin statique à une animation SVG.
    Au lieu de recevoir des valeurs constantes pour \(x\), \(y\), \(\theta\), \(f\) et \(\phi\), elle reçoit des fonctions dépendant du temps.

    À chaque instant, la position, l’orientation, l’intensité de la poussée et la direction de la poussée sont recalculées.
    Cela permet d’animer simultanément le corps du booster et la flamme du réacteur.

    Dans l’exemple de test :
    - le booster se déplace de la gauche vers la droite ;
    - il monte légèrement ;
    - il effectue une rotation complète ;
    - l’intensité de la poussée augmente progressivement ;
    - l’orientation de la flamme varie au cours du temps.

    Cette animation confirme que la fonction met correctement à jour le corps du booster et la flamme à partir de fonctions dépendantes du temps.
    """)
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


@app.cell
def _(booster_anim, l, mo, np, redstart_solve):
    def simulated_booster_animation(
        t_span,
        y0,
        f_phi,
        view_box,
        stop_at_ground=False,
        extinguish_at_end=False,
    ):
        sol = redstart_solve(t_span, y0, f_phi)
        T = t_span[1] - t_span[0]

        # Temps de contact avec le sol : centre de masse à y = l/2
        t_ground = T

        if stop_at_ground:
            ts = np.linspace(t_span[0], t_span[1], 1000)
            y_values = sol(ts)[2]

            indices = np.where(y_values <= l / 2)[0]

            if len(indices) > 0:
                t_ground = ts[indices[0]]

        def clipped_time(t):
            return min(t, t_ground)

        def x_fun(t):
            tc = clipped_time(t)
            return sol(tc)[0]

        def y_fun(t):
            tc = clipped_time(t)
            return max(sol(tc)[2], l / 2)

        def theta_fun(t):
            tc = clipped_time(t)
            return sol(tc)[4]

        def f_fun(t):
            if extinguish_at_end and t >= t_ground:
                return 0.0

            tc = clipped_time(t)
            return f_phi(tc, sol(tc))[0]

        def phi_fun(t):
            tc = clipped_time(t)
            return f_phi(tc, sol(tc))[1]

        return mo.Html(
            world(
                view_box,
                booster_anim(x_fun, y_fun, theta_fun, f_fun, phi_fun, T=T)
            )
        )

    return (simulated_booster_animation,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Scénario 1: Chute Libre
    """)
    return


@app.cell
def _(np, simulated_booster_animation):
    def scenario_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        return simulated_booster_animation(
            t_span,
            y0,
            f_phi,
            view_box=[-3, 3, -2, 11],
            stop_at_ground=True,
        )

    return (scenario_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Scénario 2 : Poussée verticale constante f=Mg
    """)
    return


@app.cell
def _(M, g, np, simulated_booster_animation):
    def scenario_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([M * g, 0.0])

        return simulated_booster_animation(t_span, y0, f_phi, [-3, 3, -3, 11])

    return (scenario_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Scénario 3 : Poussée f=Mg et ϕ=π/8
    """)
    return


@app.cell
def _(M, g, np, simulated_booster_animation):
    def scenario_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([M * g, np.pi / 8])

        return simulated_booster_animation(t_span, y0, f_phi, [-15, 15, -5, 12])

    return (scenario_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Scénario 4 : Controlled landing
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve):
    def scenario_4():
        # Simulation physique jusqu'à l'atterrissage
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi(t, y):
            f = 0.384 * t + 0.44
            return np.array([f, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        # Animation un peu plus longue pour voir le booster posé
        T_anim = 6.0
        t_landing = 5.0

        def clipped_time(t):
            return min(t, t_landing)

        def x_fun(t):
            return sol(clipped_time(t))[0]

        def y_fun(t):
            return sol(clipped_time(t))[2]

        def theta_fun(t):
            return sol(clipped_time(t))[4]

        def f_fun(t):
            # Avant l'arrivée : force calculée
            # Après l'arrivée : moteur éteint
            if t >= t_landing:
                return 0.0
            return 0.384 * t + 0.44

        def phi_fun(t):
            return 0.0

        return mo.Html(
            world(
                [-3, 3, -2, 11],
                booster_anim(
                    x_fun,
                    y_fun,
                    theta_fun,
                    f_fun,
                    phi_fun,
                    T=T_anim,
                )
            )
        )

    return (scenario_4,)


@app.cell
def _(mo, scenario_1, scenario_2, scenario_3, scenario_4):
    mo.vstack(
        [
            mo.md("### 1. Free fall"),
            scenario_1(),

            mo.md("### 2. Constant thrust: $f = Mg$, $\\phi = 0$"),
            scenario_2(),

            mo.md("### 3. Constant thrust: $f = Mg$, $\\phi = \\pi/8$"),
            scenario_3(),

            mo.md("### 4. Controlled landing"),
            scenario_4(),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧩 Analyse des scénarios de simulation

    Les animations générées permettent de valider visuellement le comportement de notre modèle d’état selon différentes conditions de poussée.

    **Scénario 1 : Chute libre \((f=0)\)**

    Sans poussée, la seule force appliquée au booster est son poids \(Mg\). Le booster subit donc une accélération gravitationnelle vers le bas.
    Dans l’animation, il chute verticalement jusqu’à atteindre le sol. Une fois le contact avec le sol atteint, son mouvement est arrêté afin d’éviter qu’il traverse visuellement le pad d’atterrissage.

    **Scénario 2 : Poussée d’équilibre stationnaire \((f=Mg,\ \phi=0)\)**

    Dans ce cas, la poussée est verticale et alignée avec l’axe du booster. Elle compense exactement la gravité :

    \[
    \sum F_y = Mg - Mg = 0.
    \]

    Comme les vitesses initiales sont nulles, l’accélération est également nulle. Le booster reste donc en vol stationnaire parfait, ou *hovering*, à son altitude initiale \(y=10\).

    **Scénario 3 : Poussée désaxée \((f=Mg,\ \phi=\pi/8)\)**

    L’orientation de la tuyère crée une asymétrie physique importante.

    1. La composante verticale de la force vaut :

    \[
    Mg\cos\left(\frac{\pi}{8}\right)
    \]

    Comme cette valeur est inférieure au poids \(Mg\), la poussée ne compense plus totalement la gravité. Le booster perd donc de l’altitude.

    2. La composante horizontale de la force vaut :

    \[
    -Mg\sin\left(\frac{\pi}{8}\right)
    \]

    Elle est non nulle, ce qui génère une translation latérale du centre de masse.

    3. Comme la force est appliquée à la base du booster et qu’elle est désaxée par rapport à son axe principal, elle crée un couple :

    \[
    \tau = -\frac{\ell}{2}f\sin(\phi).
    \]

    Ce couple entraîne une accélération angulaire, donc une rotation du booster sur lui-même.

    Le comportement attendu est donc bien une combinaison de perte d’altitude, de déplacement latéral et de rotation.

    **Scénario 4 : Atterrissage contrôlé (*Soft Landing*)**

    Ce scénario valide l’objectif final du projet : réaliser un atterrissage doux du booster.

    Grâce à la loi de commande polynomiale \(f(t)\), le booster descend progressivement depuis sa hauteur initiale tout en réduisant sa vitesse verticale. À l’instant \(t=5\) s, il atteint le sol avec :

    \[
    y(5)=\frac{\ell}{2}=1,
    \qquad
    \dot{y}(5)=0.
    \]

    Le moteur est ensuite coupé afin de représenter l’arrêt de la poussée après le contact avec le sol.

    Dans le code, le temps physique d’atterrissage reste bien \(t=5\) s. L’animation est simplement prolongée légèrement après cet instant pour permettre de visualiser le booster posé au sol avec la flamme éteinte.

    Il s’agit donc d’un atterrissage contrôlé par une commande planifiée en temps, et non d’une stabilisation en boucle fermée.
    """)
    return


if __name__ == "__main__":
    app.run()
