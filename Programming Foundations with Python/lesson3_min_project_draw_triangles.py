# This is the lesson 3 mini project

import turtle
import math

def draw_triangle(some_turtle, line_length):
	for x in xrange(3):
		some_turtle.forward(line_length);
		some_turtle.left(120);

def draw_triangle_inside_triangle(some_turtle, start_x, start_y, line_length, level):
	if level > 0: 
		# go to the given starting position without drawing actual lines
		some_turtle.penup();
		some_turtle.goto(start_x, start_y);
		some_turtle.setheading(0);
		some_turtle.pendown();

		# draw the bigger green triangle
		some_turtle.fillcolor("green")
		some_turtle.begin_fill();
		draw_triangle(some_turtle, line_length);
		some_turtle.end_fill();

		# draw the smaller whilte triangle inside it
		line_length = line_length / 2;
		level = level - 1;
		some_turtle.forward(line_length);
		some_turtle.left(60);
		some_turtle.fillcolor("white")
		some_turtle.begin_fill();
		draw_triangle(some_turtle, line_length);
		some_turtle.end_fill();

		# draw inner same shpaes by giving the starting positions, line length, and the recursion level 
		draw_triangle_inside_triangle(some_turtle, start_x, start_y, line_length, level);
		draw_triangle_inside_triangle(some_turtle, start_x + line_length, start_y, line_length, level);
		draw_triangle_inside_triangle(some_turtle, start_x + line_length / 2, start_y + line_length / 2 * math.sqrt(3), line_length, level);

def draw():
	window = turtle.Screen();
	window.bgcolor("white");

	brad = turtle.Turtle();
	brad.shape("turtle");
	brad.color("blue");
	brad.pensize(2);
	brad.speed("slow");

	line_length = 400;
	level = 3;
	draw_triangle_inside_triangle(brad, 0, 0, line_length, level);

	window.exitonclick();

draw();