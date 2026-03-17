from tkinter import *
import turtle


class KochSnowflake:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Koch Snowflake")  # Set a title

        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window)  # Create and add a frame to window
        frame1.pack()

        Label(frame1, text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()
        self.order.set("0")  # Default value
        entry = Entry(frame1, textvariable=self.order, justify=RIGHT, width=10)
        entry.pack(side=LEFT)

        Button(frame1, text="Display Koch Snowflake",
               command=self.display).pack(side=LEFT)

        # Create turtle canvas
        self.canvas = Canvas(window, width=600, height=600)
        self.canvas.pack()

        # Initialize turtle
        self.t = turtle.RawTurtle(self.canvas)
        self.t.speed(0)
        self.t.hideturtle()

        window.mainloop()  # Create an event loop

    def display(self):
        """Display the Koch snowflake"""
        self.t.clear()  # Clear previous drawing
        self.t.penup()

        try:
            order = int(self.order.get())
        except ValueError:
            self.t.goto(0, 0)
            self.t.write("Please enter a valid integer",
                         align="center", font=("Arial", 14, "bold"))
            return

        # Position turtle for right-side-up triangle
        self.t.goto(-200, -150)
        self.t.setheading(60)  # Point up-right
        self.t.pendown()

        # Draw the three sides
        for _ in range(3):
            self.drawKochCurve(order, 400)
            self.t.right(120)

        # Add order label
        self.t.penup()
        self.t.goto(0, 250)
        self.t.write(f"Order {order}", align="center",
                     font=("Arial", 16, "bold"))

    def drawKochCurve(self, order, length):
        """Draw Koch curve recursively"""
        if order == 0:  # Base condition
            self.t.forward(length)
        else:
            self.drawKochCurve(order - 1, length / 3)
            self.t.left(60)
            self.drawKochCurve(order - 1, length / 3)
            self.t.right(120)
            self.drawKochCurve(order - 1, length / 3)
            self.t.left(60)
            self.drawKochCurve(order - 1, length / 3)


# Create GUI
KochSnowflake()