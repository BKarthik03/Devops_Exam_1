import matplotlib.pyplot as plt

# Create a simple list of values
x = [1, 2, 3, 4, 5]
y = [i * 2 for i in x]

# Plot
plt.plot(x, y)
plt.title("Sample Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Save the output as an image
plt.savefig("output_plot.png")

print("Plot generated successfully!")
