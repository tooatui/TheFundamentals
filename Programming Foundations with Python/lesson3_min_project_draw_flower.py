# This is the lesson 3 mini project

import turtle

def draw_rhombus(some_turtle):
	the_smaller_angle = 45;
	the_bigger_angle = 180 - the_smaller_angle;

	for x in xrange(2):
		some_turtle.forward(100);
		some_turtle.right(the_smaller_angle);
		some_turtle.forward(100);
		some_turtle.right(the_bigger_angle);

def draw():
	window = turtle.Screen();
	window.bgcolor("white");

	rotate_angle = 10;
	rotate_times = 360 / rotate_angle;

	brad = turtle.Turtle();
	brad.shape("turtle");
	brad.color("blue");
	brad.pensize(2);
	brad.speed(0);


	for x in range(0, rotate_times):
		brad.right(rotate_angle);
		draw_rhombus(brad);

	brad.right(90);
	brad.forward(300);

	window.exitonclick();

draw();